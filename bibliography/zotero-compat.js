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
    return citation.slice(index + title.length)
      .replace(/^[”’"']+\s*,?\s*/, '')
      .trim();
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
      const pageParts = result.pages.split(/[–—-]/).map(v => v.trim()).filter(Boolean);
      result.spage = pageParts[0] || '';
      result.epage = pageParts[1] || '';
    }

    let issue = '';
    const issueMatch = beforeYear.match(/,\s*(?:no\.|nos\.|issue)\s*([^,]+?)(?:,\s*special supplement)?$/i);
    if (issueMatch) {
      issue = issueMatch[1].trim();
      beforeYear = beforeYear.slice(0, issueMatch.index).trim();
    } else {
      beforeYear = beforeYear.replace(/,\s*special supplement$/i, '').trim();
    }

    let volume = '';
    const volumeMatch = beforeYear.match(/^(.*\D)\s+(\d+(?:\.\d+)?)$/);
    if (volumeMatch) {
      beforeYear = volumeMatch[1].trim();
      volume = volumeMatch[2];
    }

    result.journal = beforeYear.replace(/^in\s+/i, '').trim();
    result.volume = volume;
    result.issue = issue;
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

  function notifyZotero() {
    clearTimeout(notifyTimer);
    notifyTimer = setTimeout(() => {
      document.dispatchEvent(new Event('ZoteroItemUpdated', {
        bubbles: true,
        cancelable: true
      }));
    }, 120);
  }

  function process(root = document) {
    let changed = false;
    root.querySelectorAll?.('.bib-entry').forEach(article => {
      if (addCOinS(article)) changed = true;
    });
    if (changed) notifyZotero();
  }

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
