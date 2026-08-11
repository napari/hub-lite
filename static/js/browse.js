/**
 * Homepage browse + search.
 *
 * - Browse (no query): the pre-generated `plugins_list.html`, sorted by
 *   `last_updated` descending, injected directly so the homepage is fast.
 * - Search: Pagefind's JS API (`pagefind.search(term)`). Results are rendered
 *   by filling the `<template id="plugin-card">` markup defined in
 *   `index.html`. Pagefind does all ranking; result sorting is added in a
 *   follow-up commit.
 *
 * Pagefind is loaded lazily on the first search, so the homepage never blocks
 * on the WASM/index bundle.
 */

const SEARCH_BOX = document.getElementById("searchBox");
const RESULTS = document.getElementById("results");
const PLUGIN_COUNT = document.getElementById("pluginCount");
const PLUGIN_TEMPLATE = document.getElementById("plugin-card");

const PLUGINS_LIST_URL = "plugins_list.html";
const TIMEOUT_DURATION = 300;

let pagefind; // lazily loaded on the first search
let templateHtml = "";
let staticHtml = null; // cached contents of plugins_list.html
let searchTimeout;
let currentToken = 0;

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
      escapeHtml(
        data.plugin_types ? formatPluginTypes(data.plugin_types) : "Unknown",
      ),
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
  const search = await pf.search(term);
  if (token !== currentToken) return;

  const results = search.results ?? [];
  PLUGIN_COUNT.textContent = results.length;
  const pluginData = await Promise.all(results.map((result) => result.data()));
  if (token !== currentToken) return;

  RESULTS.innerHTML = pluginData
    .map((data) => fillTemplate({ url: data.url, ...data.meta }))
    .join("");
}

function attachListeners() {
  SEARCH_BOX.addEventListener("input", () => {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
      if (SEARCH_BOX.value.trim()) {
        runSearch(SEARCH_BOX.value);
      } else {
        loadStaticBrowse();
      }
    }, TIMEOUT_DURATION);
  });
}

async function init() {
  templateHtml = PLUGIN_TEMPLATE.innerHTML;
  attachListeners();
  await loadStaticBrowse();
}

init();
