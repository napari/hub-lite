
[![License BSD-3](https://img.shields.io/pypi/l/napari-segselect.svg?color=green)](https://github.com/bwmr/napari-segselect/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-segselect.svg?color=green)](https://pypi.org/project/napari-segselect)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-segselect.svg?color=green)](https://python.org)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-segselect)](https://napari-hub.org/plugins/napari-segselect)

Select a connected component from a [membrain-seg](https://github.com/teamtomo/membrain-seg) segmentation.

## Usage

1. Run `membrain-seg` with the `--store-connected-components` flag (optional, otherwise connected components will be calculated while opening)
2. Open the segmentation in Napari, find out which component numbers correspond to your feature.
    ![Label Layer](images/image2.png)
3. Enter these numbers and a feature name in the widget, press run. 
    ![Widget](images/image3.png)
4. Save the resulting layer using naparis built-in dialog. 
5. Now you have a standalone binary segmentation of your feature of interest.
    ![Output](images/image4.png)


## Installation

You can install `napari-segselect` via [pip]:

    pip install napari-segselect
   
Or directly from GitHub:

    pip install git+https://github.com/bwmr/napari-segselect.git


## License

Distributed under the terms of the [BSD-3] license,
"napari-segselect" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

This [napari] plugin was generated with [copier] using the [napari-plugin-template].


[napari]: https://github.com/napari/napari
[copier]: https://copier.readthedocs.io/en/stable/
[@napari]: https://github.com/napari
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[napari-plugin-template]: https://github.com/napari/napari-plugin-template

[file an issue]: https://github.com/bwmr/napari-segselect/issues

[napari]: https://github.com/napari/napari
[pip]: https://pypi.org/project/pip/
