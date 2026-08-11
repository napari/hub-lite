/**
 * Homepage browse + search.
 *
 * - Browse (no query): the pre-generated `plugins_list.html`, sorted by
 *   `last_updated` descending, injected directly so the homepage is fast.
 * - Search: Pagefind's JS API (`pagefind.search(term)`). Results are rendered
 *   by filling the card markup below. (Follow-up commits add sorting and move
 *   this markup into a `<template id="plugin-card">` in `index.html`.)
 *
 * Pagefind is loaded lazily on the first search, so the homepage never blocks
 * on the WASM/index bundle.
 */

const SEARCH_BOX = document.getElementById("searchBox");
const RESULTS = document.getElementById("results");
const PLUGIN_COUNT = document.getElementById("pluginCount");

const PLUGINS_LIST_URL = "plugins_list.html";
const TIMEOUT_DURATION = 300;

// Result card markup, kept here as a string for now (a later commit moves it
// into a <template id="plugin-card"> element in index.html).
const CARD_TEMPLATE = `
<a class="searchResult py-sds-xl border-black border-t-2 last:border-b-2 hover:bg-hub-gray-100 w-full" data-testid="pluginSearchResult" href="{{url}}">
  <article class="grid gap-x-sds-xl screen-495:gap-x-12 screen-600:grid-cols-2 screen-1425:grid-cols-napari-3" data-testid="searchResult">
    <div class="col-span-2 screen-495:col-span-1 screen-1425:col-span-2 flex flex-col justify-between">
      <div>
        <h3 class="font-bold text-lg" data-testid="searchResultDisplayName">{{display_name}}</h3>
        <span class="mt-sds-m screen-495:mt-3 text-[0.6875rem]" data-testid="searchResultName">{{name}}</span>
        <p class="mt-3" data-testid="searchResultSummary">{{summary}}</p>
      </div>
      <div class="mt-3 text-xs">{{authors}}</div>
    </div>
    <ul class="mt-sds-l screen-600:m-0 space-y-1 text-sm col-span-2 screen-495:col-span-1">
      <li class="grid grid-cols-[auto,1fr]" data-label="First released" data-testid="searchResultMetadata" data-value="{{release_date}}">
        <h4 class="inline whitespace-nowrap">First released: </h4>
        <span class="ml-sds-xxs font-bold">{{release_date}}</span>
      </li>
      <li class="grid grid-cols-[auto,1fr]" data-label="Last updated" data-testid="searchResultMetadata" data-value="{{last_updated}}">
        <h4 class="inline whitespace-nowrap">Last updated: </h4>
        <span class="ml-sds-xxs font-bold">{{last_updated}}</span>
      </li>
      <li class="grid grid-cols-[auto,1fr]" data-label="Plugin type" data-testid="searchResultMetadata" data-value="{{plugin_types}}">
        <h4 class="inline whitespace-nowrap">Plugin type: </h4>
        <span class="ml-sds-xxs font-bold">{{plugin_types}}</span>
      </li>
    </ul>
    <div class="mt-sds-xl text-xs flex flex-col gap-sds-s col-span-2 screen-1425:col-span-3"></div>
  </article>
</a>
`;

let pagefind; // lazily loaded on the first search
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
  return CARD_TEMPLATE
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
  attachListeners();
  await loadStaticBrowse();
}

init();
