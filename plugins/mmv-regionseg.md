
[![License BSD-3](https://img.shields.io/pypi/l/mmv-regionseg.svg?color=green)](https://github.com/MMV-Lab/mmv-regionseg/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/mmv-regionseg.svg?color=green)](https://pypi.org/project/mmv-regionseg)
[![Python Version](https://img.shields.io/pypi/pyversions/mmv-regionseg.svg?color=green)](https://python.org)
[![tests](https://github.com/MMV-Lab/mmv-regionseg/workflows/tests/badge.svg)](https://github.com/MMV-Lab/mmv-regionseg/actions)
[![codecov](https://codecov.io/gh/MMV-Lab/mmv-regionseg/branch/main/graph/badge.svg)](https://codecov.io/gh/MMV-Lab/mmv-regionseg)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/mmv-regionseg)](https://napari-hub.org/plugins/mmv-regionseg)

A Napari plugin for the segmentation of regions by flood_fill

----------------------------------

This [napari] plugin was generated with [copier] using the [napari-plugin-template].

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/napari-plugin-template#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `mmv-regionseg` via [pip]:

    pip install mmv-regionseg



To install latest development version :

    pip install git+https://github.com/MMV-Lab/mmv-regionseg.git

## Documentation

**MMV-RegionSeg** is a Napari plugin designed to segment three-dimensional image data based on the gray value of a selected seed point. Neighboring voxels are assigned to the same class if their intensity is similar to that of the seed point or falls within a defined tolerance range.

---

### Launching the Plugin

1. Open Napari.
2. Go to the **Plugins** menu.
3. Select **MMV-RegionSeg** from the dropdown.

This opens a widget on the right-hand side of the Napari window, featuring several buttons, labels, and a slider.

### Screenshot

Here is a preview of the MMV-RegionSeg plugin in action:

![MMV-RegionSeg Plugin Screenshot](https://raw.githubusercontent.com/MMV-Lab/MMV-RegionSeg/main/docs/images/plugin_screenshot.png)

---

### Loading Image Data

Click the **"Read image"** button to load a 3D image in TIFF format. A standard OS file dialog will open. Once the image is selected, Napari will display it as an **image layer**.

---

### Adjusting Tolerance

A **slider** below the image loading button allows you to set the gray value tolerance (range: **1–50**):

- **Low tolerance**: May result in incomplete region filling.
- **High tolerance**: May include undesired regions.

> ⚠️ Choosing the right tolerance often requires trial and error.

---

### Selecting Seed Points

Click **"Select seed points"** to activate a new **points layer** in Napari. You can then define seed points by clicking directly in the viewer.

- Each seed point is visualized.
- Multiple seed points added in one step are treated as a single class.
- Use Napari’s **Layer Controls** to move or delete seed points.

---

### Segmentation Options

After placing seed points, you can choose between two segmentation methods:

#### Flood

Click **"Flood"** to perform segmentation using  
`skimage.segmentation.flood(...)`.  
This identifies neighboring voxels within the tolerance range and saves them to a new **label layer**.

You can repeat this process for other classes by selecting new seed points. Each class will have its own label layer.

#### Growth

Click **"Growth"** to visualize the segmentation **step by step**.  
This simulates the growth of a region, similar to a cell colony expanding in a Petri dish.

---

### Resetting for New Segmentation

After a label layer is created for a class, the **points layer is removed**, allowing you to define new seed points without affecting the existing segmentation results.

---

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"mmv-regionseg" is free and open source software

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

[file an issue]: https://github.com/MMV-Lab/mmv-regionseg/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
