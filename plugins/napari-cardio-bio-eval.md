
[![License BSD-3](https://img.shields.io/pypi/l/napari-cardio-bio-eval.svg?color=green)](https://github.com/Nanobiosensorics/napari-cardio-bio-eval/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-cardio-bio-eval.svg?color=green)](https://pypi.org/project/napari-cardio-bio-eval)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-cardio-bio-eval.svg?color=green)](https://python.org)
[![tests](https://github.com/Nanobiosensorics/napari-cardio-bio-eval/workflows/tests/badge.svg)](https://github.com//Nanobiosensorics/napari-cardio-bio-eval/actions)
<!--[![codecov](https://codecov.io/gh/Nanobiosensorics/napari-cardio-bio-eval/branch/main/graph/badge.svg)](https://codecov.io/gh/Nanobiosensorics/napari-cardio-bio-eval)-->
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-cardio-bio-eval)](https://napari-hub.org/plugins/napari-cardio-bio-eval)

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

----------------------------------

The plugin provides a widget which can load, preprocess, annotate and export cardio biosensor data.  

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-cardio-bio-eval` via [pip]:

    pip install napari-cardio-bio-eval

Or use the Napari plugin manager and search for `napari-cardio-bio-eval`.

<!--
First install a fresh conda enviroment (or other python enviroment) and activate it:

    conda create -y -n napari-env -c conda-forge python=3.10
    conda activate napari-env

Then you can pip install the plugin from the github repository and it will also downloads the necessary packages:

    pip install git+https://github.com/Nanobiosensorics/napari-cardio-bio-eval

Then you can start napari with a simple command:

    napari
-->
# Usage

You can open the plugin's widgets from the **Plugins** menu after the installation of the plugin.

![image](https://github.com/Nanobiosensorics/napari-cardio-bio-eval/assets/78443646/5d209fb5-c921-45d6-bb63-c5e3ff1fb1f8)

## Data loading and preprocessing

At the top of the widget, you need to select the directory, which contains the data you want to examine and process. To successfully load the data the directory have to contain the following files:
- *_wl_power.file: which contains the starting values of the measurement
- DRM directory: which contains the difference from the previous measurement point 
- *_avg.file: which contains additional biosensor data

#### Import parameters:  
- Flipping: horizontal and vertical mirroring of the biosensor recording
- Signal range type: with this you can choose how do you want to select a smaller range of the measurement in the next field *Ranges*
    - measurement phase: you can give the index of the phases you want to see, for example with 0-1 you can view the measurement from the start to the first pause
    - individual point: you can select any given frames in an interval, for example with selecting 34 and 275 you can view the measurement from frame 34 to frame 275
- Ranges: if you choose measurement phase then give the range of the phases you want to see and if you choose individual point then select the starting and end frames. The label above helps as it shows the phrases (except the last one) and the full time of the measurement. The minimum frame or phase must be smaller than the maximum.
- Drift correction threshold: Ranges between 25 and 500.
- Filter method: mean or median

![image](https://github.com/Nanobiosensorics/napari-cardio-bio-eval/assets/78443646/28b5f563-1c5e-4591-bdf6-2ece936becac)

![image](https://github.com/Nanobiosensorics/napari-cardio-bio-eval/assets/78443646/a6004667-deac-4ff8-8729-0fcb8bc35f7f)

After selecting the source directory and the optional fliping you can load in the data with the ***Load Data*** button. After the raw data is loaded you can select the slice of the measurement you want to work with and some other parameters. Then by clicking the ***Preprocess Data*** button you start the processing and after a few seconds the well images will appear on the viewer.  

![image](https://github.com/Nanobiosensorics/napari-cardio-bio-eval/assets/78443646/23e38c70-d058-41cc-9e9e-f2d34ea553e0)

Each well has its own layer. You can turn the layers visible or invisible by clicking the small eye icon on each layer.

If the selected range is not what you wanted then you can change the parameters and preprocess again. But if you moved on to the next step (manual background selection or peak detection) then you need to restart Napari to load other data or preprocess with different parameters.

After you see the wells you can proceed to the next step or if the automatic background correction is not good enough you can click the ***Select Background Points Manually*** button and it will show the automatically selected background points for each well, which you can move to better background coordinates and in the next peak detection step these points will be used by the background correction algorithm. After the first export these points will be saved so if the same directory is loaded a second time the preprocessing will use these points.

During the background selection do NOT delete any layers.

![image](https://github.com/Nanobiosensorics/napari-cardio-bio-eval/assets/78443646/133fd74a-b53b-4540-bdf9-209c325e2b4b)

## Selecting the cells

In this step you can also set some parameters for the peak detection algorithm and then click the ***Detect Signal Peaks*** button to start the process. After a few seconds the wells with the potential cells will show on the window.

#### Detection parameters:  
- Threshold range: 25-5000
- Neighbourhood size: 1-10
- Error mask filtering:

![image](https://github.com/Nanobiosensorics/napari-cardio-bio-eval/assets/78443646/842ad2e3-32dd-4d6c-8e98-47c137a7029b)

Here you can delete, add or move the points on each points layer. There are keyboard shortcuts for easier use! 
Additionally by double clicking on any point of the image you can examine the time-signal diagram of the selected point under the widget. Be sure to select the correct layer!  

If you do not need any of the wells, then you can delete the layer and it won't be exported. If you either delete an image or peak points layer belonging to a well, the well will not be included in the export!  
After selecting the needed cells and wells (and deleting the unnecessary ones) you can export plots and additional information about them.

## Exporting

You can select what kind of data do you want to export and click the ***Export Data*** button. The data will be exported to the source directory into a *result* sub-directory.

#### Export options:
- Coordinates: the coordinates of the selected cells
- Preprocessed signals: 
- Raw signals:
- Average signal: 
- Breakdown signal: 
- Max well: 
- Plot signals with well:  
- Plot well with coordinates: 
- Plot cells individually: 
- Signal parts by phases: 
- Max centered signals: 

## Segmentation widget

The data loading and preprocessing is the same but it uses a deep learning model to segment the cells.

## License

Distributed under the terms of the [BSD-3] license,
"napari-cardio-bio-eval" is free and open source software

## Issues

If you encounter any problems, please file an issue along with a detailed description.

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
