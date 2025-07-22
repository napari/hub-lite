// Try to recover from 404 by normalizing plugin names
// and adding the required '.html' extension
(function() {
    const path = window.location.pathname;
    const isPlugin = path.includes('/plugins/');
    if (isPlugin) {
      // Extract plugin name (last part after last '/')
      const parts = path.split('/');
      var pluginName = parts[parts.length - 1];

      if (pluginName.endsWith('.html')) {
        // Remove the '.html' extension, before reconstructing the URL
        pluginName = pluginName.slice(0, -5);
      }

      const normalized = normalizeName(pluginName);
      const newPath = path.slice(0, path.lastIndexOf('/') + 1) + normalized + '.html';

      console.log(newPath);
      fetch(checkPath, { method: 'HEAD' })
        .then(response => {
            if (response.ok) {
            console.log("Exists!");
            window.location.replace(newPath);
            } else {
            console.log("Does not exist!");
            }
        });

    }

    function normalizeName(name) {
        return name.replace(/[-_.]+/g, "-").toLowerCase();
  }

})();
