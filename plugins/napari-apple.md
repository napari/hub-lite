
[![License BSD-3](https://img.shields.io/pypi/l/napari-apple.svg?color=green)](https://github.com/hereariim/napari-apple/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-apple.svg?color=green)](https://pypi.org/project/napari-apple)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-apple.svg?color=green)](https://python.org)
[![tests](https://github.com/hereariim/napari-apple/workflows/tests/badge.svg)](https://github.com/hereariim/napari-apple/actions)
[![codecov](https://codecov.io/gh/hereariim/napari-apple/branch/main/graph/badge.svg)](https://codecov.io/gh/hereariim/napari-apple)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-apple)](https://napari-hub.org/plugins/napari-apple)

Detection of apple based on YOLOv4-tiny model

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->

## Installation

Before you can operate the module, you must install the `napari-apple` module.

### Instruction for napari-module

You can install `napari-apple` via [pip]:

    pip install napari-apple

To install latest development version :

    pip install git+https://github.com/hereariim/napari-apple.git

## How does it works

Here, user drop its images in the napari windows. The plugin shows two widgets : 
- Image detection
- Export data

In Image detection, user select the interesting layer to detect apple. The "Run" button run the inference detection based on Yolov4-tiny model. At the end, the result is displayed on screen. User can correct freely the detection by removing or adding box in image.

In Export data, user export select the interesting shape layer and RGB image. A button "Save to csv" save bounding box coordinate in Yolo way into a text file.

![Capture d'écran 2024-04-24 114340](https://github.com/hereariim/napari-apple/assets/93375163/d8873a6a-8ebb-4686-bfe9-e7e7729378b1)


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-apple" is free and open source software

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

[file an issue]: https://github.com/hereariim/napari-apple/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
