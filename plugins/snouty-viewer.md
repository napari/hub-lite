
[![License MIT](https://img.shields.io/pypi/l/snouty-viewer.svg?color=green)](https://github.com/aelefebv/snouty-viewer/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/snouty-viewer.svg?color=green)](https://pypi.org/project/snouty-viewer)
[![Python Version](https://img.shields.io/pypi/pyversions/snouty-viewer.svg?color=green)](https://python.org)
[![tests](https://github.com/aelefebv/snouty-viewer/workflows/tests/badge.svg)](https://github.com/aelefebv/snouty-viewer/actions/workflows/test_and_deploy.yml)
[![codecov](https://codecov.io/gh/aelefebv/snouty-viewer/branch/main/graph/badge.svg)](https://codecov.io/gh/aelefebv/snouty-viewer)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/snouty-viewer)](https://napari-hub.org/plugins/snouty-viewer)

## Description
Easy to use plugin for opening raw Snouty files and converting them to native view.

Allows for saving to ome.tif files with corresponding OME-XML based metadata.

Also allows for bulk deskewing and saving directories.

![Example](https://i.imgur.com/VirE5DM.gif)

## Intended Audience & Supported Data
This plugin is intended for those using a SOLS (Snouty) microscope collected via
[Alfred Millett-Sikking's code](https://github.com/amsikking/SOLS_microscope).

This plugin accepts a folder with at least subdirectories of data and metadata as an input.

## Quickstart

### A. Getting the plugin working (choose either a or b, you don't have to do both)
#### a. Through pip-install:
1. pip install snouty-viewer (within a virtual environment of Python 3.8, 3.9, or 3.10 recommended)
2. Open up napari
#### b. Through Napari:
1. Open up napari
2. Plugins > Install/Uninstall plugins
3. Search for "snouty-viewer"
4. Install
5. (Maybe need to) reopen napari

### B. Viewing raw Snouty data
- Drag and drop a root folder of your Snouty data. This is the folder that includes the data and metadata subfolders.
- Select "Snouty Viewer" for opening.

### C. Converting raw Snouty data to its native view
1. Click plugins, snouty-viewer -> Native View
2. Select the file you want to convert
3. Press Deskew

### D. Saving your native view file
1. Select the channel (or multi-channel) layer you want to save
2. File > Save Selected Layer(s)...
3. Select where you want to save your file
4. Title your file, ".ome.tif" will automatically be appended.
5. Save with "Snouty Writer"
6. Wait (this could take a few minutes depending on your file's size and your hardware)

### E. Batch saving
1. Click plugins, snouty-viewer -> Batch Deskew & Save
2. Input a directory (without quotes) that contains 1 or more Snouty-acquired directories.
3. If you want to view your deskewed outputs, check the box.
4. If you want to automatically save the deskewed outputs, check the box.
5. Press Deskew and save
6. Wait (this could take a few minutes depending on your files' sizes and your hardware)
## Getting Help
- Open up an issue on [GitHub](https://github.com/aelefebv/snouty-viewer/issues).
- Start a thread on [image.sc](https://forum.image.sc/)

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->

## Installation

You can install `snouty-viewer` via [pip]:

    pip install snouty-viewer



To install latest development version :

    pip install git+https://github.com/aelefebv/snouty-viewer.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"snouty-viewer" is free and open source software

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

[file an issue]: https://github.com/aelefebv/snouty-viewer/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
