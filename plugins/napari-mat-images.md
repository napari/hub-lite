
[![PyPI version](https://img.shields.io/pypi/v/napari-mat-images.svg)](https://pypi.org/project/napari-mat-images)

[![Python versions](https://img.shields.io/pypi/pyversions/napari-mat-images.svg)](https://pypi.org/project/napari-mat-images)

[![See Build Status on Azure Pipelines](https://dev.azure.com/hectormz-1/napari-mat-images/_apis/build/status/hectormz.napari-mat-images?branchName=main)](https://dev.azure.com/hectormz-1/napari-mat-images/_build/latest?definitionId=1&branchName=main)

## Features

This plugin loads image variables stored in `MATLAB` `.mat` files into [napari](https://github.com/napari/napari).

It loads any variable that looks like an image.
Presently, that includes any array with more than two dimensions with size greater than 20 pixels (determined by `shape_is_image()`).

If loading a variable with 3 or more dimensions, the plugin assumes that it is a stack of images, and the dimension with greatest size is the axis of the stack.

### Loading Large Files

If loading a large `.mat` file saved in `HDF5`/`v7.3` format, chunks of the images are loaded as needed, resulting in fast initial load, but potentially slower scrolling.

Slices of the image stacks are randomly sampled to determine min/max contrast values.

## Requirements

This plugin relies on `scipy` to load small `.mat` files and `h5py` (with `dask`) to load larger `HDF5`/`v7.3` `.mat` files.

It implicitly requires `napari` for use.

## Installation

`napari-mat-images` requires [napari](https://github.com/napari/napari) to be installed, although it is not listed as a requirement for installation.
This plugin relies on plugin functionality found in `napari` version \> `0.2.12`. This can be installed via [pip](https://pypi.org/project/pip/) from [PyPI](https://pypi.org/project):

    $ pip install napari>0.2.12

You can install `napari-mat-images` via [pip](https://pypi.org/project/pip/) from [PyPI](https://pypi.org/project):

    $ pip install napari-mat-images

## Usage

Once installed, the plugin will be used whenever trying to load a `.mat` file.
This can be done from the `napari` GUI or commandline:

    $ napari my_file.mat

## Contributing

Contributions are very welcome.
Tests can be run with [pytest](https://docs.pytest.org/en/latest/),
please ensure the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3](http://opensource.org/licenses/BSD-3-Clause) license, `napari-mat-images` is free and open source software

## Issues

If you encounter any problems, please [file an issue](https://github.com/hectormz/napari-mat-images/issues) along with a detailed description.

---

This [napari](https://github.com/napari/napari) plugin was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with [napari](https://github.com/napari/napari)\'s [cookiecutter-napari-plugin](https://github.com/napari/cookiecutter-napari-plugin) template.


