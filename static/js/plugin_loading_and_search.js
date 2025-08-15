document.addEventListener("DOMContentLoaded", function () {
  let currentSearchAbortController = null;

  loadPlugins();

  async function loadPlugins() {
    const searchBox = document.getElementById("searchBox");
    searchBox.disabled = true;
    const pluginContainer = document.getElementById("pluginContainer");
    pluginContainer.insertBefore(
      makeSpinner("Loading plugins..."),
      pluginContainer.firstChild,
    );
    const response = await fetch("plugins_list.html");
    const html = await response.text();
    pluginContainer.innerHTML = html;
    searchBox.disabled = false;
    updatePluginCount();
  }

  function updatePluginCount() {
    // Select all <a> tags within the pluginContainer
    const allPlugins = document
      .getElementById("pluginContainer")
      .getElementsByTagName("a");

    // Filter the list of all <a> tags to only those that are currently displayed
    const visiblePlugins = Array.from(allPlugins).filter(
      (plugin) => plugin.style.display !== "none",
    );

    // Update the displayed count with the number of visible plugins
    document.getElementById("pluginCount").textContent = visiblePlugins.length;
  }

  let searchTimeout;
  document
    .getElementById("searchBox")
    .addEventListener("input", function (event) {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => {
        handleSearch(event.target.value);
      }, 300);
    });

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

  async function handleSearch(searchText) {
    // cancel previous search
    if (currentSearchAbortController) {
      currentSearchAbortController.abort();
    }

    // create new controller for this search
    currentSearchAbortController = new AbortController();

    try {
      await streamSearchResults(
        searchText,
        currentSearchAbortController.signal,
      );
    } catch (error) {
      if (error.name !== "AbortError") {
        console.error("Search error:", error);
      }
    }
  }

  async function streamSearchResults(searchText, signal) {
    // hide all plugins initially
    const pluginContainer = document.getElementById("pluginContainer");
    for (const plugin of pluginContainer.children) {
      plugin.style.display = "none";
    }

    pluginContainer.insertBefore(
      makeSpinner("Searching plugins..."),
      pluginContainer.firstChild,
    );

    updatePluginCount();

    // fetch with abort signal so we can cancel the search
    const streaming_response = await fetch("data/search_index.ndjson", {
      signal,
    });

    // streaming response
    const reader = streaming_response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";
    let index = 1; // Start from 1 to skip the spinner

    while (true) {
      if (signal.aborted) return; // Check if aborted

      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split("\n");
      buffer = lines.pop(); // Keep incomplete line

      for (const line of lines) {
        if (signal.aborted) return; // Check during processing

        if (line.trim()) {
          try {
            const obj = JSON.parse(line);
            // TODO: use a fuzzy search library for better matching
            const match =
              !searchText.trim() ||
              JSON.stringify(obj)
                .toLowerCase()
                .includes(searchText.toLowerCase());
            if (match) {
              pluginContainer.children[index].style.display = "block";
            }
            index++;
          } catch (e) {
            console.error("Parse error:", e);
          }
          updatePluginCount();
        }
      }
    }

    // only remove spinner if this search completed (wasn't aborted)
    if (!signal.aborted) {
      pluginContainer.removeChild(pluginContainer.firstChild);
    }
  }
});
