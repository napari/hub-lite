
[![License](https://img.shields.io/pypi/l/napari-mouse-controls.svg?color=green)](https://github.com/haesleinhuepf/napari-mouse-controls/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-mouse-controls.svg?color=green)](https://pypi.org/project/napari-mouse-controls)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-mouse-controls.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/napari-mouse-controls/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/napari-mouse-controls/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/napari-mouse-controls/branch/main/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/napari-mouse-controls)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-mouse-controls)](https://napari-hub.org/plugins/napari-mouse-controls)

Control zoom, slicing and contrast windowing with mouse and touch screen

----------------------------------

## Usage

You find the mouse control panel in the menu `Tools > Utilities > Mouse controls`

### Zoom

After clicking the Zoom button ![](https://github.com/haesleinhuepf/napari-mouse-controls/raw/main/src/napari_mouse_controls/icons/Zoom.png), you can click in the napari canvas and move the mouse up and down to zoom in and out.

![](https://github.com/haesleinhuepf/napari-mouse-controls/raw/main/docs/zoom.gif)

### Slicing

After clicking the Slicing button ![](https://github.com/haesleinhuepf/napari-mouse-controls/raw/main/src/napari_mouse_controls/icons/Slicing.png), you can control the currently displayed slice by moving the mouse.
By moving the mouse up and down, you control the currently selected Z-plane.
By moving the mouse left and right, you control the currently seleted time point.

![](https://github.com/haesleinhuepf/napari-mouse-controls/raw/main/docs/slicing.gif)

### Windowing

After clicking the Windowing button ![](https://github.com/haesleinhuepf/napari-mouse-controls/raw/main/src/napari_mouse_controls/icons/Windowing.png), you can modify the brightness and contrast by moving the mouse. 
By moving the mouse up and down, you control window width of the range of displayed grey values (max - min).
By moving the mouse left and right, you control the center of the grey value window. 

![](https://github.com/haesleinhuepf/napari-mouse-controls/raw/main/docs/windowing.gif)

### Normal / default mode

Click the Default button ![](https://github.com/haesleinhuepf/napari-mouse-controls/raw/main/src/napari_mouse_controls/icons/Default.png)
to return to napari's normal mode.


This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.


## Installation

You can install `napari-mouse-controls` via [pip]:

    pip install napari-mouse-controls

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-mouse-controls" is free and open source software

## Issues

If you encounter any problems, please create a thread on [image.sc] along with a detailed description and tag [@haesleinhuepf].

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

[file an issue]: https://github.com/haesleinhuepf/napari-mouse-controls/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[image.sc]: https://image.sc

[@haesleinhuepf]: https://twitter.com/haesleinhuepf


