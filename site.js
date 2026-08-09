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

const state = {
  records: [],
  filtered: [],
  shown: PAGE_SIZE
};

function parseCSV(text) {
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;

  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    const next = text[i + 1];

    if (quoted) {
      if (ch === '"' && next === '"') {
        field += '"';
        i += 1;
      } else if (ch === '"') {
        quoted = false;
      } else {
        field += ch;
      }
      continue;
    }

    if (ch === '"') {
      quoted = true;
    } else if (ch === ',') {
      row.push(field);
      field = "";
    } else if (ch === '\n') {
      row.push(field.replace(/\r$/, ""));
      rows.push(row);
      row = [];
      field = "";
    } else {
      field += ch;
    }
  }

  if (field.length || row.length) {
    row.push(field.replace(/\r$/, ""));
    rows.push(row);
  }

  const header = rows.shift() || [];
  return rows
    .filter(values => values.some(value => value.trim() !== ""))
    .map(values => Object.fromEntries(header.map((key, index) => [key, values[index] ?? ""])));
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

function applyPresentationQC(record, qc) {
  const next = { ...record };
  const institutionMap = qc.institution_value_map || {};
  if (institutionMap[next.institution_current]) {
    next.institution_current = institutionMap[next.institution_current];
  }
  const fieldOverrides = (qc.entry_field_overrides || {})[next.entry_id];
  if (fieldOverrides) Object.assign(next, fieldOverrides);
  return next;
}

async function reconstructFrozenCatalogue() {
  const [aliasPayload, scopePayload, qcPayload, ...batchTexts] = await Promise.all([
    fetchJSON("data/survey/07AR_SUPERSEDED_ALIASES_2026-08-09.json"),
    fetchJSON("data/survey/scope_19c_overrides.json"),
    fetchJSON("data/survey/07AR_FINAL_QC_OVERRIDES_2026-08-09.json"),
    ...strictBatchPaths.map(fetchText)
  ]);

  const aliases = aliasPayload.superseded_entry_ids || {};
  const scopeOverrides = scopePayload.overrides || {};
  const seen = new Set();
  const frozen = [];

  batchTexts.forEach(text => {
    parseCSV(text).forEach(record => {
      const id = (record.entry_id || "").trim();
      if (!id || aliases[id] || seen.has(id)) return;
      seen.add(id);
      const scope = scopeOverrides[id];
      if (scope && String(scope.status || "") !== "CORE_19C") return;
      frozen.push(applyPresentationQC(record, qcPayload));
    });
  });

  if (frozen.length !== EXPECTED_FROZEN_COUNT) {
    throw new Error(`Closure contract yielded ${frozen.length} records; expected ${EXPECTED_FROZEN_COUNT}.`);
  }

  return frozen;
}

function escapeHTML(value) {
  return String(value ?? "").replace(/[&<>'"]/g, char => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    "'": "&#39;",
    '"': "&quot;"
  })[char]);
}

function safeURL(value) {
  try {
    const url = new URL(value);
    return ["http:", "https:"].includes(url.protocol) ? url.href : "";
  } catch {
    return "";
  }
}

function shortText(value, max = 112) {
  const clean = String(value || "").replace(/\s+/g, " ").trim();
  if (clean.length <= max) return clean;
  return `${clean.slice(0, max - 1).trimEnd()}…`;
}

function optionValues(field) {
  return [...new Set(state.records.map(record => (record[field] || "").trim()).filter(Boolean))]
    .sort((a, b) => a.localeCompare(b));
}

function populateSelect(id, field) {
  const select = document.getElementById(id);
  optionValues(field).forEach(value => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    select.appendChild(option);
  });
}

function buildSearchHaystack(record) {
  return [
    record.entry_id,
    record.country,
    record.institution_current,
    record.institution_historical,
    record.collection_title_or_search_entry,
    record.person_or_collection_name,
    record.relationship_phrase,
    record.date_range,
    record.subject_scope,
    record.physical_structure,
    record.event_side_hooks,
    record.notes
  ].join(" ").toLowerCase();
}

