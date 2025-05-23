
[![License](https://img.shields.io/pypi/l/napari-IP-workflow.svg?color=green)](https://github.com/jayunruh/napari-IP-workflow/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-IP-workflow.svg?color=green)](https://pypi.org/project/napari-IP-workflow)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-IP-workflow.svg?color=green)](https://python.org)
[![tests](https://github.com/jayunruh/napari-IP-workflow/workflows/tests/badge.svg)](https://github.com/jayunruh/napari-IP-workflow/actions)
[![codecov](https://codecov.io/gh/jayunruh/napari-IP-workflow/branch/main/graph/badge.svg)](https://codecov.io/gh/jayunruh/napari-IP-workflow)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-IP-workflow)](https://napari-hub.org/plugins/napari-IP-workflow)

A plugin to do image preprocessing, segmentation, and measurements on other images.  The typical workflow is background subtraction followed by smoothing, thresholding, and size filtering.  This is typically done on nuclear stained images.  Segmentation can optionally be followed by circular label expansion to find cytoplasmic signals. The labeled signals are then measured on background subtracted images.

##General organization

The code is separated into non-interactive processing functions (ipfunctions module) and an interactive widget (segwidget module).  Please look at the code on github for examples: [Github](https://github.com/jayunruh/napari-ip-workflow). The expected workflow is from jupyter notebooks with an interactive workflow shown in src/napari-ip-workflow/_tests/standard_segementation_widget.ipynb and a non-interactive workflow shown in src/napari-ip-workflow/_tests/standard_segmentation.ipynb.  The expectation is to find the best parameters in an interactive way (ideally testing on several images) and then use the non-interactive workflow to batch through more data sets.  All image processing algorithms are in the ipfunctions module and the segwidget module has the Napari widget code.  Below I describe the strategies that are utilized in the workflow.

## Background subtraction strategy

Automated background subtraction (e.g. as in Fiji) is often accomplished with a low pass filter-style approach like rolling ball background subtraction.  This approach fails as feature sizes grow larger or measurements approach the background.  Manual selection of the background is more robust but introduces human variability and isn't compatible with high throughput analyses.  Our approach is to attempt to automate regional selection of background as follows.  First the image is smoothed with a Gaussian filter to eliminate background noise.  Next, minimum values are subtracted from each channel and the resulting images are summed.   Next, a uniform 2D boxcar smoothing is applied to the image--background level regions in the resulting image are at least the boxcar size distance away from foreground objects.  The minimum pixel in that resulting image is a good approximation for the background region of the image.  A thick border is specified to avoid lower intensity regions at the border of the image.  This algorithm is implemented in the ipfunctions module as findBackground.  Once the background region is found, it can be measured with measureCirc.

## Segmentation and thresholding strategy

There are many automated thresholding algorithms available via python and, by extension, Napari.  This program uses a very simplistic but powerful method.  Most segmentable images consist of foreground and background components.  In imaging, the foreground is more noisy than the background.  Ideally a smoothed background subtracted image will have a maximum intensity that represents the foreground well and a background intensity of 0.  In that case, the threshold level can be easily defined as a fraction of that smoothed maximum intensity.  A threshold fraction of 0.25 tends to work well but lower values may be more robust if background is fairly smooth and the foreground is noisier.  In some cases the foreground has anomalous high values that will skew the estimation.  In that case it may be better to estimate the foreground as e.g. the 99th percentile of the intensity.  In some cases it may be useful to use the average intensity as a reference point instead or use the raw intensity value (statistic is Identity).  Those last options tend to be less robust and it may be desired in those cases to use some of the more complex autothresholding methods.  After thresholding, objects on the image edge are eliminated and objects are filtered according to size.  The minimum area can easy remove small debris that can contaminate a measurement.  The maximum area can be used for large contaminants or poorly segmented clusters of cells that might not be desired in the analysis.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->

## Installation

You can install `napari-IP-workflow` via [pip]:

    pip install napari-IP-workflow



To install latest development version :

    pip install git+https://github.com/jayunruh/napari-IP-workflow.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [GNU GPL v3.0] license,
"napari-IP-workflow" is free and open source software

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

[file an issue]: https://github.com/jayunruh/napari-IP-workflow/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
