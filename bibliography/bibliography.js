const state={rows:[],filtered:[],manifest:null};

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
  return [row.authors,row.title,row.citation,row.type,row.language,row.tags,row.note].join(' ').toLowerCase();
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
      <p class="bib-meta"><span class="type">${escapeHTML(row.type)}</span><span>${escapeHTML(row.language||'Language unspecified')}</span>${tags.map(t=>`<span>${escapeHTML(t)}</span>`).join('')}</p>
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
  document.getElementById('bib-result-count').textContent=`${state.filtered.length} of ${state.rows.length} verified slide-locked entries`;
  renderSection('research','research-list','research');
  renderSection('primary','primary-list','primary');
  updateExportStatus();
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

function csvCell(value,delimiter=','){
  const text=String(value??'');
  if(text.includes('"')||text.includes('\n')||text.includes('\r')||text.includes(delimiter))return `"${text.replace(/"/g,'""')}"`;
  return text;
}

function tabularText(rows,delimiter=','){
  if(!rows.length)return '';
  const fields=Object.keys(state.rows[0]||rows[0]);
  return [fields.join(delimiter),...rows.map(row=>fields.map(field=>csvCell(row[field],delimiter)).join(delimiter))].join('\n')+'\n';
}

function firstURL(row){return parseLinks(row.links)[0]?.url||'';}

