
[![License](https://img.shields.io/pypi/l/napari-hdf5-labels-io.svg?color=green)](https://github.com/yapic/napari-hdf5-labels-io/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-hdf5-labels-io.svg?color=green)](https://pypi.org/project/napari-hdf5-labels-io)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-hdf5-labels-io.svg?color=green)](https://python.org)
[![tests](https://github.com/yapic/napari-hdf5-labels-io/workflows/tests/badge.svg)](https://github.com/yapic/napari-hdf5-labels-io/actions)
[![codecov](https://codecov.io/gh/yapic/napari-hdf5-labels-io/branch/master/graph/badge.svg)](https://codecov.io/gh/yapic/napari-hdf5-labels-io)

napari plugin to store napari projects in a .h5 file. Label layer are stored in a sparse representation (COO list).

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Description

This napari plugin provides a writer and reader to store existing layers in the current napari window, all the metadata is stored as well in a HDF5 file. All the stored preferences are included when a project file is opened.

Label layers are stored in a coordinate list sparse representation with the [Sparse module](https://sparse.pydata.org/) to keep the project file size minimum when possible (aiming to implement this in other layers in the future).

## HDF5 file architecture

The project file is a HDF5 generated with the [h5py module](https://docs.h5py.org). The file groups correspond to the different napari layer types and the layer metadata is stored as attributes of each layer.

In the case of the meta dictionary which is nested in the LayerData meta dictionary (napari IO), new keys are generated in the outer dictionary to use them as h5 dataset attributes. This nested dictionary architecture is reconstructed by the reader to ensure format compatibility.

## Installation

You can install `napari-hdf5-labels-io` via [pip]:

    pip install napari-hdf5-labels-io

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [GNU GPL v3.0] license,
"napari-hdf5-labels-io" is free and open source software.

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
[file an issue]: https://github.com/yapic/napari-hdf5-labels-io/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


