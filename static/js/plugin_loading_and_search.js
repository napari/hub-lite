/**
 * Homepage plugin loading & search.
 *
 * The default "Browse plugins" section is the pre-generated `plugins_list.html`,
 * which is sorted by `last_updated` (descending) so newly released/updated
 * plugins appear at the top — restoring the pre-pagefind ordering. Searching
 * uses Pagefind's fuzzy search via its JS API, also sorted by `last_updated`
 * descending.
 *
 * See https://github.com/napari/hub-lite/issues/178.
 *
 * The sort key is registered on each plugin page via the
 * `data-pagefind-sort="last_updated"` attribute in
 * templates/each_plugin_template.html.
 */

const SEARCH_BOX = document.getElementById("searchBox");
const PLUGIN_CONTAINER = document.getElementById("pluginContainer");
const PLUGIN_COUNT = document.getElementById("pluginCount");

const TIMEOUT_DURATION = 300; // debounce, ms
const PLUGINS_LIST_URL = "plugins_list.html";
const SORT = { last_updated: "desc" };

let pagefind; // lazily loaded on the first search
let searchTimeout;
let currentSearchToken = 0;
let staticHtml = null; // cached contents of plugins_list.html

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

function makeSpinner(text) {
  const container = document.createElement("div");
  container.className = "spinner-container";
  const spinner = document.createElement("span");
  spinner.className = "spinner";
  const textNode = document.createElement("span");
  textNode.textContent = text;
  container.appendChild(spinner);
  container.appendChild(textNode);
  return container;
}

function renderResult({ url, meta }) {
  const releaseDate = meta.release_date
    ? escapeHtml(meta.release_date)
    : "Unknown";
  const lastUpdated = meta.last_updated
    ? escapeHtml(meta.last_updated)
    : "Unknown";
  const pluginTypes = meta.plugin_types
    ? escapeHtml(formatPluginTypes(meta.plugin_types))
    : "Unknown";

  return `
  <a class="searchResult py-sds-xl border-black border-t-2 last:border-b-2 hover:bg-hub-gray-100 w-full" data-testid="pluginSearchResult" href="${escapeHtml(url)}">
    <article class="grid gap-x-sds-xl screen-495:gap-x-12 screen-600:grid-cols-2 screen-1425:grid-cols-napari-3" data-testid="searchResult">
      <div class="col-span-2 screen-495:col-span-1 screen-1425:col-span-2 flex flex-col justify-between">
        <div>
          <h3 class="font-bold text-lg" data-testid="searchResultDisplayName">${escapeHtml(meta.display_name)}</h3>
          <span class="mt-sds-m screen-495:mt-3 text-[0.6875rem]" data-testid="searchResultName">${escapeHtml(meta.name)}</span>
          <p class="mt-3" data-testid="searchResultSummary">${escapeHtml(meta.summary)}</p>
        </div>
        <div class="mt-3 text-xs">
          ${escapeHtml(meta.authors)}
        </div>
      </div>
      <ul class="mt-sds-l screen-600:m-0 space-y-1 text-sm col-span-2 screen-495:col-span-1">
        <li class="grid grid-cols-[auto,1fr]" data-label="First released" data-testid="searchResultMetadata" data-value="${releaseDate}">
          <h4 class="inline whitespace-nowrap">First released<!-- -->: </h4>
          <span class="ml-sds-xxs font-bold">${releaseDate}</span>
        </li>
        <li class="grid grid-cols-[auto,1fr]" data-label="Last updated" data-testid="searchResultMetadata" data-value="${lastUpdated}">
          <h4 class="inline whitespace-nowrap">Last updated<!-- -->: </h4>
          <span class="ml-sds-xxs font-bold">${lastUpdated}</span>
        </li>
        <li class="grid grid-cols-[auto,1fr]" data-label="Plugin type" data-testid="searchResultMetadata" data-value="${pluginTypes}">
          <h4 class="inline whitespace-nowrap">Plugin type<!-- -->: </h4>
          <span class="ml-sds-xxs font-bold">${pluginTypes}</span>
        </li>
      </ul>
      <div class="mt-sds-xl text-xs flex flex-col gap-sds-s col-span-2 screen-1425:col-span-3"></div>
    </article>
  </a>`;
}

function clearSearchSpinner() {
  const searchBoxContainer = document.getElementById("searchBoxContainer");
  const existingSpinner =
    searchBoxContainer.querySelector(".spinner-container");
  if (existingSpinner) {
    searchBoxContainer.removeChild(existingSpinner);
  }
}

async function loadStaticPlugins() {
  // The default browse view is the pre-generated, updated-sorted list. It
  // comes from a single static file, so it renders instantly with no blank/
  // broken flash while Pagefind's WASM + index load lazily on first search.
  if (staticHtml === null) {
    const response = await fetch(PLUGINS_LIST_URL);
    staticHtml = await response.text();
  }
  PLUGIN_CONTAINER.innerHTML = staticHtml;
  PLUGIN_COUNT.textContent = PLUGIN_CONTAINER.querySelectorAll("a").length;
}

async function getPagefind() {
  if (!pagefind) {
    pagefind = await import("/pagefind/pagefind.js");
    await pagefind.init();
  }
  return pagefind;
}

async function runSearch(searchText) {
  const token = ++currentSearchToken;

  // No query -> restore the full updated-sorted browse list.
  if (!searchText.trim()) {
    await loadStaticPlugins();
    return;
  }

  clearSearchSpinner();
  PLUGIN_CONTAINER.innerHTML = "";
  const searchIcon = document.getElementById("searchIcon");
  const searchBoxContainer = document.getElementById("searchBoxContainer");
  searchBoxContainer.insertBefore(
    makeSpinner("Searching plugins..."),
    searchIcon,
  );

  try {
    const pf = await getPagefind();
    const search = await pf.search(searchText.trim(), { sort: SORT });
    if (token !== currentSearchToken) return;

    const results = search.results ?? [];
    PLUGIN_COUNT.textContent = results.length;

    const pluginData = await Promise.all(
      results.map((result) => result.data()),
    );
    if (token !== currentSearchToken) return;

    PLUGIN_CONTAINER.innerHTML = pluginData.map(renderResult).join("");
  } finally {
    if (token === currentSearchToken) {
      clearSearchSpinner();
    }
  }
}

function attachSearchListener() {
  SEARCH_BOX.addEventListener("input", () => {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(
      () => runSearch(SEARCH_BOX.value),
      TIMEOUT_DURATION,
    );
  });
}

async function init() {
  attachSearchListener();

  // Default browse: the pre-generated, updated-sorted plugin list. Pagefind
  // is deliberately NOT loaded here — it is fetched lazily on the first
  // search, so the homepage never blocks on the WASM/index bundle.
  await loadStaticPlugins();

  // Support deep-linking to a search via ?query=...
  const params = new URLSearchParams(window.location.search);
  const query = params.get("query") ?? "";
  if (query) {
    SEARCH_BOX.value = query;
    await runSearch(query);
  }
}

init();
