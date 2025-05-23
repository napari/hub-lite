
[![License BSD-3](https://img.shields.io/pypi/l/napari-indices.svg?color=green)](https://github.com/Emmanulla0/napari-indices/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-indices.svg?color=green)](https://pypi.org/project/napari-indices)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-indices.svg?color=green)](https://python.org)
[![tests](https://github.com/Emmanulla0/napari-indices/workflows/tests/badge.svg)](https://github.com/Emmanulla0/napari-indices/actions)
[![codecov](https://codecov.io/gh/Emmanulla0/napari-indices/branch/main/graph/badge.svg)](https://codecov.io/gh/Emmanulla0/napari-indices)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-indices)](https://napari-hub.org/plugins/napari-indices)

Calculer les indices de végétation

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->
Emmanuella OKAFOR (L3 PA CMI-PSI_Université d'Angers) developed this plugin during her internship with a french team called ImHorPHen (lead by David ROUSSEAU). This plugin realises vegetation indexes computation with hyperspectral images. For the momment, there are five vegetation indexes : NDVI, TCARI, NPCI, SGI, NDGI.
## Installation

You can install `napari-indices` via [pip]:

    pip install napari-indices



To install latest development version :

    pip install git+https://github.com/Emmanulla0/napari-indices.git

## Plugin description


Using this plugin requires importing the bands of a hyperspectral image into a **tif file**, in our case, 160 bands. You must launch it by accessing the **Plugins > napari-indices> Vegetation indices** menu.

![Capture d'écran 2023-05-29 124720](https://github.com/Emmanuella0/napari-indices/assets/132358490/3b3895df-d0a7-466e-8ada-92bd4b642852)

Then select the vegetation index to be calculated and the different bands to be used, then click the **Run** button to start the calculation. This results in the images corresponding to the calculated indices.

![etape_2](https://github.com/Emmanuella0/napari-indices/assets/132358490/4875f0fc-3435-4875-ba4e-8881cb179b96)


The areas of interest to be analysed must then be defined. To do this, click the **Shapes** button on the Napari interface and choose the **add rectangle** shape from the menu that appears. Using the mouse, it is then possible to draw a rectangle on each of the two areas to be analyzed, for example a tree sheet and a green sheet of paper. 

![etape_3](https://github.com/Emmanuella0/napari-indices/assets/132358490/fc8612fe-5deb-4290-b4c3-9cac20acf1ce)


To perform the Fisher ratio calculation and display the histogram, it is necessary to go back to the **Plugins > napari-indices > ExempleQWidget** menu and click the **Click me! **. This action opens a new window displaying the best vegetation index to use, its corresponding Fisher ratio and the histogram of the two selected regions on the image of the vegetation index concerned. A video explaining the plugin is available at: https://uabox.univ-angers.fr/index.php/s/LqB0qs11n3jxZVJ.

![Histogram](https://github.com/Emmanuella0/napari-indices/assets/132358490/be176176-1972-402c-9a01-8e367347d9d8)

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-indices" is free and open source software

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

[file an issue]: https://github.com/Emmanulla0/napari-indices/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