function extractDOI(row){
  for(const link of parseLinks(row.links)){
    try{
      const u=new URL(link.url);
      if(u.hostname.toLowerCase()==='doi.org')return decodeURIComponent(u.pathname.replace(/^\//,''));
    }catch{}
  }
  const match=String(row.links||'').match(/10\.\d{4,9}\/[-._;()/:A-Z0-9]+/i);
  return match?match[0].replace(/[.,;]+$/,''):'';
}

function parseName(name){
  const clean=String(name||'').trim();
  if(!clean)return null;
  if(/^Meyers Konversations-Lexikon$/i.test(clean))return {literal:clean};
  const parts=clean.split(/\s+/);
  if(parts.length===1)return {literal:clean};
  const particles=new Set(['da','de','del','der','di','du','la','le','van','von']);
  let familyStart=parts.length-1;
  while(familyStart>0&&particles.has(parts[familyStart-1].toLowerCase()))familyStart--;
  return {given:parts.slice(0,familyStart).join(' '),family:parts.slice(familyStart).join(' ')};
}

function parseCreators(value){
  const creators=[];
  String(value||'').split(/\s*;\s*/).filter(Boolean).forEach(group=>{
    let role='author';
    let text=group.trim();
    if(/^ed\.\s+/i.test(text)){role='editor';text=text.replace(/^ed\.\s+/i,'');}
    const names=text.replace(/,\s+and\s+/gi,'|').replace(/\s+and\s+/gi,'|').replace(/,\s+(?=[A-ZÀ-ÖØ-Þ])/g,'|').split('|').map(v=>v.trim()).filter(Boolean);
    names.forEach(name=>{const parsed=parseName(name);if(parsed)creators.push({role,...parsed});});
  });
  return creators;
}

function cslType(row){
  const type=String(row.type||'').toLowerCase();
  if(type.includes('encyclopedia'))return 'entry-encyclopedia';
  if(type==='book'||type==='manual')return 'book';
  if(type.includes('collection essay'))return 'webpage';
  return 'article-journal';
}

function cslRecord(row){
  const creators=parseCreators(row.authors);
  const author=creators.filter(c=>c.role==='author').map(({given,family,literal})=>literal?{literal}:{given,family});
  const editor=creators.filter(c=>c.role==='editor').map(({given,family,literal})=>literal?{literal}:{given,family});
  const record={
    id:row.id,
    type:cslType(row),
    title:row.title,
    issued:{'date-parts':[[Number(row.year)]]},
    language:row.language||undefined,
    keyword:splitTags(row.tags).join(', '),
    note:`${row.citation}${row.note?`\n\n${row.note}`:''}`,
    URL:firstURL(row)||undefined,
    DOI:extractDOI(row)||undefined
  };
  if(author.length)record.author=author;
  if(editor.length)record.editor=editor;
  return Object.fromEntries(Object.entries(record).filter(([,value])=>value!==undefined&&value!==''));
}

function bibType(row){
  const type=String(row.type||'').toLowerCase();
  if(type==='book'||type==='manual')return 'book';
  if(type.includes('encyclopedia'))return 'inreference';
  if(type.includes('collection essay'))return 'misc';
  return 'article';
}

function bibEscape(value){return String(value??'').replace(/\\/g,'\\\\').replace(/[{}]/g,ch=>`\\${ch}`).replace(/\s+/g,' ').trim();}

function creatorDisplay(creator){return creator.literal||[creator.given,creator.family].filter(Boolean).join(' ');}

function bibtexText(rows){
  return rows.map(row=>{
    const creators=parseCreators(row.authors);
    const authors=creators.filter(c=>c.role==='author').map(creatorDisplay).join(' and ');
    const editors=creators.filter(c=>c.role==='editor').map(creatorDisplay).join(' and ');
    const fields=[
      ['title',row.title],['author',authors],['editor',editors],['year',row.year],['language',row.language],['keywords',splitTags(row.tags).join(', ')],['doi',extractDOI(row)],['url',firstURL(row)],['note',`${row.citation}${row.note?` — ${row.note}`:''}`]
    ].filter(([,value])=>String(value||'').trim()!=='');
    return `@${bibType(row)}{${row.id},\n${fields.map(([key,value])=>`  ${key} = {${bibEscape(value)}}`).join(',\n')}\n}`;
  }).join('\n\n')+'\n';
}

function risType(row){
  const type=String(row.type||'').toLowerCase();
  if(type==='book'||type==='manual')return 'BOOK';
  if(type.includes('encyclopedia'))return 'ENCYC';
  if(type.includes('collection essay'))return 'ELEC';
  return 'JOUR';
}

function risText(rows){
  return rows.map(row=>{
    const creators=parseCreators(row.authors);
    const lines=[`TY  - ${risType(row)}`,`ID  - ${row.id}`,`TI  - ${row.title}`];
    creators.filter(c=>c.role==='author').forEach(c=>lines.push(`AU  - ${creatorDisplay(c)}`));
    creators.filter(c=>c.role==='editor').forEach(c=>lines.push(`ED  - ${creatorDisplay(c)}`));
    lines.push(`PY  - ${row.year}`);
    if(row.language)lines.push(`LA  - ${row.language}`);
    splitTags(row.tags).forEach(tag=>lines.push(`KW  - ${tag}`));
    const doi=extractDOI(row),url=firstURL(row);
    if(doi)lines.push(`DO  - ${doi}`);
    if(url)lines.push(`UR  - ${url}`);
    lines.push(`N1  - ${row.citation}`);
    if(row.note)lines.push(`N1  - ${row.note}`);
    lines.push('ER  - ');
    return lines.join('\n');
  }).join('\n\n')+'\n';
}

function exportRows(){
  return document.getElementById('bib-export-scope')?.value==='filtered'?state.filtered:state.rows;
}

function updateExportStatus(message=''){
  const status=document.getElementById('bib-export-status');
  if(!status)return;
  const scope=document.getElementById('bib-export-scope')?.value||'all';
  const count=scope==='filtered'?state.filtered.length:state.rows.length;
  status.textContent=message||`${count} entries ready · ${scope==='filtered'?'current filtered view':'complete bibliography'}`;
}

function downloadBlob(filename,text,mime){
  const blob=new Blob([text],{type:mime});
  const url=URL.createObjectURL(blob);
  const a=document.createElement('a');a.href=url;a.download=filename;document.body.appendChild(a);a.click();a.remove();
  setTimeout(()=>URL.revokeObjectURL(url),1000);
}

function exportFormat(format){
  const rows=exportRows();
  if(!rows.length){updateExportStatus('No rows in the selected export scope.');return;}
  const scope=document.getElementById('bib-export-scope')?.value==='filtered'?'filtered':'all';
  const stem=`microscope-slides-bibliography-${scope}`;
  let text='',extension='',mime='text/plain;charset=utf-8';
  if(format==='csv'){text=tabularText(rows,',');extension='csv';mime='text/csv;charset=utf-8';}
  else if(format==='tsv'){text=tabularText(rows,'\t');extension='tsv';mime='text/tab-separated-values;charset=utf-8';}
  else if(format==='json'){
    text=JSON.stringify({schema_version:'1.0',bibliography_version:state.manifest?.version||'',release_date:state.manifest?.date||'',scope,records:rows},null,2)+'\n';
    extension='json';mime='application/json;charset=utf-8';
  }
  else if(format==='csl-json'){text=JSON.stringify(rows.map(cslRecord),null,2)+'\n';extension='csl.json';mime='application/json;charset=utf-8';}
  else if(format==='bibtex'){text=bibtexText(rows);extension='bib';mime='application/x-bibtex;charset=utf-8';}
  else if(format==='ris'){text=risText(rows);extension='ris';mime='application/x-research-info-systems;charset=utf-8';}
  else return;
  downloadBlob(`${stem}.${extension}`,text,mime);
  updateExportStatus(`${rows.length} entries exported · ${format.toUpperCase()}`);
}

function bindExportControls(){
  const scope=document.getElementById('bib-export-scope');
  if(scope)scope.addEventListener('change',()=>updateExportStatus());
  document.querySelectorAll('[data-bib-export]').forEach(button=>button.addEventListener('click',()=>exportFormat(button.dataset.bibExport)));
  updateExportStatus();
}

async function init(){
  try{
    const manifestResponse=await fetch('bibliography-manifest.json',{cache:'no-store'});
    if(!manifestResponse.ok)throw new Error(`manifest HTTP ${manifestResponse.status}`);
    const manifest=await manifestResponse.json();
    state.manifest=manifest;
    const parts=await Promise.all(manifest.chunks.map(async path=>{
      const response=await fetch(path,{cache:'no-store'});
      if(!response.ok)throw new Error(`${path}: HTTP ${response.status}`);
      return parseCSV(await response.text());
    }));
    state.rows=parts.flat();
    const research=state.rows.filter(r=>r.section==='research').length;
    const primary=state.rows.filter(r=>r.section==='primary').length;
    const languages=new Set(state.rows.map(r=>r.language).filter(Boolean));
    if(state.rows.length!==manifest.total_entries||research!==manifest.research||primary!==manifest.primary||languages.size!==manifest.publication_languages)throw new Error(`bibliography contract mismatch: ${state.rows.length}/${research}/${primary}/${languages.size}`);
    state.filtered=[...state.rows];
    populateTags();
    bindControls();
    bindExportControls();
    applyFilters();
  }catch(error){
    console.error(error);
    document.getElementById('bib-result-count').textContent='Bibliography data failed to load';
    document.getElementById('research-list').innerHTML=`<p class="bib-empty">The bibliography CSV could not be loaded. ${escapeHTML(error.message)}</p>`;
    document.getElementById('primary').hidden=true;
    updateExportStatus('Export unavailable because bibliography data failed to load.');
  }
}

init();
