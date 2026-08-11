/**
 * Consolidated homepage search.
 *
 * - Browse (no query): the pre-generated `plugins_list.html`, sorted by
 *   `last_updated` descending, injected directly so the homepage is fast.
 * - Search: Pagefind's JS API (`pagefind.search(term, { sort? })`). Results
 *   are rendered by filling the `<template id="plugin-card">` markup defined
 *   in `index.html`. Pagefind does all ranking/sorting; this file only wires
 *   the search box, the "Sort" toggle buttons, and the card template.
 *   The buttons let you sort results by "First released" or "Last updated"
 *   (the same wording the plugin pages use), newest first (desc) or oldest
 *   first (asc): clicking an active date button flips the direction.
 *
 * Pagefind is loaded lazily on the first search, so the homepage never blocks
 * on the WASM/index bundle.
 */

const SEARCH_BOX = document.getElementById("searchBox");
const RESULTS = document.getElementById("results");
const PLUGIN_COUNT = document.getElementById("pluginCount");
const SORT_CONTROL = document.getElementById("sortControl");
const SORT_BUTTONS = Array.from(
  document.querySelectorAll("#sortControl .sort-btn"),
);
const PLUGIN_TEMPLATE = document.getElementById("plugin-card");

const PLUGINS_LIST_URL = "plugins_list.html";
const TIMEOUT_DURATION = 300;

// Sort field/direction combos mapped to Pagefind `sort` payloads.
// The "first_released" and "last_updated" keys are captured on every plugin
// page via `data-pagefind-sort` in each_plugin_template.html.
const SORT_OPTIONS = {
  "first_released:desc": { first_released: "desc" },
  "first_released:asc": { first_released: "asc" },
  "last_updated:desc": { last_updated: "desc" },
  "last_updated:asc": { last_updated: "asc" },
};

let pagefind; // lazily loaded on the first search
let templateHtml = "";
let staticHtml = null; // cached contents of plugins_list.html
let searchTimeout;
let currentToken = 0;
let sortField = "relevance"; // "relevance" | "first_released" | "last_updated"
let sortDir = "desc"; // only used when sortField is a date field

function escapeHtml(value) {
  const entities = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;",
  };
  return String(value ?? "").replace(/[&<>"']/g, (char) => entities[char]);
}

function formatPluginTypes(pluginTypes) {
  return String(pluginTypes ?? "").toLowerCase().replace(/\./g, "").trim();
}

function fillTemplate(data) {
  return templateHtml
    .replaceAll("{{display_name}}", escapeHtml(data.display_name))
    .replaceAll("{{name}}", escapeHtml(data.name))
    .replaceAll("{{summary}}", escapeHtml(data.summary))
    .replaceAll("{{authors}}", escapeHtml(data.authors))
    .replaceAll(
      "{{release_date}}",
      escapeHtml(data.release_date || "Unknown"),
    )
    .replaceAll(
      "{{last_updated}}",
      escapeHtml(data.last_updated || "Unknown"),
    )
    .replaceAll(
      "{{plugin_types}}",
      escapeHtml(data.plugin_types ? formatPluginTypes(data.plugin_types) : "Unknown"),
    )
    .replaceAll("{{url}}", escapeHtml(data.url));
}

async function loadStaticBrowse() {
  if (staticHtml === null) {
    const response = await fetch(PLUGINS_LIST_URL);
    staticHtml = await response.text();
  }
  RESULTS.innerHTML = staticHtml;
  PLUGIN_COUNT.textContent = RESULTS.querySelectorAll("a").length;
}

async function getPagefind() {
  if (!pagefind) {
    pagefind = await import("/pagefind/pagefind.js");
    await pagefind.init();
  }
  return pagefind;
}

async function runSearch(searchText) {
  const token = ++currentToken;
  const term = (searchText ?? "").trim();

  const pf = await getPagefind();
  const mode =
    sortField === "relevance" ? "relevance" : `${sortField}:${sortDir}`;
  const sort = SORT_OPTIONS[mode];
  const search = await pf.search(term, sort ? { sort } : {});
  if (token !== currentToken) return;

  const results = search.results ?? [];
  PLUGIN_COUNT.textContent = results.length;
  const pluginData = await Promise.all(results.map((result) => result.data()));
  if (token !== currentToken) return;

  RESULTS.innerHTML = pluginData
    .map((data) => fillTemplate({ url: data.url, ...data.meta }))
    .join("");
}

function updateSortUI() {
  SORT_BUTTONS.forEach((button) => {
    const field = button.dataset.sortField;
    const isActive = field === sortField;
    button.classList.toggle("active", isActive);
    const arrow = button.querySelector(".sort-arrow");
    if (arrow) {
      arrow.textContent = sortDir === "desc" ? "▾" : "▴";
      arrow.classList.toggle("visible", isActive);
    }
  });
}

function attachListeners() {
  SEARCH_BOX.addEventListener("input", () => {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
      const searching = SEARCH_BOX.value.trim().length > 0;
      SORT_CONTROL.style.display = searching ? "flex" : "none";
      if (!searching) {
        sortField = "relevance";
        sortDir = "desc";
        updateSortUI();
      }
      if (searching) {
        runSearch(SEARCH_BOX.value);
      } else {
        loadStaticBrowse();
      }
    }, TIMEOUT_DURATION);
  });

  SORT_BUTTONS.forEach((button) => {
    button.addEventListener("click", () => {
      const field = button.dataset.sortField;
      if (field === sortField) {
        if (field !== "relevance") {
          // Re-clicking an active date button flips asc/desc.
          sortDir = sortDir === "desc" ? "asc" : "desc";
        }
      } else {
        sortField = field;
        sortDir = "desc";
      }
      updateSortUI();
      if (SEARCH_BOX.value.trim()) {
        runSearch(SEARCH_BOX.value);
      }
    });
  });
}

async function init() {
  templateHtml = PLUGIN_TEMPLATE.innerHTML;
  attachListeners();
  await loadStaticBrowse();
}

init();
