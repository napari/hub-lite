/**
 * Sorted static browse + Pagefind component search.
 *
 * The default "Browse plugins" view is the pre-generated `plugins_list.html`,
 * sorted by `last_updated` (descending). Searching uses the Pagefind component
 * UI (`<pagefind-input>` + `<pagefind-results>`) with native relevance
 * ranking. `faceted` without `preload` keeps the component results empty and
 * defers loading Pagefind's WASM + index until the first search, so the
 * homepage renders instantly from the static list.
 */

const PLUGIN_COUNT = document.getElementById("pluginCount");
const STATIC_BROWSE = document.getElementById("staticBrowse");
const PF_RESULTS = document.getElementById("pfResults");

let staticCount = 0;

async function loadStaticBrowse() {
  const response = await fetch("plugins_list.html");
  STATIC_BROWSE.innerHTML = await response.text();
  staticCount = STATIC_BROWSE.querySelectorAll("a").length;
  PLUGIN_COUNT.textContent = staticCount;
}

function setMode(searching) {
  STATIC_BROWSE.style.display = searching ? "none" : "block";
  PF_RESULTS.style.display = searching ? "block" : "none";
  if (!searching) {
    PLUGIN_COUNT.textContent = staticCount;
  }
}

async function waitForInstance() {
  while (
    !window.PagefindComponents?.getInstanceManager?.()?.getInstance?.("default")
  ) {
    await new Promise((resolve) => setTimeout(resolve, 50));
  }
  return window.PagefindComponents.getInstanceManager().getInstance("default");
}

async function init() {
  await loadStaticBrowse();
  setMode(false);

  let searching = false;
  const instance = await waitForInstance();
  instance.on("search", (term) => {
    searching = (term ?? "").trim().length > 0;
    setMode(searching);
  });
  instance.on("results", (searchResult) => {
    // Only update the count while a search is active; when idle the static
    // browse count is shown and the component may emit a hidden empty-search.
    if (searching) {
      PLUGIN_COUNT.textContent = searchResult?.results?.length ?? 0;
    }
  });
}

init();
