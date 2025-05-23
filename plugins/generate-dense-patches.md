
[![License BSD-3](https://img.shields.io/pypi/l/generate-dense-patches.svg?color=green)](https://github.com/volume-em/generate-dense-patches/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/generate-dense-patches.svg?color=green)](https://pypi.org/project/generate-dense-patches)
[![Python Version](https://img.shields.io/pypi/pyversions/generate-dense-patches.svg?color=green)](https://python.org)
[![tests](https://github.com/volume-em/generate-dense-patches/workflows/tests/badge.svg)](https://github.com/volume-em/generate-dense-patches/actions)
[![codecov](https://codecov.io/gh/volume-em/generate-dense-patches/branch/main/graph/badge.svg)](https://codecov.io/gh/volume-em/generate-dense-patches)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/generate-dense-patches)](https://napari-hub.org/plugins/generate-dense-patches)

A simple plugin to create a lot of training data from a 3D volume and mask. For help with this plugin please open an issue, for issues with napari specifically raise an issue here instead.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

## Installation

It's recommended to have installed napari and pyqt through conda. 

    conda install napari pyqt

Then to install this plugin via [pip]:

    pip install generate-dense-patches



To install latest development version :

    pip install git+https://github.com/volume-em/generate-dense-patches.git


## Usage
To use this plugin with napari:
1. Drag and drop an image and/or segmentation mask (tif) into the viewer.
2. Open "Plugins" Toolbar and select "Generate dense patches" and click "Generate 2D Patches"

This plugin works to create a lot of 2D training data by generating an $n^3$ cube, rotating every $\theta$ slices and saving every (step size) slice of the generated volume.

3. Make sure the "save directory box", "step size", "rotation theta", and "patch size" is filled in

If no point is placed, then the center of the image will be used as the center of the cube. If a point is placed, then the center of the cube will be the point.

4. Press run and wait for the patches to be generated.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"generate-dense-patches" is free and open source software

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

[file an issue]: https://github.com/volume-em/generate-dense-patches/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
