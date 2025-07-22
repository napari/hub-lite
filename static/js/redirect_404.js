(function() {
    const path = window.location.pathname;
    const isPlugin = path.startsWith('/plugins/') && !path.endsWith('.html');

    if (isPlugin) {
      window.location.replace(path + '.html');
    }
  })();
