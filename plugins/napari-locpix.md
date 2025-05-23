
[![License MIT](https://img.shields.io/pypi/l/napari-locpix.svg?color=green)](https://github.com/oubino/napari-locpix/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-locpix.svg?color=green)](https://pypi.org/project/napari-locpix)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-locpix.svg?color=green)](https://python.org)
[![tests](https://github.com/oubino/napari-locpix/workflows/tests/badge.svg)](https://github.com/oubino/napari-locpix/actions)
[![codecov](https://codecov.io/gh/oubino/napari-locpix/branch/main/graph/badge.svg)](https://codecov.io/gh/oubino/napari-locpix)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-locpix)](https://napari-hub.org/plugins/napari-locpix)

Load in SMLM data and annotate within napari

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-locpix` via [pip]:

    pip install napari-locpix


To install latest development version :

    pip install git+https://github.com/oubino/napari-locpix.git


## Usage

This plugin allows a user to

1. Read in SMLM data
2. Visualise SMLM data in a histogram
3. Add segmentations to the data
4. Extract the underlying localisations from the segmentations

### IO

The input data can be in the form of a .csv or .parquet.

We expect there to be 4 columns at least, which should he identified inthe file column selection:

* X coordinate
* Y coordinate
* Frame
* Channel

If the data has been annotated with this software we can also load this in.
Note however we currently only support loading in annotated data saved as a .parquet folder.
Therefore, we recommend always keeping a .parquet copy until loading in an annotated .csv
is supported.

The data can be outputted to a .parquet or a .csv

Drop localisations with zero label, gives you the option to only save the localisations which have been annotated i.e. labels 1 and above.

Channels labels allows you to give a real name label to each of the channels e.g. Chan 0 label: 'Alexa 647'

### Visualisation

Using the render button you can render the loaded in data according to the histogram settings

X/Y bins defines the number of bins for the histogram

Vis interpolation defines how to interpolate the image before viewing

### Annotations

Annotations can be added using Napari's viewer.

Simply click the add Labels.

Note that this software will expect the labels to be called "Labels"

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-locpix" is free and open source software

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

[file an issue]: https://github.com/oubino/napari-locpix/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
