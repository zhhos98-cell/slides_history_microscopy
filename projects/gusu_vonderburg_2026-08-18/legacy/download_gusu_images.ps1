param(
  [Parameter(Mandatory=$false)]
  [string]$CsvPath = ".\gusu_vonderburg_catalogue_manifest_resolved.csv",
  [Parameter(Mandatory=$false)]
  [string]$OutDir = ".\gusu_images"
)

$ErrorActionPreference = "Continue"
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

$rows = Import-Csv -LiteralPath $CsvPath
$ok = 0
$skip = 0
$fail = 0

foreach ($r in $rows) {
    $url = $r.direct_image_url
    if ([string]::IsNullOrWhiteSpace($url)) { $url = $r.print_image_url }
    if ([string]::IsNullOrWhiteSpace($url)) { $url = $r.web_image_url }
    if ([string]::IsNullOrWhiteSpace($url)) {
        $skip++
        continue
    }

    $fn = $r.filename_safe
    if ([string]::IsNullOrWhiteSpace($fn)) {
        $safeAcc = ($r.accession -replace '[^A-Za-z0-9]+','_').Trim('_')
        $fn = "$($r.museum_code)_$safeAcc.jpg"
    }
    $dest = Join-Path $OutDir $fn

    if (Test-Path -LiteralPath $dest) {
        $skip++
        continue
    }

    try {
        Invoke-WebRequest -Uri $url -OutFile $dest -UseBasicParsing -TimeoutSec 90
        $ok++
        Write-Host "[OK] $($r.machine_id) -> $fn"
    }
    catch {
        $fail++
        Write-Warning "[FAIL] $($r.machine_id): $($_.Exception.Message)"
    }
}

Write-Host "done: downloaded=$ok skipped=$skip failed=$fail"
