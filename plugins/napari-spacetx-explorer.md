
[![License](https://img.shields.io/pypi/l/napari-spacetx-explorer.svg?color=green)](https://github.com/sebgoti/napari-spacetx-explorer/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-spacetx-explorer.svg?color=green)](https://pypi.org/project/napari-spacetx-explorer)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-spacetx-explorer.svg?color=green)](https://python.org)
[![tests](https://github.com/sebgoti/napari-spacetx-explorer/workflows/tests/badge.svg)](https://github.com/sebgoti/napari-spacetx-explorer/actions)
[![codecov](https://codecov.io/gh/sebgoti/napari-spacetx-explorer/branch/master/graph/badge.svg)](https://codecov.io/gh/sebgoti/napari-spacetx-explorer)

A napari plugin for interactive visualization of decoded spots from spatial transcriptomic data stored as CSV

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

The plugin code was written by Sebastian Gonzalez-Tirado.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->
## Reader hookspec

`napari-spacetx-explorer` allows the user to open and visualize CSV files that
have point-data stored in a given format. The main target is for users who
want to analyze decoded spot maps from spatial omics experiments but it can
used as well for any other type of coordinate data where each point has assigned
a label (e. g. a gene) as a string and the x and y-coordinates of the point's center.
The header for these data must be 'target', 'xc', and 'yc', respectively.

![img.png](https://github.com/sebgoti/napari-spacetx-explorer/raw/main/docs/Read_Hookspec.png)

## Selecting genes

After loading the gene/target maps it is possible to select specific groups for better visualization.
This creates a new "Points" layer in napari with the selected groups displayed in different colors.

![img.png](https://github.com/sebgoti/napari-spacetx-explorer/raw/main/docs/_function_hookspec.png)

## Loading data in OME.ZARR format

The plugin napari-ome-zarr can be used to display whole-tissue images in addition to the spot maps produced with the 
`napari-spacetx-explorer` plugin.

![img.png](https://github.com/sebgoti/napari-spacetx-explorer/raw/main/docs/_ome_zarr_napari_spacetx_explorer.png)

## Installation

The easiest installation is via the "Install/Uninstall Plugins..." under the Plugins menu in napari.  
Another way is through [pip] 

    pip install napari-spacetx-explorer

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-spacetx-explorer" is free and open source software

## Issues

If you encounter any problems or would like some support, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[file an issue]: https://github.com/sebgoti/napari-spacetx-explorer/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


