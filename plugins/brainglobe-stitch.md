
Stitching tiled 3D light-sheet data in napari

<p align="center">
  <img height="460" src="https://github.com/user-attachments/assets/91f61f24-6fcf-4aa1-8a8f-de8c5e3db4a2" alt="Stitching a mouse brain acquired at a resolution of 4.06 &micro;m/px, 4.06 &micro;m/px, 5 &micro;m/px using 4 tiles">
</p>

----------------------------------

A [napari] plugin for stitching tiled 3D acquisitions from a [mesoSPIM] light-sheet microscope.
The plugin utilises [BigStitcher] to align the tiles and napari to visualise the stitched data.

## Installation

We strongly recommend to use a virtual environment manager (like `conda`). The installation instructions below
will not specify the Qt backend for napari, and you will therefore need to install that separately. Please see the
[`napari` installation instructions](https://napari.org/stable/tutorials/fundamentals/installation.html) for further advice on this.

To install latest development version:

    pip install git+https://github.com/brainglobe/brainglobe-stitch.git

This plugin requires Fiji to be installed on your system. You can download Fiji [here](https://imagej.net/Fiji/Downloads).

The BigStitcher plugin must be installed in Fiji. Please follow the instructions [here](https://imagej.net/plugins/bigstitcher/#download).

## Seeking help or contributing
We are always happy to help users of our tools, and welcome any contributions. If you would like to get in contact with us for any reason, please see the [contact page of our website](https://brainglobe.info/contact.html).

## Citation
If you find this package useful, please make sure to cite the original BigStitcher publication:
> Hörl, D., Rojas Rusak, F., Preusser, F. *et al.* BigStitcher: reconstructing high-resolution image datasets of cleared and expanded samples. Nat Methods 16, 870–874 (2019). https://doi.org/10.1038/s41592-019-0501-0


## License
Distributed under the terms of the [BSD-3] license,
"brainglobe-stitch" is free and open source software

## Acknowledgements
This [napari] plugin was generated with [Cookiecutter] using napari's [cookiecutter-napari-plugin] template and the [Neuroinformatics Unit's template](https://github.com/neuroinformatics-unit/python-cookiecutter).

[napari]: https://napari.org
[mesoSPIM]: https://www.mesospim.org/
[BigStitcher]: https://imagej.net/BigStitcher
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
