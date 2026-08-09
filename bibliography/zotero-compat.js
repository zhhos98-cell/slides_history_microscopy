(() => {
  const SOURCE_ID = 'info:sid/zhhos98-cell.github.io:slides_history_microscopy';
  let notifyTimer = null;

  function creatorNames(row) {
    try {
      return parseCreators(row.authors)
        .filter(creator => creator.role === 'author')
        .map(creator => creator.literal || [creator.given, creator.family].filter(Boolean).join(' '))
        .filter(Boolean);
    } catch {
      return String(row.authors || '')
        .replace(/;\s*ed\.\s+.*$/i, '')
        .split(/\s+and\s+|,\s+and\s+|;\s*/)
        .map(value => value.trim())
        .filter(Boolean);
    }
  }

  function contextObject(row) {
    const params = new URLSearchParams();
    const type = String(row.type || '').toLowerCase();
    const isBook = type === 'book' || type === 'manual' || type.includes('encyclopedia');

    params.set('ctx_ver', 'Z39.88-2004');
    params.set('rfr_id', SOURCE_ID);
    params.set('rft_val_fmt', isBook
      ? 'info:ofi/fmt:kev:mtx:book'
      : 'info:ofi/fmt:kev:mtx:journal');

    if (isBook) {
      params.set('rft.genre', type.includes('encyclopedia') ? 'bookitem' : 'book');
      if (type.includes('encyclopedia')) params.set('rft.atitle', row.title || '');
      else params.set('rft.btitle', row.title || '');
    } else {
      params.set('rft.genre', 'article');
      params.set('rft.atitle', row.title || '');
    }

    if (row.year) params.set('rft.date', row.year);
    if (row.language) params.set('rft.language', row.language);
    creatorNames(row).forEach(name => params.append('rft.au', name));

    try {
      const doi = extractDOI(row);
      if (doi) params.append('rft_id', `info:doi/${doi}`);
    } catch {}

    try {
      const url = firstURL(row);
      if (url) params.append('rft_id', url);
    } catch {}

    return params.toString();
  }

  function addCOinS(article) {
    if (!(article instanceof HTMLElement) || article.querySelector(':scope > .Z3988')) return false;
    const row = state?.rows?.find(record => record.id === article.id);
    if (!row) return false;

    const span = document.createElement('span');
    span.className = 'Z3988 zotero-coins';
    span.title = contextObject(row);
    span.hidden = true;
    span.setAttribute('aria-hidden', 'true');
    article.appendChild(span);
    return true;
  }

  function notifyZotero() {
    clearTimeout(notifyTimer);
    notifyTimer = setTimeout(() => {
      document.dispatchEvent(new Event('ZoteroItemUpdated', {
        bubbles: true,
        cancelable: true
      }));
    }, 60);
  }

  function process(root = document) {
    let changed = false;
    root.querySelectorAll?.('.bib-entry').forEach(article => {
      if (addCOinS(article)) changed = true;
    });
    if (changed) notifyZotero();
  }

  const observer = new MutationObserver(mutations => {
    let shouldProcess = false;
    for (const mutation of mutations) {
      if ([...mutation.addedNodes].some(node => node.nodeType === Node.ELEMENT_NODE)) {
        shouldProcess = true;
        break;
      }
    }
    if (shouldProcess) process();
  });

  observer.observe(document.body, { childList: true, subtree: true });
  process();
})();
