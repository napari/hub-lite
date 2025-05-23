
[![License BSD-3](https://img.shields.io/pypi/l/napari-spofi.svg?color=green)](https://github.com/githubuser/napari-spofi/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-spofi.svg?color=green)](https://pypi.org/project/napari-spofi)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-spofi.svg?color=green)](https://python.org)
[![tests](https://github.com/githubuser/napari-spofi/workflows/tests/badge.svg)](https://github.com/githubuser/napari-spofi/actions)
[![codecov](https://codecov.io/gh/githubuser/napari-spofi/branch/main/graph/badge.svg)](https://codecov.io/gh/githubuser/napari-spofi)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-spofi)](https://napari-hub.org/plugins/napari-spofi)

napari plugin to interactively train and test a StarDist model

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started


and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Description

This plugin provides tools for annotating spots in a 3D two-channel image (hdf5 type input file),
submitting tiles for StarDist model generation or model re-training, and refining initial annotations
based on predictions (kind of human-in-the-loop approach).

The objects of interest in the image are sphere-like spots with a diameter of just a
few pixels and are thus well suited for StarDist instance segmentation. The image 
dimensions are typically 1024x1024 pixels in xy and ≥ 64 sections in z.


## Installation

With python and pip installed (e.g., via miniconda or miniforge),
it is recommended to create a new environment and install `napari-spofi` using pip.

    pip install napari napari-spofi

## Starting `napari-spofi`

Start `napari` and select "spot finder (napari-spofi)" from the "plugin" menu.

### Annotate image
Go to the 'annotation' section of the widget and create a new directory for annotations. Add an image
folder containing at least one h5 file (foreground and background, e.g., 'ch1' & 'ch2'). Select an image file, foreground and background
channels. Load the image file.

Inspect the image for distinct regions. To help locate relevant tile positions, make
the 'checkerboard' layer visible. While the 'tiles' layer is active, double-click a tile
to add it to the list of tiles. This list will be used to generate a set of 
images and masks for training purposes.

Switch to napari's 2D view. Navigate to the centre section of each spot in the active tile
and annotate by adding points (one point per spot) using the 'true' points layer. The
built-in heuristic will automatically annotate pixels that belong to individual spots.
Some image enhancement step before loading images may be beneficial. 

Annotate tiles in one or a multiple images.
To prepare training data, use the 'extract spots' button.

### Train a StarDist model
Go to the 'training' section of the widget. Adjust the "number of epochs". For a first
check, 100 epochs is a good start. The plugin uses a simplified setup for StarDist
configurations (please see [StarDist](https://github.com/stardist/stardist/) for a full discussion).

Start training and watch the 'loss' and 'val_loss' values, which should decrease
steadily while their ratio should roughly remain at 1 as training progresses.

The retrain option allows the selection of an existing model for retraining.

### Predict instances
Go to the 'prediction' section of the widget to start spot prediction for the
currently loaded image. Select the appropriate model from the given annotation
directory. The 'threshold' value is calculated from the validation data and can be
adjusted. Start a new prediction and load the predicted spots when the process has
finished. (It is possible to load an existing prediction).

### Polish annotation
Predicted spots will be loaded into two new layers: 'predicted' and 'edited'. The
'predicted' layer is not editable and gives an overview of the spots found. Check
your annotation in the active tiles ('true' layer) and compare it carefully with
the spots in the 'edited' layer.
Adjust the positions of the spots or remove any incorrect spots from the 'edited'
layer. Extract the spots and train a new model or retrain the model.



## Contributing

Contributions are very welcome.

## License

Distributed under the terms of the [BSD-3] license,
"napari-spofi" is free and open source software

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

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
