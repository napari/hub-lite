<img style="float: right;" src="https://imaging.epfl.ch/resources/logo-for-gitlab.svg">


# napari-bee-annotator
Developed by the [EPFL Center for Imaging](https://imaging.epfl.ch/) for the [Mobile Robotic Systems Group](https://www.epfl.ch/labs/mobots/) in Dec 2023.
This napari plugin provides an easy way for the researches to annotate honey bees leaving/entering the hive. The annotations will serve as ground truth for the validation of various automated animal tracking approaches.

[![License BSD-3](https://img.shields.io/pypi/l/napari-bee-annotator.svg?color=green)](https://github.com/EPFL-Center-for-Imaging/napari-bee-annotator/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-bee-annotator.svg?color=green)](https://pypi.org/project/napari-bee-annotator)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-bee-annotator.svg?color=green)](https://python.org)
[![tests](https://github.com/EPFL-Center-for-Imaging/napari-bee-annotator/workflows/tests/badge.svg)](https://github.com/EPFL-Center-for-Imaging/napari-bee-annotator/actions)
[![codecov](https://codecov.io/gh/EPFL-Center-for-Imaging/napari-bee-annotator/branch/main/graph/badge.svg)](https://codecov.io/gh/EPFL-Center-for-Imaging/napari-bee-annotator)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-bee-annotator)](https://napari-hub.org/plugins/napari-bee-annotator)

## Installation

You can install `napari-bee-annotator` via [pip]:

    pip install napari-bee-annotator



To install latest development version :

    pip install git+https://github.com/EPFL-Center-for-Imaging/napari-bee-annotator.git

## Getting started

1. Open napari with the plugin and your video using the following command `napari -w napari-bee-annotator --plugin video path/to/video.mp4`. Note that you need to have [napari_video](https://www.napari-hub.org/plugins/napari_video) installed to read `mp4` files.

2. Select the orientation of your video: horizontal/vertical refers to the direction of the bee's leaving/entering the hive.

3. Start annotating: A simple left click indicates a bee moving up or to the left depending on the orientation selected. You can hold down the shift key to annotate a bee moving down or to the right. Annotations can be deleted with a right click on the annotation you want to delete. To move to the next frame, you can either hold down `ctrl` and scroll with the mouse wheel or click on the play button. Playback parameters, such as the playback speed, can be changed by right clicking on the play button.

4. Saving and loading tracks: To save a tracks layer selected from the list of layers and click on `File > Save selected layers`. Choose a name and the csv extension. If you want to continue to work on the annotations for a specific video, you first have to load the corresponding csv file by clicking on `Open with Plugin > Open file(s)...`. Select the file you want to load and click on open. A dialog should pop up that asks you to select the reader to use for loading the csv file. Select `Bee annotator`. Lastly, you have to tell the plugin to interact with the layer you just loaded by selecting it in the `Tracks layer` drop down menu.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-bee-annotator" is free and open source software

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

[file an issue]: https://github.com/EPFL-Center-for-Imaging/napari-bee-annotator/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
