const state={rows:[],filtered:[]};

function parseCSV(text){
  const rows=[];let row=[],field='',quoted=false;
  for(let i=0;i<text.length;i++){
    const ch=text[i],next=text[i+1];
    if(quoted){
      if(ch==='"'&&next==='"'){field+='"';i++;}
      else if(ch==='"'){quoted=false;}
      else field+=ch;
      continue;
    }
    if(ch==='"') quoted=true;
    else if(ch===','){row.push(field);field='';}
    else if(ch==='\n'){row.push(field.replace(/\r$/,''));rows.push(row);row=[];field='';}
    else field+=ch;
  }
  if(field.length||row.length){row.push(field.replace(/\r$/,''));rows.push(row);}
  const header=rows.shift()||[];
  return rows.filter(r=>r.some(v=>v.trim()!=='')).map(r=>Object.fromEntries(header.map((k,i)=>[k,r[i]??''])));
}

function escapeHTML(value){
  return String(value??'').replace(/[&<>'"]/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;",'"':"&quot;"})[ch]);
}

function safeURL(value){
  try{const u=new URL(value);return ['http:','https:'].includes(u.protocol)?u.href:'';}catch{return '';}
}

function splitTags(value){return String(value||'').split(';').map(v=>v.trim()).filter(Boolean);}

function parseLinks(value){
  return String(value||'').split(';').map(part=>part.trim()).filter(Boolean).map(part=>{
    const match=part.match(/^(.+?):\s+(https?:\/\/\S+)$/);
    return match?{label:match[1].trim(),url:safeURL(match[2].trim())}:null;
  }).filter(v=>v&&v.url);
}

function haystack(row){
  return [row.authors,row.title,row.citation,row.type,row.tags,row.note].join(' ').toLowerCase();
}

function renderLinks(row){
  const links=parseLinks(row.links);
  if(!links.length)return '';
  return `<p class="bib-links">${links.map(l=>`<a href="${escapeHTML(l.url)}" target="_blank" rel="noopener">${escapeHTML(l.label)} ↗</a>`).join(' · ')}</p>`;
}

function renderEntry(row){
  const tags=splitTags(row.tags);
  return `<article class="bib-entry" id="${escapeHTML(row.id)}">
    <p class="bib-year">${escapeHTML(row.year)}</p>
    <div>
      <h3>${escapeHTML(row.citation)}</h3>
      <p class="bib-note">${escapeHTML(row.note)}</p>
      <p class="bib-meta"><span class="type">${escapeHTML(row.type)}</span>${tags.map(t=>`<span>${escapeHTML(t)}</span>`).join('')}</p>
      ${renderLinks(row)}
    </div>
  </article>`;
}

function renderSection(section,elementId,sectionId){
  const rows=state.filtered.filter(r=>r.section===section).sort((a,b)=>Number(a.year)-Number(b.year)||a.authors.localeCompare(b.authors));
  const target=document.getElementById(elementId),sectionEl=document.getElementById(sectionId);
  sectionEl.hidden=rows.length===0;
  target.innerHTML=rows.length?rows.map(renderEntry).join(''):'<p class="bib-empty">No entries match the current filters.</p>';
}

function applyFilters(){
  const q=document.getElementById('bib-search').value.trim().toLowerCase();
  const section=document.getElementById('bib-section-filter').value;
  const tag=document.getElementById('bib-tag-filter').value;
  state.filtered=state.rows.filter(row=>(!section||row.section===section)&&(!tag||splitTags(row.tags).includes(tag))&&(!q||haystack(row).includes(q)));
  document.getElementById('bib-result-count').textContent=`${state.filtered.length} of ${state.rows.length} verified entries`;
  renderSection('research','research-list','research');
  renderSection('primary','primary-list','primary');
}

function populateTags(){
  const select=document.getElementById('bib-tag-filter');
  const tags=[...new Set(state.rows.flatMap(r=>splitTags(r.tags)))].sort((a,b)=>a.localeCompare(b));
  tags.forEach(tag=>{const option=document.createElement('option');option.value=tag;option.textContent=tag;select.appendChild(option);});
}

function bindControls(){
  document.getElementById('bib-search').addEventListener('input',applyFilters);
  document.getElementById('bib-section-filter').addEventListener('change',applyFilters);
  document.getElementById('bib-tag-filter').addEventListener('change',applyFilters);
  document.getElementById('bib-reset').addEventListener('click',()=>{
    document.getElementById('bib-search').value='';
    document.getElementById('bib-section-filter').value='';
    document.getElementById('bib-tag-filter').value='';
    applyFilters();
  });
}

async function init(){
  try{
    const response=await fetch('bibliography.csv',{cache:'no-store'});
    if(!response.ok)throw new Error(`HTTP ${response.status}`);
    state.rows=parseCSV(await response.text());
    const research=state.rows.filter(r=>r.section==='research').length;
    const primary=state.rows.filter(r=>r.section==='primary').length;
    if(state.rows.length!==44||research!==31||primary!==13)throw new Error(`bibliography contract mismatch: ${state.rows.length}/${research}/${primary}`);
    state.filtered=[...state.rows];
    populateTags();
    bindControls();
    applyFilters();
  }catch(error){
    console.error(error);
    document.getElementById('bib-result-count').textContent='Bibliography data failed to load';
    document.getElementById('research-list').innerHTML=`<p class="bib-empty">The bibliography CSV could not be loaded. ${escapeHTML(error.message)}</p>`;
    document.getElementById('primary').hidden=true;
  }
}

init();
