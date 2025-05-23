
[![License BSD-3](https://img.shields.io/pypi/l/napari-conidie.svg?color=green)](https://github.com/hereariim/napari-conidie/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-conidie.svg?color=green)](https://pypi.org/project/napari-conidie)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-conidie.svg?color=green)](https://python.org)
[![tests](https://github.com/hereariim/napari-conidie/workflows/tests/badge.svg)](https://github.com/hereariim/napari-conidie/actions)
[![codecov](https://codecov.io/gh/hereariim/napari-conidie/branch/main/graph/badge.svg)](https://codecov.io/gh/hereariim/napari-conidie)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-conidie)](https://napari-hub.org/plugins/napari-conidie)

A segmentation tool to get conidie and hyphe

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

This plugin is a use case for obtaining conidia and hyphae surface from images. This plugin is a private tool dedicated exclusively to the work of the QUASAV team.

## Installation

This private tool cannot be found in the built-in napari. The installation therefore follows two steps:

1 - Install latest development version :

    git clone https://github.com/hereariim/napari-conidie.git

## Getting started

As prerequisite, user must have installed ilastik in its computer.

Before using the plugin, you must have two data:

- The ilastik model
- The compressed file contained your images structured as followed :

```
└── Compressed file
    ├── Folder1
    │   ├── img0_1.jpg
    │   ├── img0_2.jpg
    │   ...
    │   └── img0_n.jpg
    │ 
    ├── Folder2
    │   ├── img1_1.jpg
    │   ├── img1_2.jpg
    │   ...
    │   └── img1_n.jpg
    ...
    │
    └──  Foldern
        ├── imgn_1.jpg
        ├── imgn_2.jpg
        ...
        └── imgn_n.jpg
```

## Plugin

![here](https://github.com/hereariim/napari-conidie/assets/93375163/07cf6bc3-3d55-4ae1-94ac-8e8b33193963)

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-conidie" is free and open source software

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

[file an issue]: https://github.com/hereariim/napari-conidie/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
