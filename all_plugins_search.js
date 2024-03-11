document.addEventListener('DOMContentLoaded', function() {
    loadPlugins();

    async function loadPlugins() {
        const response = await fetch('plugins_list.html');
        const html = await response.text();
        document.getElementById('pluginContainer').innerHTML = html;
        updatePluginCount();
    }

    function updatePluginCount() {
        const count = document.getElementById('pluginContainer').querySelectorAll('a').length; // Assuming each plugin is wrapped in a <a>
        document.getElementById('pluginCount').textContent = count;
    }

    document.getElementById('searchBox').addEventListener('input', function() {
        searchFunction(this.value); // Pass the current value of the search box to the search function
    });

    async function searchFunction(searchText) {
        // Load the entire list again (or you could optimize by caching it)
        const response = await fetch('plugins_list.html');
        const html = await response.text();
        document.getElementById('pluginContainer').innerHTML = html;

        if (!searchText) {
            updatePluginCount();
            return; // If the search box is empty, display all plugins
        }

        const plugins = Array.from(document.getElementById('pluginContainer').children);
        const filteredPlugins = plugins.filter(plugin => plugin.textContent.toLowerCase().includes(searchText.toLowerCase()));

        document.getElementById('pluginContainer').innerHTML = ''; // Clear the container
        filteredPlugins.forEach(plugin => {
            document.getElementById('pluginContainer').appendChild(plugin);
        });

        updatePluginCount(); // Update the count based on search
    }
});
