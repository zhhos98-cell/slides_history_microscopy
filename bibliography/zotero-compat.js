(() => {
  const SOURCE_ID = 'info:sid/zhhos98-cell.github.io:slides_history_microscopy';
  let notifyTimer = null;

  function creators(row) {
    try {
      return parseCreators(row.authors)
        .filter(creator => creator.role === 'author')
        .map(creator => ({
          given: String(creator.given || '').trim(),
          family: String(creator.family || '').trim(),
          literal: String(creator.literal || '').trim()
        }))
        .filter(creator => creator.literal || creator.family || creator.given);
    } catch {
      return String(row.authors || '')
        .replace(/;\s*ed\.\s+.*$/i, '')
        .replace(/,\s+and\s+/gi, '|')
        .replace(/\s+and\s+/gi, '|')
        .replace(/,\s+(?=[A-ZÀ-ÖØ-Þ])/g, '|')
        .split('|')
        .map(value => value.trim())
        .filter(Boolean)
        .map(name => {
          const parts = name.split(/\s+/);
          return parts.length > 1
            ? { given: parts.slice(0, -1).join(' '), family: parts.at(-1), literal: '' }
            : { given: '', family: '', literal: name };
        });
    }
  }

  function creatorDisplay(creator) {
    return creator.literal || [creator.given, creator.family].filter(Boolean).join(' ');
  }

  function doiFor(row) {
    try { return extractDOI(row) || ''; } catch { return ''; }
  }

  function urlFor(row) {
    try { return firstURL(row) || ''; } catch { return ''; }
  }

  function explicitISBN(row) {
    const text = `${row.citation || ''} ${row.note || ''} ${row.links || ''}`;
    const match = text.match(/\bISBN(?:-1[03])?\s*[:#]?\s*((?:97[89][\s-]?)?\d[\d\s-]{7,16}[\dXx])\b/i);
    return match ? match[1].replace(/[\s-]/g, '') : '';
  }

  function citationAfterTitle(row) {
    const citation = String(row.citation || '');
    const title = String(row.title || '');
    const index = title ? citation.indexOf(title) : -1;
    if (index < 0) return '';
    return citation.slice(index + title.length).replace(/^[”’"']+\s*,?\s*/, '').trim();
  }

  function journalMetadata(row) {
    const result = { journal: '', volume: '', issue: '', pages: '', spage: '', epage: '' };
    const tail = citationAfterTitle(row);
    if (!tail) return result;
    const yearToken = `(${row.year})`;
    const yearIndex = tail.lastIndexOf(yearToken);
    if (yearIndex < 0) return result;
    let beforeYear = tail.slice(0, yearIndex).trim().replace(/,$/, '').trim();
    const afterYear = tail.slice(yearIndex + yearToken.length);
    const pageMatch = afterYear.match(/:\s*([0-9A-Za-z]+(?:\s*[–—-]\s*[0-9A-Za-z]+)?)/);
    if (pageMatch) {
      result.pages = pageMatch[1].replace(/\s+/g, '');
      const parts = result.pages.split(/[–—-]/).map(v => v.trim()).filter(Boolean);
      result.spage = parts[0] || '';
      result.epage = parts[1] || '';
    }
    const issueMatch = beforeYear.match(/,\s*(?:no\.|nos\.|issue)\s*([^,]+?)(?:,\s*special supplement)?$/i);
    if (issueMatch) {
      result.issue = issueMatch[1].trim();
      beforeYear = beforeYear.slice(0, issueMatch.index).trim();
    } else {
      beforeYear = beforeYear.replace(/,\s*special supplement$/i, '').trim();
    }
    const volumeMatch = beforeYear.match(/^(.*\D)\s+(\d+(?:\.\d+)?)$/);
    if (volumeMatch) {
      beforeYear = volumeMatch[1].trim();
      result.volume = volumeMatch[2];
    }
    result.journal = beforeYear.replace(/^in\s+/i, '').trim();
    return result;
  }

  function bookMetadata(row) {
    const result = { place: '', publisher: '' };
    const citation = String(row.citation || '');
    const year = String(row.year || '').replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    if (!year) return result;
    const publication = citation.match(new RegExp(`\\(([^:()]+):\\s*([^()]+?),\\s*${year}\\)`));
    if (publication) {
      result.place = publication[1].trim();
      result.publisher = publication[2].trim();
    }
    return result;
  }

  function contextObject(row) {
    const params = new URLSearchParams();
    const type = String(row.type || '').toLowerCase();
    const authorList = creators(row);
    const firstAuthor = authorList[0];
    const doi = doiFor(row);
    const url = urlFor(row);
    const isbn = explicitISBN(row);
    const isBook = type === 'book' || type === 'manual' || type.includes('encyclopedia');
    const isConference = type.includes('conference');

    params.set('url_ver', 'Z39.88-2004');
    params.set('ctx_ver', 'Z39.88-2004');
    params.set('rfr_id', SOURCE_ID);

    if (isBook || isConference) {
      params.set('rft_val_fmt', 'info:ofi/fmt:kev:mtx:book');
      if (isConference) {
        params.set('rft.genre', 'bookitem');
        params.set('rft.atitle', row.title || '');
        const proceedings = citationAfterTitle(row).match(/^in\s+(.+?)(?:,\s*vol\.|\s*\()/i);
        if (proceedings) params.set('rft.btitle', proceedings[1].trim());
      } else if (type.includes('encyclopedia')) {
        params.set('rft.genre', 'bookitem');
        params.set('rft.atitle', row.title || '');
      } else {
        params.set('rft.genre', 'book');
        params.set('rft.btitle', row.title || '');
      }
      const book = bookMetadata(row);
      if (book.place) params.set('rft.place', book.place);
      if (book.publisher) params.set('rft.pub', book.publisher);
      if (isbn) params.set('rft.isbn', isbn);
    } else {
      params.set('rft_val_fmt', 'info:ofi/fmt:kev:mtx:journal');
      params.set('rft.genre', 'article');
      params.set('rft.atitle', row.title || '');
      const journal = journalMetadata(row);
      if (journal.journal) params.set('rft.jtitle', journal.journal);
      if (journal.volume) params.set('rft.volume', journal.volume);
      if (journal.issue) params.set('rft.issue', journal.issue);
      if (journal.spage) params.set('rft.spage', journal.spage);
      if (journal.epage) params.set('rft.epage', journal.epage);
      if (journal.pages) params.set('rft.pages', journal.pages);
    }

    if (row.year) params.set('rft.date', row.year);
    if (row.language) params.set('rft.language', row.language);
    authorList.forEach(author => params.append('rft.au', creatorDisplay(author)));
    if (firstAuthor && !firstAuthor.literal) {
      if (firstAuthor.family) params.set('rft.aulast', firstAuthor.family);
      if (firstAuthor.given) params.set('rft.aufirst', firstAuthor.given);
    }
    if (doi) params.append('rft_id', `info:doi/${doi}`);
    if (url) params.append('rft_id', url);
    return params.toString();
  }

  function addCOinS(article) {
    if (!(article instanceof HTMLElement) || article.querySelector(':scope > .Z3988')) return false;
    const row = state?.rows?.find(record => record.id === article.id);
    if (!row) return false;
    const authorList = creators(row);
    const doi = doiFor(row);
    const isbn = explicitISBN(row);
    const span = document.createElement('span');
    span.className = 'Z3988 zotero-coins';
    span.title = contextObject(row);
    span.hidden = true;
    span.setAttribute('aria-hidden', 'true');
    span.dataset.bibId = row.id;
    span.dataset.zoteroTitle = row.title || '';
    span.dataset.zoteroYear = row.year || '';
    span.dataset.zoteroAuthors = String(authorList.length);
    if (doi) span.dataset.zoteroDoi = doi;
    if (isbn) span.dataset.zoteroIsbn = isbn;
    article.appendChild(span);
    return true;
  }

  function refineEntry(article) {
    if (!(article instanceof HTMLElement) || article.dataset.refined === 'true') return;
    article.dataset.refined = 'true';

    const note = article.querySelector('.bib-note');
    if (note && note.textContent.trim()) {
      const details = document.createElement('details');
      details.className = 'bib-entry-note';
      const summary = document.createElement('summary');
      summary.textContent = 'Why it matters';
      note.replaceWith(details);
      details.append(summary, note);
    }

    const meta = article.querySelector('.bib-meta');
    if (meta) {
      const spans = [...meta.querySelectorAll(':scope > span')];
      if (spans.length > 2) {
        const details = document.createElement('details');
        details.className = 'bib-entry-themes';
        const summary = document.createElement('summary');
        summary.textContent = `Themes ${spans.length - 2}`;
        const wrap = document.createElement('span');
        wrap.className = 'bib-theme-list';
        spans.slice(2).forEach(span => wrap.appendChild(span));
        details.append(summary, wrap);
        meta.appendChild(details);
      }
    }
  }

  function refinePage() {
    if (document.body.dataset.bibRefined === 'true') return;
    document.body.dataset.bibRefined = 'true';

    const style = document.createElement('style');
    style.id = 'bib-refined-style';
    style.textContent = `
      body.bib-page{background:linear-gradient(180deg,#1b1512 0,#211915 38rem,#1d1714 100%)}
      .page-intro{grid-template-columns:150px minmax(0,1fr);gap:clamp(30px,6vw,88px);padding:72px 0 48px}.page-intro::after{width:110px}.page-intro h1{max-width:840px;font-size:clamp(3rem,6.2vw,5.8rem);line-height:.91}.page-intro .page-dek{max-width:680px;color:rgba(245,239,232,.72);font-size:1.04rem}
      .bib-scope{display:block;padding:22px 0 28px}.bib-scope>details{max-width:900px}.bib-scope summary,.bib-export summary{list-style:none;cursor:pointer;display:flex;align-items:baseline;justify-content:space-between;gap:20px;padding:10px 0;color:var(--bib-ink);font-family:Arial,Helvetica,sans-serif;font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}.bib-scope summary::-webkit-details-marker,.bib-export summary::-webkit-details-marker{display:none}.bib-scope summary::after,.bib-export summary::after{content:'+';color:var(--bib-accent);font-size:1rem;font-weight:400}.bib-scope details[open]>summary::after,.bib-export details[open]>summary::after{content:'−'}.bib-disclosure-sub{color:var(--bib-muted);font-weight:400;letter-spacing:.02em;text-transform:none}.bib-disclosure-body{padding:4px 0 16px}.bib-disclosure-body>p{max-width:790px;margin:12px 0;color:rgba(245,239,232,.68);font-size:.89rem}.bib-disclosure-body .bib-caution{padding:0;border:0;background:transparent;color:rgba(245,239,232,.55)!important;font-size:.69rem}
      .scope-stats{display:flex;flex-wrap:wrap;gap:8px 24px;margin:18px 0 0;border:0}.scope-stats>*{display:inline;min-height:0;padding:0;border:0;color:var(--bib-muted);font-size:.62rem}.scope-stats strong{display:inline;margin-right:4px;font-family:Arial,Helvetica,sans-serif;font-size:.72rem;font-weight:700;color:var(--bib-ink)}.scope-stats a{color:var(--bib-accent)}
      .bib-controls{grid-template-columns:minmax(240px,1.8fr) minmax(150px,.8fr) minmax(170px,1fr) auto;gap:22px;margin-top:30px;padding:0 0 13px;border:0;border-bottom:1px solid var(--bib-line-strong);background:transparent}.bib-controls label{padding:0;background:transparent}.bib-controls input,.bib-controls select{padding:4px 0 7px;border-bottom:1px solid rgba(245,239,232,.22);font-size:.76rem}.bib-controls button{align-self:end;min-width:0;min-height:31px;padding:0 2px;border:0;border-bottom:1px solid rgba(212,161,116,.42);background:transparent}.bib-controls button:hover{background:transparent;color:var(--bib-ink)}
      .bib-result-line{padding:11px 0 0;border:0;font-size:.6rem}.bib-result-line p:nth-child(n+2){display:none}
      .bib-export{display:block;padding:8px 0 20px;border-bottom:1px solid var(--bib-line-strong)}.bib-export>div:first-child{display:none}.bib-export-copy>p:first-child{display:none}.bib-export-toolbar{grid-template-columns:minmax(180px,.55fr) 2fr;gap:22px;border:0;background:transparent}.bib-export-toolbar label{padding:0;background:transparent}.bib-export-toolbar select{padding:5px 0 8px;border-bottom:1px solid rgba(245,239,232,.22)}.bib-export-buttons{display:flex;flex-wrap:wrap;gap:5px 18px;background:transparent}.bib-export-buttons button{min-height:32px;padding:0;border:0;border-bottom:1px solid rgba(212,161,116,.4);background:transparent;color:var(--bib-ink)}.bib-export-buttons button:hover{background:transparent;color:var(--bib-accent)}.bib-export-note{max-width:760px;margin-top:12px!important;font-size:.62rem}.bib-export-status{font-size:.59rem}
      .bib-section{padding:54px 0 62px}.bib-section-head{grid-template-columns:150px minmax(0,1fr);gap:clamp(30px,6vw,88px);margin-bottom:24px}.bib-section-head h2{font-size:clamp(1.9rem,3.7vw,3.15rem)}.bib-section-head>div>p{max-width:650px;font-size:.84rem}.bib-list{border-top:1px solid var(--bib-line-strong)}.bib-entry{grid-template-columns:90px minmax(0,1fr);gap:32px;padding:22px 0}.bib-entry:hover{margin-inline:0;padding-inline:0;background:transparent}.bib-entry h3{max-width:850px;font-size:1.02rem;line-height:1.5}.bib-year{font-size:.66rem}.bib-meta{align-items:center;gap:5px 12px;margin-top:8px;font-size:.58rem}.bib-meta>span:nth-of-type(n+3){display:none}.bib-entry-note,.bib-entry-themes{display:inline-block;margin:7px 12px 0 0;font-family:Arial,Helvetica,sans-serif;color:var(--bib-muted);font-size:.61rem}.bib-entry-note summary,.bib-entry-themes summary{cursor:pointer;list-style:none;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px;text-decoration-color:rgba(212,161,116,.45)}.bib-entry-note summary::-webkit-details-marker,.bib-entry-themes summary::-webkit-details-marker{display:none}.bib-entry-note .bib-note{display:block;max-width:760px;margin:8px 0 3px;color:rgba(245,239,232,.62);font-family:Georgia,'Times New Roman',serif;font-size:.82rem}.bib-theme-list{display:flex;flex-wrap:wrap;gap:5px 10px;max-width:760px;margin-top:7px;color:rgba(245,239,232,.55)}.bib-links{margin-top:9px;font-size:.62rem}
      .bib-method,.bib-data{display:none!important}.subpage-footer{border-top:1px solid var(--bib-line);padding-top:24px}
      @media(max-width:900px){.page-intro,.bib-section-head{grid-template-columns:1fr;gap:15px}.bib-controls{grid-template-columns:1fr 1fr}.bib-controls .search-field{grid-column:1/-1}.bib-export-toolbar{grid-template-columns:1fr}.bib-entry{grid-template-columns:70px minmax(0,1fr);gap:22px}}
      @media(max-width:680px){.page-intro{padding-top:52px}.page-intro h1{font-size:clamp(2.7rem,14vw,4.5rem)}.bib-controls{grid-template-columns:1fr;gap:14px}.bib-entry{grid-template-columns:1fr;gap:5px}.bib-export-buttons{gap:4px 14px}.bib-disclosure-sub{display:none}}
    `;
    document.head.appendChild(style);

    const scope = document.querySelector('.bib-scope');
    if (scope && !scope.querySelector('.bib-scope-details')) {
      const copy = scope.querySelector('.scope-copy') || scope.querySelector('div');
      const heading = copy?.querySelector('h2');
      const title = heading?.textContent?.trim() || 'Scope and method';
      if (heading) heading.remove();
      const details = document.createElement('details');
      details.className = 'bib-scope-details';
      const summary = document.createElement('summary');
      summary.innerHTML = `<span>Scope &amp; method</span><span class="bib-disclosure-sub">${title}</span>`;
      const body = document.createElement('div');
      body.className = 'bib-disclosure-body';
      if (copy) while (copy.firstChild) body.appendChild(copy.firstChild);

      const method = document.querySelector('.bib-method');
      if (method) {
        const methodCopy = method.querySelector('div');
        if (methodCopy) {
          const methodInline = document.createElement('div');
          methodInline.className = 'bib-method-inline';
          const methodHeading = methodCopy.querySelector('h2');
          if (methodHeading) {
            const h = document.createElement('p');
            h.innerHTML = `<strong>${methodHeading.textContent}</strong>`;
            methodInline.appendChild(h);
          }
          [...methodCopy.querySelectorAll('p')].forEach(p => methodInline.appendChild(p.cloneNode(true)));
          body.appendChild(methodInline);
        }
      }
      details.append(summary, body);
      scope.replaceChildren(details);
    }

    const exportSection = document.querySelector('.bib-export');
    if (exportSection && !exportSection.querySelector('.bib-export-details')) {
      const copy = exportSection.querySelector('.bib-export-copy');
      const details = document.createElement('details');
      details.className = 'bib-export-details';
      const summary = document.createElement('summary');
      summary.innerHTML = '<span>Export bibliography</span><span class="bib-disclosure-sub">CSV · TSV · JSON · CSL · BibTeX · RIS</span>';
      if (copy) details.append(summary, copy);
      else details.append(summary);
      exportSection.replaceChildren(details);
    }

    document.querySelector('.bib-data')?.remove();
    document.querySelector('.bib-method')?.remove();
  }

  function notifyZotero() {
    clearTimeout(notifyTimer);
    notifyTimer = setTimeout(() => {
      document.dispatchEvent(new Event('ZoteroItemUpdated', { bubbles: true, cancelable: true }));
    }, 120);
  }

  function process(root = document) {
    let changed = false;
    root.querySelectorAll?.('.bib-entry').forEach(article => {
      refineEntry(article);
      if (addCOinS(article)) changed = true;
    });
    if (changed) notifyZotero();
  }

  refinePage();

  const observer = new MutationObserver(mutations => {
    const shouldProcess = mutations.some(mutation =>
      [...mutation.addedNodes].some(node =>
        node.nodeType === Node.ELEMENT_NODE
        && (node.matches?.('.bib-entry') || node.querySelector?.('.bib-entry'))
      )
    );
    if (shouldProcess) process();
  });

  observer.observe(document.body, { childList: true, subtree: true });
  process();
})();
