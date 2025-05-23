
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/FrancisCrickInstitute/CALM_Template/HEAD?labpath=blob%2Fmain%2Fsegment_image.ipynb)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3115/)
![Commit activity](https://img.shields.io/github/commit-activity/y/FrancisCrickInstitute/CALM_Template?style=plastic)
![GitHub](https://img.shields.io/github/license/FrancisCrickInstitute/CALM_Template?color=green&style=plastic)

PARSEG (PAralellised Refinement of SEGmentations) combines segmentation masks and filters overlapping objects based on colocalization statistics, such as percent overlap. 

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

## Overview
By leveraging [Dask], PARSEG filters overlapping segmentations masks in a computationally efficient manner by processing individual 2D slices in parallel. 

There are two different ways to interact with PARSEG and use it for different objectives:

* As a napari plugin for graphical user interaction
* As a Python API to allow users to integrate PARSEG tools into their own custom workflows

## Installation

You can install `napari-segmentation-overlap-filter` via [pip]:

    pip install napari-segmentation-overlap-filter

## Getting Started

### Napari Plugin
1. Download the example dataset images
2. Start napari and open both images as separate layers
3. Convert the layers from an `Image Layer` to a `Labels Layer` by right-clicking on the layer
4. Open the plugin with `Plugins > Segmentation Overlap Filter` and the widget will appear on the right
5. Select the two segmentation masks you'd like to combine using the drop down and menu
6. Drag the slider to set percent overlap allowed
7. Click `Run`
8. Optionally, export the overlap dataframe as a csv file

### Python API
This [example notebook] shows how you can integrate the Python API into your own workflow for filtering and combining overlapping segmentation masks

## Issues

If you encounter any problems, please file an issue along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[Dask]: https://www.dask.org/
[pip]: https://pypi.org/project/pip/
[example notebook]: https://github.com/FrancisCrickInstitute/PARSEG/blob/main/Notebooks/Combine_Segmentations_And_Filter_Overlaps.ipynb
