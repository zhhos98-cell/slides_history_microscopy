(() => {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const root = document.documentElement;
  const body = document.body;
  const seen = new WeakSet();
  const tracked = new Set();

  body.classList.add('motion-enhanced');

  const selectors = [
    '.project-item h3',
    '.project-item p:last-child',
    '.case-visual > div',
    '.case-grid article',
    '.record-card',
    '.data-ledger a',
    '.page-intro > *',
    '.bib-scope > *',
    '.bib-export > *',
    '.bib-section-head > *',
    '.bib-entry',
    '.bib-method > *',
    '.bib-data > *',
    '.source-intro > *',
    '.source-principle > *',
    '.source-key span',
    '.corpus-strip > *',
    '.source-record'
  ].join(',');

  let observer = null;
  if (!reduced && 'IntersectionObserver' in window) {
    observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('motion-visible');
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -7% 0px' });
  }

  function register(scope = document) {
    scope.querySelectorAll?.(selectors).forEach((element, index) => {
      if (seen.has(element)) return;
      seen.add(element);
      tracked.add(element);
      element.classList.add('motion-piece');
      element.style.setProperty('--motion-delay', `${Math.min((index % 5) * 52, 208)}ms`);
      if (reduced || !observer) element.classList.add('motion-visible');
      else observer.observe(element);
    });

    scope.querySelectorAll?.('.section-heading, .page-intro, .source-intro').forEach(element => {
      element.classList.add('motion-line');
      if (reduced) element.classList.add('motion-visible');
      else if (observer && !seen.has(element)) {
        seen.add(element);
        observer.observe(element);
      }
    });
  }

  function updateScrollVars() {
    const y = window.scrollY || 0;
    const max = Math.max(document.documentElement.scrollHeight - window.innerHeight, 1);
    root.style.setProperty('--scroll-y', y.toFixed(1));
    root.style.setProperty('--scroll-progress', (y / max).toFixed(4));
  }

  let ticking = false;
  function requestScrollUpdate() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      updateScrollVars();
      ticking = false;
    });
  }

  function updatePointer(event) {
    if (reduced) return;
    const x = event.clientX / Math.max(window.innerWidth, 1) - 0.5;
    const y = event.clientY / Math.max(window.innerHeight, 1) - 0.5;
    root.style.setProperty('--pointer-x', x.toFixed(4));
    root.style.setProperty('--pointer-y', y.toFixed(4));
  }

  register();
  updateScrollVars();

  if ('MutationObserver' in window) {
    const mutationObserver = new MutationObserver(mutations => {
      mutations.forEach(mutation => mutation.addedNodes.forEach(node => {
        if (node.nodeType !== 1) return;
        if (node.matches?.(selectors)) {
          register(node.parentElement || document);
        } else {
          register(node);
        }
      }));
    });
    mutationObserver.observe(document.body, { childList: true, subtree: true });
  }

  window.addEventListener('scroll', requestScrollUpdate, { passive: true });
  window.addEventListener('resize', requestScrollUpdate, { passive: true });
  window.addEventListener('pointermove', updatePointer, { passive: true });
})();
