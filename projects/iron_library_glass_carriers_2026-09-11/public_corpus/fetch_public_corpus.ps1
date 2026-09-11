[CmdletBinding()]
param(
    [string[]]$Only = @(),
    [switch]$IiifImages,
    [switch]$LocalFiles,
    [switch]$Force,
    [ValidateRange(0, 10000)]
    [int]$DelayMs = 200
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Windows PowerShell 5.1 can otherwise negotiate an old TLS version on some systems.
try {
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
} catch {}

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$ManifestPath = Join-Path $Root 'manifest.tsv'
$RawRoot = Join-Path $Root 'raw'
$UserAgent = 'slides-history-microscopy-research-fetcher/1.0'

if (-not (Test-Path -LiteralPath $ManifestPath)) {
    throw "manifest.tsv not found: $ManifestPath"
}

New-Item -ItemType Directory -Force -Path $RawRoot | Out-Null

$Http = [System.Net.Http.HttpClient]::new()
$Http.DefaultRequestHeaders.UserAgent.ParseAdd($UserAgent)
$Http.Timeout = [TimeSpan]::FromMinutes(5)

function Get-PropertyValue {
    param(
        [Parameter(Mandatory = $true)]$Object,
        [Parameter(Mandatory = $true)][string]$Name
    )
    if ($null -eq $Object) { return $null }
    $p = $Object.PSObject.Properties[$Name]
    if ($null -eq $p) { return $null }
    return $p.Value
}

function ConvertTo-SafeName {
    param([Parameter(Mandatory = $true)][string]$Value)
    $name = $Value -replace '[\\/:*?"<>|]', '_'
    $name = $name -replace '[^A-Za-z0-9._()\- ]', '_'
    $name = $name -replace '\s+', '_'
    $name = $name.Trim(' ', '.', '_')
    if ([string]::IsNullOrWhiteSpace($name)) { return 'source' }
    if ($name.Length -gt 120) { $name = $name.Substring(0, 120) }
    return $name
}

function Get-Bytes {
    param([Parameter(Mandatory = $true)][string]$Url)

    $response = $Http.GetAsync($Url).GetAwaiter().GetResult()
    try {
        $response.EnsureSuccessStatusCode() | Out-Null
        $bytes = $response.Content.ReadAsByteArrayAsync().GetAwaiter().GetResult()
        $contentType = $null
        if ($null -ne $response.Content.Headers.ContentType) {
            $contentType = $response.Content.Headers.ContentType.MediaType
        }
        return [pscustomobject]@{
            Bytes       = $bytes
            ContentType = $contentType
            FinalUrl    = $response.RequestMessage.RequestUri.AbsoluteUri
        }
    }
    finally {
        $response.Dispose()
    }
}

function Save-RemoteFile {
    param(
        [Parameter(Mandatory = $true)][string]$Url,
        [Parameter(Mandatory = $true)][string]$Destination,
        [switch]$Overwrite
    )

    if ((Test-Path -LiteralPath $Destination) -and -not $Overwrite) {
        Write-Host "exists, skip: $Destination"
        return $null
    }

    $parent = Split-Path -Parent $Destination
    New-Item -ItemType Directory -Force -Path $parent | Out-Null

    $result = Get-Bytes -Url $Url
    [IO.File]::WriteAllBytes($Destination, $result.Bytes)
    return $result
}

function Get-IiifLabel {
    param($Label, [int]$Fallback)

    if ($null -eq $Label) { return [string]$Fallback }
    if ($Label -is [string]) { return $Label }

    # IIIF Presentation 3 language-map label.
    foreach ($prop in $Label.PSObject.Properties) {
        if ($prop.Value -is [System.Array] -and $prop.Value.Count -gt 0) {
            return [string]$prop.Value[0]
        }
    }
    return [string]$Fallback
}

function Get-IiifServiceUrl {
    param($Resource)

    if ($null -eq $Resource) { return $null }

    $service = Get-PropertyValue -Object $Resource -Name 'service'
    if ($service -is [System.Array]) {
        if ($service.Count -eq 0) { $service = $null }
        else { $service = $service[0] }
    }

    if ($null -ne $service) {
        $base = Get-PropertyValue -Object $service -Name 'id'
        if ([string]::IsNullOrWhiteSpace([string]$base)) {
            $base = Get-PropertyValue -Object $service -Name '@id'
        }
        if (-not [string]::IsNullOrWhiteSpace([string]$base)) {
            $type = [string](Get-PropertyValue -Object $service -Name 'type')
            if ($type -match 'ImageService3') {
                return ([string]$base).TrimEnd('/') + '/full/max/0/default.jpg'
            }
            return ([string]$base).TrimEnd('/') + '/full/full/0/default.jpg'
        }
    }

    $direct = Get-PropertyValue -Object $Resource -Name 'id'
    if ([string]::IsNullOrWhiteSpace([string]$direct)) {
        $direct = Get-PropertyValue -Object $Resource -Name '@id'
    }
    if ([string]::IsNullOrWhiteSpace([string]$direct)) { return $null }
    return [string]$direct
}

function Get-IiifCanvases {
    param([Parameter(Mandatory = $true)]$Manifest)

    $rows = [System.Collections.Generic.List[object]]::new()

    # IIIF Presentation 2
    $sequences = Get-PropertyValue -Object $Manifest -Name 'sequences'
    if ($null -ne $sequences -and $sequences.Count -gt 0) {
        $canvases = Get-PropertyValue -Object $sequences[0] -Name 'canvases'
        $n = 0
        foreach ($canvas in $canvases) {
            $n++
            $label = Get-IiifLabel -Label (Get-PropertyValue -Object $canvas -Name 'label') -Fallback $n
            $resource = $null
            $images = Get-PropertyValue -Object $canvas -Name 'images'
            if ($null -ne $images -and $images.Count -gt 0) {
                $resource = Get-PropertyValue -Object $images[0] -Name 'resource'
            }

            $rows.Add([pscustomobject]@{
                Sequence = $n
                Label    = $label
                ImageUrl = Get-IiifServiceUrl -Resource $resource
            })
        }
        return $rows
    }

    # IIIF Presentation 3
    $items = Get-PropertyValue -Object $Manifest -Name 'items'
    if ($null -ne $items) {
        $n = 0
        foreach ($canvas in $items) {
            $n++
            $label = Get-IiifLabel -Label (Get-PropertyValue -Object $canvas -Name 'label') -Fallback $n
            $resource = $null

            $annotationPages = Get-PropertyValue -Object $canvas -Name 'items'
            if ($null -ne $annotationPages -and $annotationPages.Count -gt 0) {
                $annotations = Get-PropertyValue -Object $annotationPages[0] -Name 'items'
                if ($null -ne $annotations -and $annotations.Count -gt 0) {
                    $resource = Get-PropertyValue -Object $annotations[0] -Name 'body'
                }
            }

            $rows.Add([pscustomobject]@{
                Sequence = $n
                Label    = $label
                ImageUrl = Get-IiifServiceUrl -Resource $resource
            })
        }
    }

    return $rows
}

function Invoke-IiifHarvest {
    param(
        [Parameter(Mandatory = $true)]$Row,
        [switch]$DownloadImages
    )

    $sourceId = ConvertTo-SafeName ([string]$Row.id)
    $outDir = Join-Path (Join-Path $RawRoot 'e_codices') $sourceId
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null

    $manifestFile = Join-Path $outDir 'manifest.json'
    $manifestDownload = Save-RemoteFile -Url ([string]$Row.url) -Destination $manifestFile -Overwrite:$Force
    if ($null -ne $manifestDownload) {
        Write-Host "saved manifest: $($Row.id)"
    }

    $manifest = Get-Content -LiteralPath $manifestFile -Raw -Encoding UTF8 | ConvertFrom-Json
    $canvases = @(Get-IiifCanvases -Manifest $manifest)

    $indexFile = Join-Path $outDir 'canvas_index.tsv'
    $indexLines = [System.Collections.Generic.List[string]]::new()
    $indexLines.Add("sequence`tlabel`timage_url")
    foreach ($canvas in $canvases) {
        $cleanLabel = ([string]$canvas.Label) -replace "`t", ' ' -replace "`r?`n", ' '
        $indexLines.Add("$($canvas.Sequence)`t$cleanLabel`t$($canvas.ImageUrl)")
    }
    [IO.File]::WriteAllLines($indexFile, $indexLines, [Text.UTF8Encoding]::new($false))
    Write-Host "indexed: $($Row.id) ($($canvases.Count) canvases)"

    if (-not $DownloadImages) { return }

    $pagesDir = Join-Path $outDir 'pages'
    New-Item -ItemType Directory -Force -Path $pagesDir | Out-Null

    foreach ($canvas in $canvases) {
        if ([string]::IsNullOrWhiteSpace([string]$canvas.ImageUrl)) {
            Write-Warning "no image URL: $($Row.id) canvas $($canvas.Sequence)"
            continue
        }

        $safeLabel = ConvertTo-SafeName ([string]$canvas.Label)
        $filename = ('{0:D4}_{1}.jpg' -f [int]$canvas.Sequence, $safeLabel)
        $destination = Join-Path $pagesDir $filename
        $downloaded = Save-RemoteFile -Url ([string]$canvas.ImageUrl) -Destination $destination -Overwrite:$Force
        if ($null -ne $downloaded) {
            Write-Host "downloaded $($Row.id) $($canvas.Sequence)/$($canvases.Count): $($canvas.Label)"
            if ($DelayMs -gt 0) { Start-Sleep -Milliseconds $DelayMs }
        }
    }
}

function Get-ExtensionFromContentType {
    param([string]$ContentType)
    switch -Regex ($ContentType) {
        '^application/pdf' { return '.pdf' }
        '^image/jpeg'      { return '.jpg' }
        '^image/png'       { return '.png' }
        '^text/html'       { return '.html' }
        '^application/json' { return '.json' }
        default            { return '.bin' }
    }
}

function Invoke-LocalFileHarvest {
    param([Parameter(Mandatory = $true)]$Row)

    $sourceId = ConvertTo-SafeName ([string]$Row.id)
    $filesDir = Join-Path $RawRoot 'files'
    New-Item -ItemType Directory -Force -Path $filesDir | Out-Null

    $existing = Get-ChildItem -LiteralPath $filesDir -Filter "$sourceId.*" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($null -ne $existing -and -not $Force) {
        Write-Host "exists, skip: $($existing.FullName)"
        return
    }

    $result = Get-Bytes -Url ([string]$Row.url)
    $extension = Get-ExtensionFromContentType -ContentType ([string]$result.ContentType)
    $destination = Join-Path $filesDir ($sourceId + $extension)
    [IO.File]::WriteAllBytes($destination, $result.Bytes)
    Write-Host "saved local research copy: $($Row.id) -> $destination [$($result.ContentType)]"
}

try {
    $rows = Import-Csv -LiteralPath $ManifestPath -Delimiter "`t"
    $selected = @{}
    foreach ($id in $Only) { $selected[$id] = $true }

    foreach ($row in $rows) {
        if ($selected.Count -gt 0 -and -not $selected.ContainsKey([string]$row.id)) {
            continue
        }

        try {
            switch ([string]$row.fetch_mode) {
                'iiif' {
                    Invoke-IiifHarvest -Row $row -DownloadImages:$IiifImages
                }
                'local_file' {
                    if ($LocalFiles) {
                        Invoke-LocalFileHarvest -Row $row
                    } else {
                        Write-Host "local_file skipped by policy: $($row.id) -> $($row.url)"
                    }
                }
                default {
                    Write-Host "link only: $($row.id) -> $($row.url)"
                }
            }
        }
        catch {
            Write-Warning "ERROR $($row.id): $($_.Exception.Message)"
        }
    }
}
finally {
    $Http.Dispose()
}
