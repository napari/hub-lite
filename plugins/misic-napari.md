
<!-- [![License](https://img.shields.io/pypi/l/misic-napari-plugin.svg?color=green)](https://github.com/pswap/misic-napari-plugin/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/misic-napari-plugin.svg?color=green)](https://pypi.org/project/misic-napari-plugin)
[![Python Version](https://img.shields.io/pypi/pyversions/misic-napari-plugin.svg?color=green)](https://python.org)
[![tests](https://github.com/pswap/misic-napari-plugin/workflows/tests/badge.svg)](https://github.com/pswap/misic-napari-plugin/actions)
[![codecov](https://codecov.io/gh/pswap/misic-napari-plugin/branch/master/graph/badge.svg)](https://codecov.io/gh/pswap/misic-napari-plugin) -->

----------------------------------

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

A napari plugin for [MiSiC](https://elifesciences.org/articles/65151). Segmentation of bacteria in dense colonies. 
The plugin provides acces to preprocessing of the image like scaling, gamma correction, sharpness and noise variance that can improve the segmentation of bacteria irrespective of the imaging modality.

## Install Napari
Install napari either the bundled app or through [pip/conda]
https://napari.org/#installation

## Installation

Install `misic-napari` through plugin manager in napari.

Or

You can install `misic-napari` via [pip] in the napari console:

    pip install misic-napari

## Tutorial
Note: 
The image should be in the format [n,row,col] or [row,col], i.e., a single image or a stack. Hyper-stacks are not supported yet. 

#### get_width


Creates a Shapes layer with name 'cell-width' where the cell width can be hand drawn using line drawing tools in the shapes layer. This need not be precise and can be adjusted later. Click `get_cell_width` to obtain the desired mean cell width. This will be used to scale the image accordingly before segmentation.
 
#### segment

This can be used to quickly set the parameters that can be later used to segment the whole stack.

```
use_roi
```
A square ROI of side 256 is created by default for quickly checking adjusting the segmentation parameters. The roi can be resized or moved in the `roi` shapes layer.

```
light_background
```
True; for phase-contrast images.

False; for bright-field and fluorescence images.

```
use_local_noise
```
If checked, this adds noise to image with local variance. In this case, a noise_var of around 0.1 works well. If unchecked, this adds noise with global variance of noise_var/100. Adding may help in removing false positives.

```
gaussian_laplace
```
Useful when segmenting fluorescence images. 

```
adjust_scale
```
Fine-tuning the scale around ([0.8,1.2]) the scale obtained from cell-width determined in `get_cell_width`.

```
noise_var
```
Amount of noise to be added to the image at the preprocessing step. This helps reduce the False Positives and, in many cases, to separate cells effectively. 
```
gamma
```
gamma correction 

```
sharpness_scale and sharpness_amount
```
Unsharp mask based sharpness with sigma = sharpness_scale and amount = sharpness_amount



### segment_stack
Segments the entire stack using the parameters that were obtained in "segment".


### save
The parameters can be saved in a json file. 

## License

Distributed under the terms of the [MIT] license,
"misic-napari" is free and open source software

## Cite
```
@article {10.7554/eLife.65151,
article_type = {journal},
title = {Misic, a general deep learning-based method for the high-throughput cell segmentation of complex bacterial communities},
author = {Panigrahi, Swapnesh and Murat, Dorothée and Le Gall, Antoine and Martineau, Eugénie and Goldlust, Kelly and Fiche, Jean-Bernard and Rombouts, Sara and Nöllmann, Marcelo and Espinosa, Leon and Mignot, Tâm},
editor = {Xiao, Jie and Storz, Gisela and Hensel, Zach},
volume = 10,
year = 2021,
month = {sep},
pub_date = {2021-09-09},
pages = {e65151},
citation = {eLife 2021;10:e65151},
doi = {10.7554/eLife.65151},
url = {https://doi.org/10.7554/eLife.65151},
abstract = {Studies of bacterial communities, biofilms and microbiomes, are multiplying due to their impact on health and ecology. Live imaging of microbial communities requires new tools for the robust identification of bacterial cells in dense and often inter-species populations, sometimes over very large scales. Here, we developed MiSiC, a general deep-learning-based 2D segmentation method that automatically segments single bacteria in complex images of interacting bacterial communities with very little parameter adjustment, independent of the microscopy settings and imaging modality. Using a bacterial predator-prey interaction model, we demonstrate that MiSiC enables the analysis of interspecies interactions, resolving processes at subcellular scales and discriminating between species in millimeter size datasets. The simple implementation of MiSiC and the relatively low need in computing power make its use broadly accessible to fields interested in bacterial interactions and cell biology.},
keywords = {Deep learning, image analysis, microscopy, myxococcus xanthus, biofilms},
journal = {eLife},
issn = {2050-084X},
publisher = {eLife Sciences Publications, Ltd},
}
```
