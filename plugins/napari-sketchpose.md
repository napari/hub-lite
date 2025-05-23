
[![License GNU GPL v3.0](https://img.shields.io/pypi/l/napari-sketchpose.svg?color=green)](https://github.com/koopa31/napari-sketchpose/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-sketchpose.svg?color=green)](https://pypi.org/project/napari-sketchpose)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-sketchpose.svg?color=green)](https://python.org)
[![tests](https://github.com/koopa31/napari-sketchpose/workflows/tests/badge.svg)](https://github.com/koopa31/napari-sketchpose/actions)
[![codecov](https://codecov.io/gh/koopa31/napari-sketchpose/branch/main/graph/badge.svg)](https://codecov.io/gh/koopa31/napari-sketchpose)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-sketchpose)](https://napari-hub.org/plugins/napari-sketchpose)

A plugin to adapt the Omnipose implementation to frugal labeling. It aims to facilitate the training from scratch or the 
use of transfer learning with little data, by not needing to draw entire cells, but a few squiggles instead (see GIF below).


If you use this plugin please cite the [paper](https://hal.science/hal-04330824): 

Clément Cazorla, Nathanaël Munier, Renaud Morin, Pierre Weiss. Sketchpose: Learning to Segment
Cells with Partial Annotations. 2023. ffhal-04330824f

```bibtex
@unpublished{cazorla:hal-04330824,
      TITLE = {{Sketchpose: Learning to Segment Cells with Partial Annotations}},
      AUTHOR = {Cazorla, Cl{\'e}ment and Munier, Nathana{\"e}l and Morin, Renaud and Weiss, Pierre},
      URL = {https://hal.science/hal-04330824},
      NOTE = {working paper or preprint},
      YEAR = {2023},
      MONTH = Dec,
      KEYWORDS = {Cellpose -Segmentation -Frugal learning -Napari -Deep learning -Distance map},
      PDF = {https://hal.science/hal-04330824/file/sketchpose_hal.pdf},
      HAL_ID = {hal-04330824},
      HAL_VERSION = {v1},
    }

```


![](https://bitbucket.org/koopa31/napari-sketchpose/raw/b691817e9e20a3c1c2bc69277579f6fb9b26354e/images/frugalpose.gif)
Image Credit: Eduard Muzhevskyi
----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation



First, we advise you to create a conda environment in Python 3.10, in which you will run Napari:

    conda create -n sketchpose_env python=3.10
    conda activate sketchpose_env
    conda install pip
    python -m pip install "napari[all]" --upgrade

You can install `napari_sketchpose` via [pip]:

    pip install napari_sketchpose

WARNING:

For Windows users, CUDA version of PyTorch may not be installed properly. When the plugin starts for the first time, it checks whether
CUDA version is installed. If not, it tries to install it using light-the-torch library. If this does not work, you should re-install 
CUDA torch and torchvision versions manually, otherwise the plugin will not work properly.

## Tutorial

We strongly recommend reading the [documentation] to get the most out of the plugin.
A step-by-step tutorial illustrated with GIFs will guide you through the various stages.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [GNU GPL v3.0] license,
"napari-sketchpose" is free and open source software

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

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[documentation]: https://sketchpose-doc.readthedocs.io/en/latest/
