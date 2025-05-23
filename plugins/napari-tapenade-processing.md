
[![License MIT](https://img.shields.io/pypi/l/napari-tapenade-processing.svg?color=green)](https://github.com/jules-vanaret/napari-tapenade-processing/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-tapenade-processing.svg?color=green)](https://pypi.org/project/napari-tapenade-processing)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-tapenade-processing.svg?color=green)](https://python.org)
[![tests](https://github.com/jules-vanaret/napari-tapenade-processing/workflows/tests/badge.svg)](https://github.com/jules-vanaret/napari-tapenade-processing/actions)
[![codecov](https://codecov.io/gh/jules-vanaret/napari-tapenade-processing/branch/main/graph/badge.svg)](https://codecov.io/gh/jules-vanaret/napari-tapenade-processing)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-tapenade-processing)](https://napari-hub.org/plugins/napari-tapenade-processing)

<img src="https://github.com/GuignardLab/tapenade/blob/main/imgs/tapenade3.png" width="100">

A collection of methods to process images of deep 3D/3D+time tissues in Napari.

`napari-tapenade-processing` is a [napari] plugin that is part of the [Tapenade](https://github.com/GuignardLab/tapenade) project. Tapenade is a tool for the analysis of dense 3D tissues acquired with deep imaging microscopy. It is designed to be user-friendly and to provide a comprehensive analysis of the data.

If you use this plugin for your research, please [cite us](https://github.com/GuignardLab/tapenade/blob/main/README.md#how-to-cite).

## Overview

<img src="imgs/napari_preproc_demo.gif"/>

While working with large and dense 3D and 3D+time gastruloid datasets, we found that being able to visualise and interact with the data dynamically greatly helped processing it.
During the pre-processing stage, dynamical exploration and interaction led to faster tuning of the parameters by allowing direct visual feedback, and gave key biophysical insight during the analysis stage.

From a given set of raw images, segmented object instances, and object mask, the plugin allows the user to quickly run all pre-processing functions from our main pipeline with custom parameters while being able to see and interact with the result of each step. For large datasets that are cumbersome to manipulate or cannot be loaded in Napari, the plugin provides a macro recording feature: the users can experiment and design their own pipeline on a smaller subset of the dataset, then run it on the full dataset without having to load it in Napari.

<img src="imgs/Fig_Napari_preprocessing.png">

## Installation

The plugin obviously requires [napari] to run. If you don't have it yet, follow the instructions [here](https://napari.org/stable/tutorials/fundamentals/installation.html).

The simplest way to install `napari-tapenade-processing` is via the [napari] plugin manager. Open Napari, go to `Plugins > Install/Uninstall Packages...` and search for `napari-tapenade-processing`. Click on the install button and you are ready to go!

You can also install `napari-tapenade-processing` via [pip]:

    pip install napari-tapenade-processing

To install latest development version :

    pip install git+https://github.com/jules-vanaret/napari-tapenade-processing.git

## Usage

### General overview of the plugin within Napari

<img src="imgs/proc_0.png">

To start a pre-processing pipeline, follow these steps:

1. First, load your images in Napari. You can drag and drop them from your file explorer to the Napari viewer, or open them using the `File > Open files...` menu.
2. Click on the `Plugins > Tapenade Processing` menu to open the plugin.
3. The image you have loaded will be displayed as individual layers in the Layer List. They can be clicked-on to reveal a set of visual parameters (see 4) that can be adjusted. By double-clicking on a layer name, you can change it. Right-clicking a layer will give you several options. The little eye icon next to the layer name can be clicked to hide the layer.
4. You can adjust visual parameters for each layer, like the contrast limits, the colormap, the opacity, the blending mode, etc.
5. If you want to switch between 2D and 3D views, click on the `Toggle 2D/3D view` button (it resembles a square when in 2D mode, or a cube when in 3D mode).
6. You can toggle the grid view (as shown in the example image) by clicking on the `Toggle grid mode` button. By right-clicking the button, you can parametrize the grid view (e.g number of columns, number of rows, etc).
7. The plugin is composed of three tabs. The first tab is dedicated to pre-processing functions, the second tab is dedicated to the macro recording feature, and the third tab is dedicated to advanced parameters.

### Tab 1: The pre-processing functions

<img src="imgs/proc_1.png" width=300>

The pre-processing tab is composed of the following elements:

1. A combo box to select the pre-processing function to apply from a list.
2. A set of comboxes that allow you to select the layers to apply the function on. If a function does not require a specific layer, the combo box will be greyed out. `Image` layers correspond to integer or float data, `Labels` layers correspond to integer data and represent segmented object instances, `Mask` layers correspond to boolean data and usually represent the sample's large scale mask (inside/outside). All layers must have data of the same shape (same number of dimensions and same dimensions). Layers can be 3D or 3D+time, respectively with the ZYX or TZYX order.
(2') If a layer does not appear in a combo box, but is present in the Layer List, you can click on the `Refresh` button to update the list of layers.
3. A set of parameters that you can tune to adjust the function's behaviour. The parameters are specific to each function. In case of doubt, you can click on the little `[?]` button next to the widget to get a tooltip with a description.
4. A `Run function` button to apply the function with the current parameters to the previously selected layers.


### Tab 2: The macro recording feature

#### A. Recording a macro

<img src="imgs/proc_macro_1.png" width=300>

To record a macro, click on the `Macro recording` tab and follow these steps:

1. Click on `Choose directory` to select a folder where the macro file will be saved.
2. Click on `Start recording macro` to start recording the functions you will apply. At this point, you can start applying sequences of functions to images/segementations/masks that you have already loaded in Napari or that you load in the middle of the recording. 

<img src="imgs/proc_macro_2.png" width=300>

3. When you are finished, click `Stop recording and save macro`. It will be saved in the JSON (`.json`) format, and the name will follow the pattern `recorder_parameters_YYYY-MM-DD_HH-MM-SS.json`.

#### B. Running a macro

Macros allow you to run a sequence of functions in batch on folders of input TIFF images (either different frames of the same 3D+t image, or several 3D images). The input images should be in the same folder, and the output will be saved in a folder of your choice. The output of each function will be saved in a separate folder, and the name of the folder will be linked to the name of the function.

<img src="imgs/proc_macro_3.png" width=300>

To run a macro, click on the `Macro recording` tab and follow these steps:

1. Click on `Select file` to choose the macro file you want to run.
2. After specifying the path to the macro file, several path entries with names like `Path to folder ([...]) N` (e.g `Path to folder (['Image'] 1`) will appear. Click on the `Choose directory` button to select the folder where the input images (TIFF files) are located.
3. Click on `Choose directory` under `Path to save outputs folders of tifs` to select the folder where the results of the pipeline will be saved. Each function call will generate a folder whose name will be linked to the name of the function.
4. You can click the `Compress when saving` checkbox to save the output TIFF images in a compressed format using ZLIB compression. 
5. Choose the number of workers to use for parallel processing. The default value is 1, which means that the functions will be run sequentially on the images. If you have a multi-core CPU, you can increase this value to speed up the processing. Be careful that setting this value too high can lead to memory issues.
6. Click on `Run macro` to start the processing. You will see as many folders as there are steps in your pipeline, containing the results on each frame.


### Tab 3: Advanced parameters

<img src="imgs/proc_2.png" width=300>

The advanced parameters tab is composed of the following elements:

1. A checkbox `New layers overwrite previous ones`: whether the output of the pre-processing functions should be saved as new layers or overwrite the previous ones that were used as input. This can be useful to save memory when you don't need to compare the input and output of a function.

## Demo dataset

A demo dataset is available [here](https://amubox.univ-amu.fr/s/MRdFy3KqQNjpyHa).

### Content

This test dataset is composed of a folder `folder_raw_data` which contains 5 separate frames (3D images), and a macro Json file `recorder_parameters.json`.  

### How to use

 - Download the folder `folder_raw_data`. 
 - Load one of the image from the folder (either drag and drop, or `File>Open file(s)`) and start creating your own pipeline.
 - To try batch processing through the macro feature, click on the `Macro recording tab`, choose a path to save the macro Json file, click on `Start recording macro`, and perform a sequence of function runs of your choice. When you are finished, click `Stop recording and save macro`. Then specify the path to your macro file below (alternatively, a valid Json file is also made available), the folder where the rest of the frames are located, and the folder where the results of the pipeline will be saved. Click on run macro. You should see as many folders as there are steps in your pipeline, containing the results on each frame.


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-tapenade-processing" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.


----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

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

[file an issue]: https://github.com/jules-vanaret/napari-tapenade-processing/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
