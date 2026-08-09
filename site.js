const EXPECTED_FROZEN_COUNT = 155;
const PAGE_SIZE = 24;

const strictBatchPaths = [
  "07K_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07L_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07M_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07N_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07O_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07P_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07Q_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07R_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07S_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07T_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07U_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07V_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07W_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07X_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07Y_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07Z_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07AA_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07AB_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07AC_Global_Microscope_Slide_Collections_Expansion_2026-08-08.csv",
  "07AD_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AE_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AF_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AG_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AH_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AI_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AJ_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AK_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AL_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AM_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AN_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AO_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AP_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv",
  "07AQ_Global_Microscope_Slide_Collections_Expansion_2026-08-09.csv"
].map(name => `data/survey/${name}`);

const state = { records: [], filtered: [], shown: PAGE_SIZE };

function parseCSV(text) {
  const rows = [];
  let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i], next = text[i + 1];
    if (quoted) {
      if (ch === '"' && next === '"') { field += '"'; i += 1; }
      else if (ch === '"') quoted = false;
      else field += ch;
      continue;
    }
    if (ch === '"') quoted = true;
    else if (ch === ',') { row.push(field); field = ""; }
    else if (ch === '\n') { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; }
    else field += ch;
  }
  if (field.length || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  const header = rows.shift() || [];
  return rows.filter(values => values.some(value => value.trim() !== ""))
    .map(values => Object.fromEntries(header.map((key, i) => [key, values[i] ?? ""])));
}

async function fetchText(path) {
  const response = await fetch(path, { cache: "no-store" });
  if (!response.ok) throw new Error(`${path}: HTTP ${response.status}`);
  return response.text();
}

async function fetchJSON(path) {
  const response = await fetch(path, { cache: "no-store" });
  if (!response.ok) throw new Error(`${path}: HTTP ${response.status}`);
  return response.json();
}

