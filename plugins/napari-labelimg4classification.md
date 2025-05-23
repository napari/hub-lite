
[![License](https://img.shields.io/pypi/l/napari-labelimg4classification.svg?color=green)](https://github.com/hiroalchem/napari-labelimg4classification/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-labelimg4classification.svg?color=green)](https://pypi.org/project/napari-labelimg4classification)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-labelimg4classification.svg?color=green)](https://python.org)
[![tests](https://github.com/hiroalchem/napari-labelimg4classification/workflows/tests/badge.svg)](https://github.com/hiroalchem/napari-labelimg4classification/actions)
[![codecov](https://codecov.io/gh/hiroalchem/napari-labelimg4classification/branch/main/graph/badge.svg)](https://codecov.io/gh/hiroalchem/napari-labelimg4classification)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-labelimg4classification)](https://napari-hub.org/plugins/napari-labelimg4classification)

A simple image-level annotation tool supporting multi-channel images for napari.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

## Usage
Start the labeling tool from the menu `Utilities > label tool for classification`.   
First, click on the Choose directory button to open the folder selection window, and select the folder that contains the
 images you want to label and annotate.   
It will automatically list and display the images of tif, png, jpg, and bmp formats.
If you want to view the channels of a multi-channel image separately, check the split channels checkbox.
![](https://github.com/hiroalchem/napari-labelimg4classification/raw/main/docs/open.gif)

Initially, all channels will be opened in grayscale, but the pseudo-color and contrast adjustments you specified will be
 carried over when you open the next image.   
Thanks to napari, you can freely merge channels and turn them on and off.   
Label classes can be added, and can be removed by typing the same name as an already added class.
![](https://github.com/hiroalchem/napari-labelimg4classification/raw/main/docs/color_and_label.gif)


It will automatically save the labels.csv file with the image path and label, and the class.txt file with the class of the label.
![](https://github.com/hiroalchem/napari-labelimg4classification/raw/main/docs/class_and_labels.png)

If labels.csv and class.txt are already in the folder, they will be loaded and reflected automatically.
![](https://github.com/hiroalchem/napari-labelimg4classification/raw/main/docs/reopen.gif)

## Installation

You can install `napari-labelimg4classification` via [pip]:

    pip install napari-labelimg4classification



To install latest development version :

    pip install git+https://github.com/hiroalchem/napari-labelimg4classification.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-labelimg4classification" is free and open source software

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

[file an issue]: https://github.com/hiroalchem/napari-labelimg4classification/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


