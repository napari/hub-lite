(function() {
    const path = window.location.pathname;
    const isPlugin = path.startsWith('/plugins/') && !path.endsWith('.html');
    if (isPlugin) {
      // Extract plugin name (last part after last '/')
      const parts = path.split('/');
      const pluginName = parts[parts.length - 1];

      const normalized = normalizeName(pluginName);
      const newPath = path.slice(0, path.lastIndexOf('/') + 1) + normalized + '.html';
      window.location.replace(newPath);
    }

    function normalizeName(name) {
        return name.replace(/[-_.]+/g, "-").toLowerCase();
  }

})();