function escapeHTML(value) {
  return String(value ?? "").replace(/[&<>'"]/g, ch => ({ "&":"&amp;", "<":"&lt;", ">":"&gt;", "'":"&#39;", '"':"&quot;" })[ch]);
}

function shortText(value, max = 112) {
  const text = String(value || "").replace(/\s+/g, " ").trim();
  return text.length <= max ? text : `${text.slice(0, max - 1).trimEnd()}…`;
}

function safeURL(value) {
  try {
    const url = new URL(value);
    return ["http:", "https:"].includes(url.protocol) ? url.href : "";
  } catch { return ""; }
}

function applyPresentationQC(record, qc) {
  const next = { ...record };
  const institutionMap = qc.institution_value_map || {};
  if (institutionMap[next.institution_current]) next.institution_current = institutionMap[next.institution_current];
  const override = (qc.entry_field_overrides || {})[next.entry_id];
  if (override) Object.assign(next, override);
  return next;
}

async function reconstructFrozenCatalogue() {
  const [aliases, scope, qc, ...texts] = await Promise.all([
    fetchJSON("data/survey/07AR_SUPERSEDED_ALIASES_2026-08-09.json"),
    fetchJSON("data/survey/scope_19c_overrides.json"),
    fetchJSON("data/survey/07AR_FINAL_QC_OVERRIDES_2026-08-09.json"),
    ...strictBatchPaths.map(fetchText)
  ]);
  const aliasMap = aliases.superseded_entry_ids || {};
  const overrides = scope.overrides || {};
  const seen = new Set();
  const out = [];
  texts.forEach(text => parseCSV(text).forEach(record => {
    const id = (record.entry_id || "").trim();
    if (!id || aliasMap[id] || seen.has(id)) return;
    seen.add(id);
    if (overrides[id] && String(overrides[id].status || "") !== "CORE_19C") return;
    out.push(applyPresentationQC(record, qc));
  }));
  if (out.length !== EXPECTED_FROZEN_COUNT) throw new Error(`Closure contract yielded ${out.length}; expected ${EXPECTED_FROZEN_COUNT}.`);
  return out;
}

function optionValues(rows, field) {
  return [...new Set(rows.map(row => String(row[field] || "").trim()).filter(Boolean))].sort((a, b) => a.localeCompare(b));
}

function fillSelect(id, values) {
  const element = document.getElementById(id);
  values.forEach(value => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    element.appendChild(option);
  });
}

function recordHaystack(record) {
  return [record.entry_id, record.country, record.institution_current, record.institution_historical, record.collection_title_or_search_entry, record.person_or_collection_name, record.relationship_phrase, record.date_range, record.subject_scope, record.physical_structure, record.event_side_hooks, record.notes].join(" ").toLowerCase();
}

function renderCard(record) {
  const source = safeURL(record.source_url);
  const institution = record.institution_current || record.institution_historical || "Institution unresolved";
  const title = record.collection_title_or_search_entry || record.person_or_collection_name || record.entry_id;
  return `<article class="record-card">
    <div class="record-top"><span>${escapeHTML(record.country || "—")} · ${escapeHTML(record.entry_id)}</span><span class="record-grade">PROV ${escapeHTML(record.provenance_value || "—")}</span></div>
    <h3>${escapeHTML(institution)}</h3>
    <p class="record-title">${escapeHTML(shortText(title, 140))}</p>
    <div class="record-facts">
      <div><b>Date layer</b><span>${escapeHTML(shortText(record.date_range || "—", 70))}</span></div>
      <div><b>Count namespace</b><span>${escapeHTML(shortText(record.stated_count || "—", 82))}</span></div>
      <div><b>Actor / collection</b><span>${escapeHTML(shortText(record.person_or_collection_name || "—", 82))}</span></div>
      <div><b>Relation</b><span>${escapeHTML(shortText(record.relationship_phrase || "—", 82))}</span></div>
    </div>
    ${source ? `<a class="record-source" href="${escapeHTML(source)}" target="_blank" rel="noopener">Primary / institutional source ↗</a>` : ""}
  </article>`;
}

function renderRecords() {
  const grid = document.getElementById("records-grid");
  const visible = state.filtered.slice(0, state.shown);
  document.getElementById("result-count").textContent = `${state.filtered.length} of ${state.records.length} frozen records`;
  grid.innerHTML = visible.length ? visible.map(renderCard).join("") : '<div class="empty-state">No frozen catalogue records match these filters.</div>';
  document.getElementById("load-more").hidden = state.shown >= state.filtered.length;
}

function applyFilters() {
  const query = document.getElementById("search-input").value.trim().toLowerCase();
  const country = document.getElementById("country-filter").value;
  const provenance = document.getElementById("provenance-filter").value;
  const certainty = document.getElementById("certainty-filter").value;
  state.filtered = state.records.filter(record =>
    (!country || record.country === country) &&
    (!provenance || record.provenance_value === provenance) &&
    (!certainty || record.slide_certainty === certainty) &&
    (!query || recordHaystack(record).includes(query))
  );
  state.shown = PAGE_SIZE;
  renderRecords();
}

function setIntegrity(status, message) {
  const pill = document.getElementById("integrity-pill");
  pill.classList.remove("ok", "error");
  if (status) pill.classList.add(status);
  document.getElementById("integrity-text").textContent = message;
}

async function initCatalogue() {
  try {
    state.records = await reconstructFrozenCatalogue();
    state.filtered = [...state.records];
    fillSelect("country-filter", optionValues(state.records, "country"));
    fillSelect("provenance-filter", optionValues(state.records, "provenance_value"));
    fillSelect("certainty-filter", optionValues(state.records, "slide_certainty"));
    ["search-input", "country-filter", "provenance-filter", "certainty-filter"].forEach(id => {
      const element = document.getElementById(id);
      element.addEventListener(id === "search-input" ? "input" : "change", applyFilters);
    });
    document.getElementById("reset-filters").addEventListener("click", () => {
      ["search-input", "country-filter", "provenance-filter", "certainty-filter"].forEach(id => document.getElementById(id).value = "");
      applyFilters();
    });
    document.getElementById("load-more").addEventListener("click", () => { state.shown += PAGE_SIZE; renderRecords(); });
    renderRecords();
    setIntegrity("ok", `Closure verified · 155 records · ${new Set(state.records.map(record => record.country).filter(Boolean)).size} countries`);
  } catch (error) {
    console.error(error);
    setIntegrity("error", "Catalogue integrity check failed");
    document.getElementById("records-grid").innerHTML = `<div class="empty-state">Frozen catalogue unavailable.<br>${escapeHTML(error.message)}</div>`;
  }
}

function initMotion() {
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduced) {
    document.body.classList.add("motion-ready");
    requestAnimationFrame(() => document.body.classList.add("hero-in"));
  }
  const revealTargets = document.querySelectorAll(".section-heading, .project-lede, .research-chain, .evidence-key, .project-item, .cases-intro, .sample-main > *, .case-index-head, .case-grid article, .catalogue-lede, .filters, .records-grid, .sources-grid article, .data-lede, .data-ledger a");
  revealTargets.forEach((element, index) => {
    element.classList.add("reveal");
    element.style.setProperty("--reveal-delay", `${Math.min((index % 4) * 45, 135)}ms`);
  });
  if (reduced) { revealTargets.forEach(element => element.classList.add("is-visible")); return; }
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) { entry.target.classList.add("is-visible"); observer.unobserve(entry.target); }
  }), { threshold: .08, rootMargin: "0px 0px -8% 0px" });
  revealTargets.forEach(element => observer.observe(element));
}

function updateScrollUI() {
  document.body.classList.toggle("nav-scrolled", window.scrollY > 36);
  const timeline = document.querySelector(".timeline");
  const sample = document.querySelector("#case-naples");
  const meter = sample?.querySelector(".case-meter span");
  if (timeline) {
    const rect = timeline.getBoundingClientRect();
    const viewport = window.innerHeight;
    const progress = Math.max(0, Math.min(1, (viewport * .72 - rect.top) / Math.max(rect.height, 1)));
    timeline.style.setProperty("--timeline-progress", `${progress * 100}%`);
    timeline.querySelectorAll(".event").forEach(event => {
      const eRect = event.getBoundingClientRect();
      event.classList.toggle("is-visible", eRect.top < viewport * .72);
    });
    if (meter) meter.style.setProperty("--case-progress", `${progress * 100}%`);
  }
  const sections = [...document.querySelectorAll("#project, #cases, #catalogue, #sources, #data")];
  let active = "";
  sections.forEach(section => { if (section.getBoundingClientRect().top <= 130) active = section.id; });
  document.querySelectorAll(".top-nav a[href^='#']").forEach(link => link.classList.toggle("is-active", link.getAttribute("href") === `#${active}`));
}

window.addEventListener("scroll", updateScrollUI, { passive: true });
window.addEventListener("resize", updateScrollUI);
document.addEventListener("DOMContentLoaded", () => {
  initMotion();
  updateScrollUI();
  initCatalogue();
});
