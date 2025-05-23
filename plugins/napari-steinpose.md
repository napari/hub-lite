
[![License BSD-3](https://img.shields.io/pypi/l/napari-steinpose.svg?color=green)](https://github.com/guiwitz/napari-steinpose/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-steinpose.svg?color=green)](https://pypi.org/project/napari-steinpose)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-steinpose.svg?color=green)](https://python.org)
[![tests](https://github.com/guiwitz/napari-steinpose/workflows/tests/badge.svg)](https://github.com/guiwitz/napari-steinpose/actions)
[![codecov](https://codecov.io/gh/guiwitz/napari-steinpose/branch/main/graph/badge.svg)](https://codecov.io/gh/guiwitz/napari-steinpose)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-steinpose)](https://napari-hub.org/plugins/napari-steinpose)

This napari plugin allows to segment and extract information from Imaging Mass Cytometry data by combining the [cellpose](http://www.cellpose.org/) and [steinbock](https://bodenmillergroup.github.io/steinbock/v0.14.2/) tools.

## Installation

In order to use this plugin, whe highly recommend to create a specific environment and to install the required software in it. You can create a conda environment using:

    conda create -n steinpose python=3.8.5 napari -c conda-forge

Then activate it and install the plugin:
    
    conda activate steinpose
    pip install napari-steinpose

### Potential issue with PyTorch

Cellpose and therefore the plugin and napari can crash without warning in some cases with ```torch==1.12.0```. This can be fixed by reverting to an earlier version using:
    
    pip install torch==1.11.0

### GPU

In order to use a GPU:

1. Uninstall the PyTorch version that gets installed by default with Cellpose:

        pip uninstall torch

2. Make sure your have up-to-date drivers for your NVIDIA card installed.

3. Re-install a GPU version of PyTorch via conda using a command that you can find [here](https://pytorch.org/get-started/locally/) (this takes care of the cuda toolkit, cudnn etc. so **no need to install manually anything more than the driver**). The command will look like this:

        conda install pytorch torchvision cudatoolkit=11.3 -c pytorch

### Plugin Updates

To update the plugin, you only need to activate the existing environment and install the new version:

    conda activate steinpose
    pip install git+https://github.com/guiwitz/napari-steinpose.git -U

## Usage

Here is a short summary on how to proceed to use the plugin. For more detailed information, please visit [this page](https://guiwitz.github.io/napari-steinpose).

### Load data

Using the "Select data folder" button, select a folder containing your .mcd files. The contents of the folder will appear in the List of images box. When you select one of the files it is loaded in the viewer. Using the ROI spinpox, you can change the roi (or acquisition) to be visualized.
### Segmentation

1. In the channels tab, choose the combination of channels to use to define images to segment. You can choose what type of projection (mean, min etc.) is used to combine channels. You can either select channels defining both cells and nuclei or just a single channel. **Note that if you want to just segment nuclei, you need to select them as "cell channel".**

2. To save the output, select a folder using the "Select output folder" button.

3. In the segmentation tab, pick a cellpose model to use. If you use one of the built-in models, you can specify the average diameter of objects to detect.

4. In the Options tab, you can set a few more options:
   - cellpose options: you can adjust the flow threshold and cell probabilities. If cells are missing try to use higher values of flow threshold (close to 1) and lower values for the cell probabilities (around -6)
   - segmentation options: you can decide to remove segmentation touching the image border, and you can also decide to expand the segmented objects by a fixed number of pixels. If a segmentation is displayed in the viewer, adjusting this parameter will live-adjust the mask.

5. You can first test the segmentation using the "Run on current image" button. Once segmentation is done, the corresponding mask is displayed. You can then run the segmentation over all ROIs of **all .mcd files** present in the folder by using the "Run on folder" button.

### Post-processing

In the Segmentation tab, if you tick the box "Run steinbock post-processing", information will directly be extracted from images and masks at the end of segmentation. Processing is done via steinbock and generates files compatible with further downstream processing.

In the Export tab, you can select what type of information to export: object intensities, geometric properties and object neighbourhood. Note that if you have performed a segmentation without post-processing, you can still run post-processing using the "Run steinbock postproc" button.

### Saving settings

To avoid having to re-type the same settings repeatedly, you can export a give configuration using the "Export config" button in the Options tab. This generates a human readable .yml file with:
- segmentation options
- channels selected for projections

The file is saved in the output folder. You can just copy the file in a new empty output folder to use it for an other analysis run. Once you select that folder containing a configuration file, you can import it with the "Import config" button. **Note that you need to have an image opened so that channels can be selected properly.**
## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-steinpose" is free and open source software

## Authors

The author of this plugin is Guillaume Witz, Data Science Lab and Microscopy Imaging Center, University of Bern. This plugin is the result of a collaboration with the Imaging Mass Cytometry and Mass Cytometry Platform, University of Bern.

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

[file an issue]: https://github.com/guiwitz/napari-steinpose/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
