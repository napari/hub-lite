
[![License MIT](https://img.shields.io/pypi/l/napari-hierarchical.svg?color=green)](https://github.com/BodenmillerGroup/napari-hierarchical/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-hierarchical.svg?color=green)](https://pypi.org/project/napari-hierarchical)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-hierarchical.svg?color=green)](https://python.org)
[![tests](https://github.com/BodenmillerGroup/napari-hierarchical/workflows/tests/badge.svg)](https://github.com/BodenmillerGroup/napari-hierarchical/actions)
[![codecov](https://codecov.io/gh/BodenmillerGroup/napari-hierarchical/branch/main/graph/badge.svg)](https://codecov.io/gh/BodenmillerGroup/napari-hierarchical)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-hierarchical)](https://napari-hub.org/plugins/napari-hierarchical)

Hierarchical file format support for napari

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.


## Installation

You can install `napari-hierarchical` via [pip]:

    pip install "napari-hierarchical[all]"

To install latest development version :

    pip install "git+https://github.com/BodenmillerGroup/napari-hierarchical.git#egg=napari-hierarchical[all]"

## Usage

The plugin enables the reading, editing and writing of container formats. In the plugin, *groups* represent hierarchically structured collections of *arrays*. Each group can hold zero or more arrays and can have zero or more child groups (hierarchical structure). An array is a logical representation of (image) data on disk and directly corresponds to a napari layer when loaded.

Files can be opened through napari (e.g. `File -> Open File(s)` menu, `Viewer.open(...)` function), as the plugin implements napari's file reader hook. Upon opening a hierarchically structured file, the *Groups* and *Arrays* widgets are displayed. The *Groups* widget allows to browse and restructure the groups tree, while the *Arrays* widget groups arrays from the selected groups by file format-specific metadata (e.g. channel name for MCD files). Selecting arrays also selects the corresponding napari layers, allowing to adjust their properties.

Arrays can be loaded individually by toggling their *loaded* state (circular button), which will add napari layers for the corresponding arrays. Similarly, loaded arrays can be shown or hidden by toggling their *visible* state (eye button), which will toggle the visibility of the associated napari layers. The loaded/visible states of groups (collections of arrays) can be toggled in a similar fashion. Arrays are always loaded into memory (no memory mapping), to allow for editing the tree structure. Loaded root groups can be exported to supported hierarchical file formats.

Currently, reading/writing of HDF5 and Zarr (not: OME-NGFF) files are supported out of the box, as well as reading imaging mass cytometry (IMC) data (i.e., MCD files). For these file formats, sample data is available through the plugin. Additional readers/writers can be implemented using a pluggy-based interface, similar to the first generation `napari-plugin-engine`.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.


## License

Distributed under the terms of the [MIT] license,
"napari-hierarchical" is free and open source software


## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

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

[file an issue]: https://github.com/BodenmillerGroup/napari-hierarchical/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
