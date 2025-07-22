// Try to recover from 404 by normalizing plugin names
// and adding the required '.html' extension
(function() {
    const path = window.location.pathname;
    const isPlugin = path.startsWith('/plugins/');
    console.log(isPlugin, path);
    if (isPlugin) {
      // Extract plugin name (last part after last '/')
      const parts = path.split('/');
      var pluginName = parts[parts.length - 1];
      console.log(pluginName);

      if (pluginName.endsWith('.html')) {
        // Remove the '.html' extension, before reconstructing the URL
        pluginName = pluginName.slice(0, -5);
      }
      console.log(pluginName);

      const normalized = normalizeName(pluginName);
      const newPath = path.slice(0, path.lastIndexOf('/') + 1) + normalized + '.html';
      console.log(newPath)
      window.location.replace(newPath);
    }

    function normalizeName(name) {
        return name.replace(/[-_.]+/g, "-").toLowerCase();
  }

})();
