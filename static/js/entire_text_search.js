document.addEventListener('DOMContentLoaded', function() {
    loadPlugins();

    async function loadPlugins() {
        const response = await fetch('plugins_list.html');
        const html = await response.text();
        document.getElementById('pluginContainer').innerHTML = html;
        updatePluginCount();
    }

    function updatePluginCount() {
        // Select all <a> tags within the pluginContainer
        const allPlugins = document.getElementById('pluginContainer').querySelectorAll('a');

        // Filter the list of all <a> tags to only those that are currently displayed
        const visiblePlugins = Array.from(allPlugins).filter(plugin => plugin.style.display !== 'none');

        // Update the displayed count with the number of visible plugins
        document.getElementById('pluginCount').textContent = visiblePlugins.length;
    }

    document.getElementById('searchBox').addEventListener('keydown', function(event) {
        if (event.key === 'Enter') { // Check if the Enter key was pressed
            searchFunction(event.target.value);
        }
    });

    async function searchFunction(searchText) {
        // Fetch the initial list to maintain the structure
        const response = await fetch('plugins_list.html');
        const html = await response.text();
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const pluginContainer = document.getElementById('pluginContainer');

        // Assuming plugins_manifest.json exists and maps plugin names to their HTML files
        const manifestResponse = await fetch('plugins_manifest.json');
        const pluginsManifest = await manifestResponse.json();

        const promises = pluginsManifest.map(async (plugin) => {
            const response = await fetch(`plugins/${plugin.html_filename}`);
            const html = await response.text();
            return { id: plugin.plugin_id, content: html.toLowerCase() }; // Removed unused property 'file'
        });

        const pluginsData = await Promise.all(promises);

        // Hide all plugins initially
        pluginContainer.innerHTML = '';

        // Now check each plugin's content for a match and only display those
        pluginsData.forEach(pluginData => {
            const pluginElement = doc.querySelector(`a[data-plugin-id="${pluginData.id}"]`);

            if (!searchText.trim()) {
                pluginContainer.appendChild(pluginElement.cloneNode(true)); // Show all plugins if search text is empty
            } else {
                // Create a RegExp for matching the whole word only, considering word boundaries
                const regex = new RegExp(`\\b${searchText.toLowerCase()}\\b`);

                // Check if plugin HTML contains the search text
                if (pluginData.content && regex.test(pluginData.content)) {
                    pluginContainer.appendChild(pluginElement.cloneNode(true));
                }
            }
        });

        updatePluginCount(); // This might need adjustment to count only visible plugins
    }
});
