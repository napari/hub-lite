
[![License BSD-3](https://img.shields.io/pypi/l/epicure.svg?color=green)](https://gitlab.pasteur.fr/gletort/epicure/-/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/epicure.svg?color=green)](https://pypi.org/project/epicure)
[![Python Version](https://img.shields.io/pypi/pyversions/epicure.svg?color=green)](https://python.org)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/epicure)](https://napari-hub.org/plugins/epicure)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13952184.svg)](https://doi.org/10.5281/zenodo.13952184)

![EpiCure logo](https://gitlab.pasteur.fr/gletort/epicure/-/raw/main/imgs/epicure_logo.png?raw=True "EpiCure logo")

**Napari plugin to ease manual correction of epithelia segmentation in movies.**

To analyse individual cell trajectory from epithelia movies marked for cell-cell junctions, a very precise segmentation and tracking is required.
Several tools such as TissuAnalyzer, Epyseg, CellPose or Dist2Net perform very good segmentation (~5% of errors). 
However, this still implies a high amount of cells to correct manually. 
EpiCure allows to decrease the burden of this task. 
Several features are proposed to ease the manual correction of the segmented movies, such as error detection, numerous shortcuts for editing the segmentation, option for tracking, display and measure/export options.
EpiCure detect segmentation errors by taking advantage of temporal information. 
When a correction is done at a given frame, EpiCure relink the track to adjust for the changes.


 > **Documentation in the [wiki](https://gitlab.pasteur.fr/gletort/epicure/-/wikis/Home)**

<p align="center">
![EpiCure interface](https://gitlab.pasteur.fr/gletort/epicure/-/raw/main/imgs/EpiGen.png?raw=True "EpiCure interface")
</p>

## Installation

### Install plugin
To install EpiCure on a fresh python virtual environment, type inside the environement:
```
pip install epicure
``` 

Then launch `Napari`, and the plugin should be visible in the `Plugins` list.

If you already have an environment with `Napari` installed, you can also install it directly in `Napari>Plugins>Install/Uninstall plugins`

### Install code
To have the code to be able to modify it, clone this repository. You can use `pip install -e .` so that everytime you update the code, the plugin will be updated. 

## Dependencies

The input files of EpiCure can be already tracked or not.
Tracking options are proposed in EpiCure:
* Laptrack centroids
* Laptrack overlaps

## Usage
Refer to the [wiki](https://gitlab.pasteur.fr/gletort/epicure/-/wikis/Home) for documentation of the different steps possible in the pipeline.

## References

If you use EpiCure, thank you for citing our work: 

EpiCure is not published yet, you can cite it using Zenodo for now: https://doi.org/10.5281/zenodo.13952184


## Issues
Issues have been disactivated to avoid spammed issues. To report an issue or ask for development, please contact us directly by email.


This [napari] plugin was initialized with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[file an issue]: https://github.com/gletort/epicure/issues
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
