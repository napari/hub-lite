
[![License](https://img.shields.io/pypi/l/napari-metroid.svg?color=green)](https://github.com/zoccoler/napari-metroid/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-metroid.svg?color=green)](https://pypi.org/project/napari-metroid)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-metroid.svg?color=green)](https://python.org)
[![tests](https://github.com/zoccoler/napari-metroid/workflows/tests/badge.svg)](https://github.com/zoccoler/napari-metroid/actions)
[![codecov](https://codecov.io/gh/zoccoler/napari-metroid/branch/main/graph/badge.svg)](https://codecov.io/gh/zoccoler/napari-metroid)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-metroid)](https://napari-hub.org/plugins/napari-metroid)

This napari plugin is an adaptation of [metroid](https://github.com/zoccoler/metroid). It creates several regions of interest of similar area over cells in a fluorescence video (2D+time). It then gets ROIs means over time and performs signal denoising: fixes photobleaching and separates signal from noise by means of blind source separation (with or without wavelet filtering).

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## A Picture (to boil down a thousand words)

Below is the graphical abstract of the Metroid software. This napari plugin works very similarly.

![](https://github.com/zoccoler/metroid/blob/master/Metroid_flowchart.png)

## Table of Contents

- [Quick Walktrough](#quick-walkthrough)
- [Installation](#installation)
- [Usage](#usage)
  - [Open Sample Data](#open-sample-data)
  - [Open Plugin Main Interface](#open-plugin-main-interface)
  - [Auto-generate Cell Mask](#auto-generate-cell-mask)
  - [Split Mask into ROIs](#split-mask-into-rois)
  - [Get ROI Means over Time](#get-roi-means-over-time)
  - [Remove Photobleaching](#remove-photobleaching)
  - [Filter Signals](#filter-signals)
  - [Save outputs](#save-outputs)
- [Contributing](#contributing)
- [Citing napari-metroid](#citing-napari-metroid)
- [License](#license)
- [Issues](#issues)

## Quick Walkthrough

Below is a full demonstration of using napari-metroid. It shows the following:
  * Open sample data;
  * Create cell mask;
  * Split mask into ROIs of similar area;
  * Get ROIs signals over time and plots two of them;
  * Remove photobleaching;
  * Remove noise:
    * Use ICA to decompose ROIs signals into independent components;
    * Plot 4 components;
    * Manually select the component of interest (source);
    * Perform inverse transformation with selected source;
        
![](https://github.com/zoccoler/napari-metroid/raw/main/figures/napari_metroid_demo.gif)

## Installation

Download and install [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html#).

Create a new conda environment:

    conda create -n metroid-env python=3.8

Install napari, e.g. via pip:

    pip install "napari[all]"

Install `napari-metroid` via [pip]:

    pip install napari-metroid

To install latest development version :

    pip install git+https://github.com/zoccoler/napari-metroid.git

## Usage
### Open Sample Data

This plugin comes with two sample videos:
- Cell1 Video Action Potential: 2D + time fluorescence video of a rat isolated cardiomyocyte labeled with a membrane potential dye upon which an external electrical field pulse is applied.
- Cell1 Video Electroporation: Same cell, but submitted to a strong external electrical field pulse.

You can open them under "File -> Open Sample -> napari-metroid", as shown below. Both videos are loaded from the [metroid main repository](https://github.com/zoccoler/metroid). To know more about the experimental conditions, please refer to the [original publication](https://doi.org/10.1186/s12859-020-03661-9).

![](https://github.com/zoccoler/napari-metroid/raw/main/figures/load_sample_data.gif)

### Open Plugin Main Interface

![](https://github.com/zoccoler/napari-metroid/raw/main/figures/open_plugin.gif)

### Auto-generate Cell Mask

Metroid can generate cell binary masks automatically by cumulative sum of images until any pixel saturation happens. It then applies Otsu thresholding and removes small objects.

![](https://github.com/zoccoler/napari-metroid/raw/main/figures/auto_create_mask.png)

### Split Mask into ROIs

By default, a cell mask is split into 32 regions of interest (ROIs) in a double-layer fashion: An outer layer of ROIs and an inner layer. 
The method is solely based on the shape of the cell mask and the main criteria is that ROIs must have similar areas. The number of ROIs in each layer can be editted. 

![](https://github.com/zoccoler/napari-metroid/raw/main/figures/mess.png)

### Get ROI Means over Time

The 'Get Signals' button serves to collect each ROI mean fluorescence over time and enable plotting. There, you can optionally provide the frame rate so that the time axis is properly displayed.
Double click over a ROI to have its signal plotted. Hold the 'ALT' key to plot multiple signals together.

![](https://github.com/zoccoler/napari-metroid/raw/main/figures/get_signals.gif)

### Remove Photobleaching

Metroid removes photobleaching by curve fitting over time periods that lack the cellular signal (which can be an action potential or an electroporation signal). That is why the 'Transitory' parameter is important. Action potentials are transitory signals whereas electroporation (at least for the duration of this experiment) are not, and the algorithm must be informed about that for proper trend removal.

![](https://github.com/zoccoler/napari-metroid/raw/main/figures/remov_photob.gif)

### Filter Signals

Cellular signals are filtered by separating signal components with either PCA or ICA (plus optional wavelet filtering). It then chooses one (or several) components and it applies the inverse transform using only the selected components. Metroid can do this component/source selection automatically based on estimations of signal power. Instead, we show below the manual selection procedure, where 4 components are plotted and the user selects one of them.

![](https://github.com/zoccoler/napari-metroid/raw/main/figures/bssd.gif)

### Save Outputs

Raw, corrected and filtered signals, as well as time and components, are arranged in a table with values for each time point. The table is displayed as a widget after each Run button click. Estimated signal-to-noise (SNR) in dB for each label/ROI are also provided (in this case, each line corresponds to a ROI, not a time point).
The user can save these data by clicking on the buttons "Copy to clipboard" or "Save as csv...".

![](https://github.com/zoccoler/napari-metroid/raw/main/figures/table_widget.png)

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## Citing napari-metroid

If you use this plugin in your research, please be kind to cite the original paper below:

Zoccoler, M., de Oliveira, P.X. METROID: an automated method for robust quantification of subcellular fluorescence events at low SNR. BMC Bioinformatics 21, 332 (2020). https://doi.org/10.1186/s12859-020-03661-9

## License

Distributed under the terms of the [BSD-3] license,
"napari-metroid" is free and open source software

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

[file an issue]: https://github.com/zoccoler/napari-metroid/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


