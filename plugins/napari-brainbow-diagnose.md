
[![License BSD-3](https://img.shields.io/pypi/l/napari-brainbow-diagnose.svg?color=green)](https://github.com/LaboratoryOpticsBiosciences/napari-brainbow-diagnose/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-brainbow-diagnose.svg?color=green)](https://pypi.org/project/napari-brainbow-diagnose)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-brainbow-diagnose.svg?color=green)](https://python.org)
[![tests](https://github.com/LaboratoryOpticsBiosciences/napari-brainbow-diagnose/workflows/tests/badge.svg)](https://github.com/LaboratoryOpticsBiosciences/napari-brainbow-diagnose/actions)
[![codecov](https://codecov.io/gh/LaboratoryOpticsBiosciences/napari-brainbow-diagnose/branch/main/graph/badge.svg)](https://codecov.io/gh/LaboratoryOpticsBiosciences/napari-brainbow-diagnose)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-brainbow-diagnose)](https://napari-hub.org/plugins/napari-brainbow-diagnose)

Explore image in channel coordinate spaces.


**Original motivation**: Brainbow dataset have unique features that need to be addressed by specialized tools.
This plugin allows you to visualize the distribution of the channel ratio interactively in the image space and channel spaces.

You can also use this plugin along with the [`napari-cluster-plotter` plugin](https://github.com/BiAPoL/napari-clusters-plotter?tab=readme-ov-file#installation) to interact with individual objects.

![demo_gif](https://raw.githubusercontent.com/LaboratoryOpticsBiosciences/napari-brainbow-diagnose/main/docs/demo_napari-brainbow-diagnose.gif)

## Available Channel space transformation

The following channel spaces are available:

![image|width=10](https://github.com/user-attachments/assets/0dae9090-da16-4653-b466-a08289e061ea)


From Cartesian RGB:
- (a) Maxwell triangle (ternary plot) [illustration](https://en.wikipedia.org/wiki/Ternary_plot)
- (c) Hue-Saturation wheel [illustration (g)](https://en.wikipedia.org/wiki/File:Hsl-hsv_models.svg)
- (e) Spherical coordinates (Theta, Phi and Radius) [illustration](https://en.wikipedia.org/wiki/Spherical_coordinate_system)
- (g,i) Hue-Saturation-Value planes [illustration (b)(f)](https://en.wikipedia.org/wiki/File:Hsl-hsv_models.svg)

## Example Notebooks

You can use this plugin to visualize channel space of:
- interactively every voxel in the image (see [demo notebook](docs/demo.ipynb))
- interactively every object (aka center point) in the image (see [demo notebook](docs/cluster_plotter_compatibility.ipynb)). To use this notebook you need to install [`napari-cluster-plotter` plugin](https://github.com/BiAPoL/napari-clusters-plotter?tab=readme-ov-file#installation).
- Not interactive in matplotlib to export figures: (see [demo notebook](docs/plot_color_space_matplotlib.ipynb))

## Example Datasets

If you want to use your dataset, you have to format it such as each channel is in one distinct `napari.Layers`
You can open test dataset to try this plugin in `File > Open Sample > napari-brainbow-diagnose`.

- The RGB Cube is an array with shape (3x256x256x256) cube : Great to check how the plugin work when all color are represented
- ChroMS Cortex Sample is an array with shape (3x256x256x256) #Hugo : Real life brainbow image (Cortex E18 Emx1Cre) !

Once you have your layers you can use the dropdown and select the corresponding layer. It is advised to match the `red, green, blue` order so the ratio you see on the napari viewer corresponds to the Hue-Saturation Wheel of the plugin.

## Installation

You can install `napari-brainbow-diagnose` via [pip]:

    pip install napari-brainbow-diagnose

If you want to use [`napari-cluster-plotter` plugin](https://github.com/BiAPoL/napari-clusters-plotter?tab=readme-ov-file#installation)  you also need to install it manually

To install latest development version :

    pip install git+https://github.com/LaboratoryOpticsBiosciences/napari-brainbow-diagnose.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-brainbow-diagnose" is free and open source software

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

[file an issue]: https://github.com/LaboratoryOpticsBiosciences/napari-brainbow-diagnose/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->
