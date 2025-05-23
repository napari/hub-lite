
[![License BSD-3](https://img.shields.io/pypi/l/napari-filter-labels-by-prop.svg?color=green)](https://github.com/loicsauteur/napari-filter-labels-by-prop/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-filter-labels-by-prop.svg?color=green)](https://pypi.org/project/napari-filter-labels-by-prop)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-filter-labels-by-prop.svg?color=green)](https://python.org)
[![tests](https://github.com/loicsauteur/napari-filter-labels-by-prop/workflows/tests/badge.svg)](https://github.com/loicsauteur/napari-filter-labels-by-prop/actions)
[![codecov](https://codecov.io/gh/loicsauteur/napari-filter-labels-by-prop/branch/main/graph/badge.svg)](https://codecov.io/gh/loicsauteur/napari-filter-labels-by-prop)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-filter-labels-by-prop)](https://napari-hub.org/plugins/napari-filter-labels-by-prop)

A simple plugin to filter labels by properties.

----------------------------------

This [napari] plugin was generated with [copier] using the [napari-plugin-template].

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/napari-plugin-template#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->
## Description

This plugin provides the possibility to filter segmentation objects by measurements
(shape and intensity). E.g. you segmented your cells, and you want to exclude segmentation objects
that have a mean intensity below a certain value.

It is intended for 2D and 3D images.

You can interactively set minimum and maximum thresholds on measurement properties, and
napari will show a preview of the selection.

Measurements are based on `scikit-image regionprops`. However, not all properties are
implemented, and they are more restricted for 3D images.

## Usage: Quick start

![](https://github.com/loicsauteur/napari-filter-labels-by-prop/raw/main/resources/preview_filter_labels.gif)

1. Start napari
2. Start the plugin from the menu: `Plugins > Filter labels by properties`
3. Add a label image
4. (optionally) Add a corresponding intensity image with the same (Z)YX shape
5. In the widget, select the property you want to filter on
6. Adjust the min/max sliders
7. When you are ready to create a new label layer click the `Create labels` button in the widget

### Usage notes:

When dealing with more than 100 label objects in an image, the filtering view update is
triggered only once you release the sliders.

Another similar plugin you could consider checking out:
[napari-skimage-regionprops](https://www.napari-hub.org/plugins/napari-skimage-regionprops).

Pixel/Voxel size are read from the napari layer scale attribute (defaults to 1 if not specified when adding the layer).
You can manually enter the size and press the `Set` button, which will set the layer scale,
and measure the shape properties with calibrated units

The "Measure projected shape properties" option is only available for 3D images.
It measures additional properties of Z-projected labels (including: "area", "convex_area", "circularity" and "perimeter").

The "Measure cytoplasm and cell compartments" is intended for label images that represent nuclei.
With this option selected, cytoplasm and cell masks will be created by a dilation of 5 units (pixels or calibrated).
Measurement in those compartments will be made and be used to filter on.
`Create labels` will also add the respective cytoplasm and cell mask layers to the napari viewer.

<!--
         ## TODO: add feature measurement also to layer.features?
-->
## Installation

You can install `napari-filter-labels-by-prop` via [pip]:

    pip install napari-filter-labels-by-prop


To install latest development version :

    pip install git+https://github.com/loicsauteur/napari-filter-labels-by-prop.git

<!--
Install Test dependencies
    `pip install -e ".[testing]"`
-->

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-filter-labels-by-prop" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[copier]: https://copier.readthedocs.io/en/stable/
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[napari-plugin-template]: https://github.com/napari/napari-plugin-template

[file an issue]: https://github.com/loicsauteur/napari-filter-labels-by-prop/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
