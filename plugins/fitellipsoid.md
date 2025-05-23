
[![License GNU GPL v3.0](https://img.shields.io/pypi/l/fitellipsoid.svg?color=green)](https://github.com/pierre-weiss/fitellipsoid/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/fitellipsoid.svg?color=green)](https://pypi.org/project/fitellipsoid)
[![Python Version](https://img.shields.io/pypi/pyversions/fitellipsoid.svg?color=green)](https://python.org)
<!-- [![tests](https://github.com/pierre-weiss/fitellipsoid/workflows/tests/badge.svg)](https://github.com/pierre-weiss/fitellipsoid/actions)-->
[![codecov](https://codecov.io/gh/pierre-weiss/fitellipsoid/branch/main/graph/badge.svg)](https://codecov.io/gh/pierre-weiss/fitellipsoid)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/fitellipsoid)](https://napari-hub.org/plugins/fitellipsoid)
[![npe2](https://img.shields.io/badge/plugin-npe2-blue?link=https://napari.org/stable/plugins/index.html)](https://napari.org/stable/plugins/index.html)

A plugin to find the best ellipsoid to fit a set of points clicked by the user.
With just a few clicks (10 is the absolute minimum) around the cells/nuclei boundaries, the plugin fits an ellipsoid and returns its parameters. 
This can be used to analyze tissue geometry, mecanical stress, provide training databases for segmentation algorithms,...

![FitEllipsoid widget example](https://raw.githubusercontent.com/pierre-weiss/fitellipsoid_napari/main/images/screenshot.jpg)

----------------------------------

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/napari-plugin-template#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `fitellipsoid` via [pip]:

    conda create -n fitellipsoid-env python=3.11
    conda activate fitellispoid-env
    pip install -U 'napari[all]'
    pip install fitellipsoid
    napari

## 🧪 Usage Instructions

1. **Open your 3D image stack** in Napari.

2. **Launch the FitEllipsoid plugin** from the plugin menu.

3. **Select the point layer** created by the plugin and begin clicking along the boundary of your object:
   - 🖱️ **Left-click** to add a point  
   - 🖱️ **Right-click** to remove the last added point  

4. **Once you've added at least 10 points**, click on the **"Fit Ellipsoid"** button.

5. A **blue ellipsoid** will be fitted and displayed.  
   - ✅ If the shape fits well, you're done with that object.  
   - ❌ If it doesn't, return to the corresponding point layer and add or adjust points.

6. **Repeat** the process for all objects you'd like to segment.  
   The plugin automatically adds a new point layer after each fit.

7. When you're finished, **save the results** as a `.csv` file and optionally export a segmentation mask.



## Contributors

- **Pierre Weiss** - Project lead, core plugin development
- **Clément Cazorla** - Added the segmentation mask generation

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [GNU GPL v3.0] license,
"fitellipsoid" is free and open source software

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

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
