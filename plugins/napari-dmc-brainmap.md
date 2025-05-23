
# napari-dmc-brainmap
*DMC-BrainMap is an end-to-end tool for multi-feature brain mapping across species.*  
This [napari](https://napari.org/stable/) plugin was generated with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) using napari's [cookiecutter-napari-plugin](https://github.com/napari/cookiecutter-napari-plugin) template.

[![License BSD-3](https://img.shields.io/pypi/l/napari-dmc-brainmap.svg?color=green)](https://github.com/hejDMC/napari-dmc-brainmap/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-dmc-brainmap.svg?color=green)](https://pypi.org/project/napari-dmc-brainmap)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-dmc-brainmap.svg?color=green)](https://python.org)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-dmc-brainmap)](https://napari-hub.org/plugins/napari-dmc-brainmap)


## Quick start
A detailed guide and tutorial can be found on the [Wiki pages of this repo](https://github.com/hejDMC/napari-dmc-brainmap/wiki).

### Installation

DMC-BrainMap is a plugin for [napari](https://napari.org/stable/). Hence, you first need to install napari and subsequently the DMC-BrainMap plugin via the plugin manager. To install napari, we recommend to install napari into a clean virtual environment using *conda* or *venv*. Please refer to the [napari installation guide](https://napari.org/stable/tutorials/fundamentals/installation.html#napari-installation) for more information and [for information on installing napari as a bundled app](https://napari.org/stable/tutorials/fundamentals/installation.html#napari-installation).  

#### Step 1: Setup the virtual environment (Python 3.10)

```
conda create -y -n napari-env -c conda-forge python=3.10
conda activate napari-env
```

#### Step 2: Install napari

```
python -m pip install "napari[all]"
```

#### Step 3: Install napari-dmc-brainmap

You can install `napari-dmc-brainmap` via the napari plugin manager or via [pip](https://pypi.org/project/napari-dmc-brainmap/):

    pip install napari-dmc-brainmap

### Usage

Please refer to the Wiki pages for detailed instructions and a short tutorial on how to use DMC-BrainMap. When working with DMC-BrainMap on your own data, please keep the following points in mind:
- DMC-BrainMap requires single-channel 16-bit .tif/.tiff images to work (in principle 8-bit also work)
- DMC-BrainMap requires that your data is organized by animals in separate folders (you can pool data later down the lane)
- DMC-BrainMap uses 5 channel labels (`dapi`, `green`, `n3`, `cy3`, `cy5`) corresponding to blue, green, orange, red and far red channels. *However, these are only labels, you can assign them as you please. Hence, you can use DMC-BrainMap also for non-fluorescence data given you converted your images to single-channel 16-bit .tif/.tiff images*. Please contact us if you need to use more than 5 channels.
- It is essential that you structure your data in the following way (hierarchical organization, same name for images in different channels, channel labels are selected by you), **otherwise DMC-BrainMap won't work**:
```
animal_id-001
│
└───stitched
│   │
│   └───dapi
│   |    │   animal_id-001_001.tiff
│   |    │   animal_id-001_002.tiff
|   │    |   animal_id-001_003.tiff
│   |    │   animal_id-001_004.tiff
│   |    │   ...
│   │   
│   └───green
│       │   animal_id-001_001.tiff
│       │   animal_id-001_002.tiff
│       │   animal_id-001_003.tiff
│       │   animal_id-001_004.tiff
│       │   ...
│   
animal_id-2
│   ...
```

## Documentation
Documentation on DMC-BrainMap's source code can be found on the project's [Read the Docs page](https://napari-dmc-brainmap.readthedocs.io/en/latest/#).

## Seeking help or contributing

DMC-BrainMap is an open-source project, and we welcome contributions of all kinds. If you have any questions, feedback, or suggestions, please feel free to open an issue on this repository. 

## License

Distributed under the terms of the [BSD-3](https://github.com/teamdigitale/licenses/blob/master/BSD-3-Clause) license,
"napari-dmc-brainmap" is free and open source software

## Citing DMC-BrainMap

If you use DMC-BrainMap in your scientific work, please cite:
```
Jung, F., Cao, X., Heymans, L., Carlén, M. (2025) "DMC-BrainMap - an open-source, end-to-end tool for multi-feature brain mapping across species", bioRxiv, https://doi.org/10.1101/2025.02.19.639009
```

BibTeX:

``` bibtex
@article{Jung2025x,
   author = {Felix Jung and Xiao Cao and Loran Heymans and Marie Carlen},
   doi = {10.1101/2025.02.19.639009},
   journal = {bioRxiv},
   month = {2},
   title = {DMC-BrainMap - an open-source, end-to-end tool for multi-feature brain mapping across species},
   url = {http://biorxiv.org/lookup/doi/10.1101/2025.02.19.639009},
   year = {2025},
}
```