function applyFilters() {
  const query = document.getElementById("search-input").value.trim().toLowerCase();
  const country = document.getElementById("country-filter").value;
  const provenance = document.getElementById("provenance-filter").value;
  const certainty = document.getElementById("certainty-filter").value;

  state.filtered = state.records.filter(record => {
    if (country && record.country !== country) return false;
    if (provenance && record.provenance_value !== provenance) return false;
    if (certainty && record.slide_certainty !== certainty) return false;
    if (query && !buildSearchHaystack(record).includes(query)) return false;
    return true;
  });
  state.shown = PAGE_SIZE;
  renderRecords();
}

function renderRecord(record) {
  const source = safeURL(record.source_url);
  const institution = record.institution_current || record.institution_historical || "Institution unresolved";
  const title = record.collection_title_or_search_entry || record.person_or_collection_name || record.entry_id;
  const count = record.stated_count || "—";
  const person = record.person_or_collection_name || "—";
  const date = record.date_range || "—";
  const relation = record.relationship_phrase || "—";

  return `
    <article class="record-card">
      <div class="record-top">
        <span>${escapeHTML(record.country || "—")} · ${escapeHTML(record.entry_id)}</span>
        <span class="record-grade">PROV ${escapeHTML(record.provenance_value || "—")}</span>
      </div>
      <h3>${escapeHTML(institution)}</h3>
      <p class="record-title">${escapeHTML(shortText(title, 140))}</p>
      <div class="record-facts">
        <div><b>Date layer</b><span>${escapeHTML(shortText(date, 70))}</span></div>
        <div><b>Count namespace</b><span>${escapeHTML(shortText(count, 82))}</span></div>
        <div><b>Actor / collection</b><span>${escapeHTML(shortText(person, 82))}</span></div>
        <div><b>Relation</b><span>${escapeHTML(shortText(relation, 82))}</span></div>
      </div>
      ${source ? `<a class="record-source" href="${escapeHTML(source)}" target="_blank" rel="noopener">Primary / institutional source ↗</a>` : ""}
    </article>`;
}

function renderRecords() {
  const grid = document.getElementById("records-grid");
  const count = document.getElementById("result-count");
  const more = document.getElementById("load-more");
  const visible = state.filtered.slice(0, state.shown);

  count.textContent = `${state.filtered.length} of ${state.records.length} frozen nodes`;
  if (!visible.length) {
    grid.innerHTML = '<div class="empty-state">No frozen catalogue nodes match these filters.</div>';
  } else {
    grid.innerHTML = visible.map(renderRecord).join("");
  }
  more.hidden = state.shown >= state.filtered.length;
}

function setIntegrity(status, message) {
  const pill = document.getElementById("integrity-pill");
  pill.classList.remove("ok", "error");
  if (status) pill.classList.add(status);
  document.getElementById("integrity-text").textContent = message;
}

function bindControls() {
  ["search-input", "country-filter", "provenance-filter", "certainty-filter"].forEach(id => {
    document.getElementById(id).addEventListener(id === "search-input" ? "input" : "change", applyFilters);
  });

  document.getElementById("reset-filters").addEventListener("click", () => {
    document.getElementById("search-input").value = "";
    document.getElementById("country-filter").value = "";
    document.getElementById("provenance-filter").value = "";
    document.getElementById("certainty-filter").value = "";
    applyFilters();
  });

  document.getElementById("load-more").addEventListener("click", () => {
    state.shown += PAGE_SIZE;
    renderRecords();
  });
}

async function initExplorer() {
  try {
    state.records = await reconstructFrozenCatalogue();
    state.filtered = [...state.records];
    populateSelect("country-filter", "country");
    populateSelect("provenance-filter", "provenance_value");
    populateSelect("certainty-filter", "slide_certainty");
    bindControls();
    renderRecords();
    const countries = new Set(state.records.map(record => record.country).filter(Boolean)).size;
    setIntegrity("ok", `Closure verified · 155 nodes · ${countries} countries`);
  } catch (error) {
    console.error(error);
    setIntegrity("error", "Catalogue integrity check failed");
    document.getElementById("result-count").textContent = "Frozen catalogue unavailable";
    document.getElementById("records-grid").innerHTML = `
      <div class="empty-state">
        The browser could not reconstruct the 155-node closure contract.<br />
        <code>${escapeHTML(error.message)}</code>
      </div>`;
  }
}

document.addEventListener("DOMContentLoaded", initExplorer);
