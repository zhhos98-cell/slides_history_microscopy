const sourceState={records:[],filtered:[]};
const sourceFiles=['source-registry.json','source-registry-02.json'];

function esc(v){return String(v??'').replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"})[c]);}
function words(r){return [r.institution,r.collection,r.country,r.city,r.type,r.relation,r.date_scope,r.holdings,r.research_use,(r.tags||[]).join(' ')].join(' ').toLowerCase();}

function fillSelect(id,values){
  const select=document.getElementById(id);
  [...new Set(values.filter(Boolean))].sort((a,b)=>a.localeCompare(b)).forEach(value=>{
    const option=document.createElement('option');option.value=value;option.textContent=value;select.appendChild(option);
  });
}

function relationLabel(value){
  return value==='direct'?'Direct evidence route':value==='portal'?'Digital primary-source portal':'Contextual route';
}

function renderRecord(r){
  const links=[`<a href="${esc(r.url)}" target="_blank" rel="noopener">Open source ↗</a>`];
  if(r.secondary_url)links.push(`<a href="${esc(r.secondary_url)}" target="_blank" rel="noopener">Related record ↗</a>`);
  return `<article class="source-record">
    <div class="source-place"><span>${esc(r.region)}</span><strong>${esc(r.city||r.country)}</strong><small>${esc(r.country)}</small></div>
    <div class="source-title">
      <p>${esc(r.institution)}</p>
      <h2>${esc(r.collection)}</h2>
      <div class="source-meta"><span>${esc(r.type)}</span><span class="relation-${esc(r.relation)}">${esc(relationLabel(r.relation))}</span><span>${esc(r.date_scope)}</span></div>
    </div>
    <div class="source-detail">
      <p>${esc(r.holdings)}</p>
      <p class="source-use">${esc(r.research_use)}</p>
      <details><summary>Access &amp; scope</summary><p>${esc(r.access)}</p></details>
      <p class="source-links">${links.join(' · ')}</p>
    </div>
  </article>`;
}

function applyFilters(){
  const q=document.getElementById('source-search').value.trim().toLowerCase();
  const region=document.getElementById('source-region').value;
  const type=document.getElementById('source-type').value;
  const relation=document.getElementById('source-relation').value;
  sourceState.filtered=sourceState.records.filter(r=>(!q||words(r).includes(q))&&(!region||r.region===region)&&(!type||r.type===type)&&(!relation||r.relation===relation));
  document.getElementById('source-list').innerHTML=sourceState.filtered.length?sourceState.filtered.map(renderRecord).join(''):'<p class="source-empty">No source route matches the current filters.</p>';
}

function bindFilters(){
  ['source-search','source-region','source-type','source-relation'].forEach(id=>document.getElementById(id).addEventListener(id==='source-search'?'input':'change',applyFilters));
  document.getElementById('source-reset').addEventListener('click',()=>{
    document.getElementById('source-search').value='';
    document.getElementById('source-region').value='';
    document.getElementById('source-type').value='';
    document.getElementById('source-relation').value='';
    applyFilters();
  });
}

function csvCell(v){const s=Array.isArray(v)?v.join('; '):String(v??'');return /[",\n]/.test(s)?`"${s.replace(/"/g,'""')}"`:s;}
function downloadCSV(){
  const fields=['id','region','country','city','institution','collection','type','relation','date_scope','holdings','research_use','access','url','secondary_url','tags'];
  const rows=sourceState.filtered.length?sourceState.filtered:sourceState.records;
  const text=[fields.join(','),...rows.map(r=>fields.map(f=>csvCell(r[f])).join(','))].join('\n')+'\n';
  const blob=new Blob([text],{type:'text/csv;charset=utf-8'}),url=URL.createObjectURL(blob),a=document.createElement('a');
  a.href=url;a.download='microscope-slides-source-registry.csv';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),500);
}

async function initSources(){
  try{
    const payloads=await Promise.all(sourceFiles.map(async path=>{
      const response=await fetch(path,{cache:'no-store'});if(!response.ok)throw new Error(`${path}: HTTP ${response.status}`);
      return response.json();
    }));
    sourceState.records=payloads.flatMap(data=>data.records||[]);
    sourceState.filtered=[...sourceState.records];
    fillSelect('source-region',sourceState.records.map(r=>r.region));
    fillSelect('source-type',sourceState.records.map(r=>r.type));
    bindFilters();
    document.getElementById('source-download-csv').addEventListener('click',downloadCSV);
    applyFilters();
  }catch(error){
    console.error(error);document.getElementById('source-list').innerHTML='<p class="source-empty">The source registry could not be loaded.</p>';
  }
}

initSources();
