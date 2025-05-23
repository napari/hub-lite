
[![License](https://img.shields.io/pypi/l/napari-affinities.svg?color=green)](https://github.com/pattonw/napari-affinities/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-affinities.svg?color=green)](https://pypi.org/project/napari-affinities)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-affinities.svg?color=green)](https://python.org)
[![tests](https://github.com/pattonw/napari-affinities/workflows/tests/badge.svg)](https://github.com/pattonw/napari-affinities/actions)
[![codecov](https://codecov.io/gh/pattonw/napari-affinities/branch/main/graph/badge.svg)](https://codecov.io/gh/pattonw/napari-affinities)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-affinities)](https://napari-hub.org/plugins/napari-affinities)

A plugin for creating, visualizing, and processing affinities

---

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## Installation

You will need a conda environment for everything to run
smoothly. Supported python versions are 3.7, 3.8, 3.9.

### pip
You can install `napari-affinities` via [pip]:

    `pip install napari-affinities`

To install latest development version :

    `pip install git+https://github.com/pattonw/napari-affinities.git`

Install torch according to your system [(follow the instructions here)](https://pytorch.org/get-started/locally/). For example with cuda 10.2 available, run:

    conda install pytorch torchvision cudatoolkit=10.2 -c pytorch

Install conda requirements:

    conda install -c conda-forge affogato

### conda

If you install via conda, there are fewer steps since
affogato and pytorch will be installed for you.

You can install `napari-affinities` via [conda]:

    `conda install -c conda-forge napari-affinities`

### Download example model:

#### 2D:

[epithelial example model](https://oc.embl.de/index.php/s/zfWMKu7HoQnSJLs)
Place the model zip file wherever you want. You can open it in the plugin with the "load from file" button.

#### 3D

[lightsheet example model](https://owncloud.gwdg.de/index.php/s/LsShICsOcilqPRs)
Unpack the tar file into test data (`lightsheet_nuclei_test_data` (an hdf5 file)) and model (`LightsheetNucleusSegmentation.zip` (a bioimageio model)).
Move the data into sample_data which will enable you to load the "Lightsheet Sample" data in napari.
Place the model zip file anywhere you want. You can open it in the plugin with the "load from file" button.

##### Workarounds to be fixed:

1. you need to update the `rdf.yaml` in the `LightsheetNucleusSegmentation.zip` with the following:
   - "shape" for "input0" should be updated with a larger minimum input size and "output0" should be updated with a larger halo. If not fixed, there will be significant tiling artifacts.
   - (Optional) "output0" should be renamed to affinities. The plugin supports multiple outputs and relies on names for figuring out which one is which. If unrecognized names are provided we assume the outputs are ordered (affinities, fgbg, lsds) but this is less reliable than explicit names.
2. This model also generates foreground in the same array as affinities, i.e. a 10 channel output `(fgbg, [-1, 0, 0], [0, -1, 0], [0, 0, -1], [-2, 0, 0], ...)`. Although predictions will work, post processing such as mutex watershed will break unless you manually separate the first channel.

## Use

Requirements for the model:

1. Bioimageio packaged pytorch model
2. Outputs with names "affinities", "fgbg"(optional) or "lsds"(optional)
   - if these names are not used, it will be assumed that the outputs are affinities, fgbg, then lsds in that order

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-affinities" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[mit]: http://opensource.org/licenses/MIT
[bsd-3]: http://opensource.org/licenses/BSD-3-Clause
[gnu gpl v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[gnu lgpl v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[apache software license 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[mozilla public license 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[file an issue]: https://github.com/pattonw/napari-affinities/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[pypi]: https://pypi.org/
