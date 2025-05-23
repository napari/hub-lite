
[![License BSD-3](https://img.shields.io/pypi/l/napari-caphid.svg?color=green)](https://github.com/hereariim/napari-caphid/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-caphid.svg?color=green)](https://pypi.org/project/napari-caphid)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-caphid.svg?color=green)](https://python.org)
[![tests](https://github.com/hereariim/napari-caphid/workflows/tests/badge.svg)](https://github.com/hereariim/napari-caphid/actions)
[![codecov](https://codecov.io/gh/hereariim/napari-caphid/branch/main/graph/badge.svg)](https://codecov.io/gh/hereariim/napari-caphid)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-caphid)](https://napari-hub.org/plugins/napari-caphid)

Annotation of aphid and update table

----------------------------------

Napari-caphid was developed for updating table of quantitative data from images. Napari-caphid was developed by Imhorphen Team (french team of University of Angers and INRAe Angers) for ECLECTIC Team (french team of University of Paris-Saclay and CNRS).

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-caphid` via [pip]:

    pip install napari-caphid



To install latest development version :

    pip install git+https://github.com/hereariim/napari-caphid.git

## Getting started

### Foreword

Before using the plugin, the directory must be structured as follows:

```
└── Directory
    ├── France
    │   ├── image
    │   │   ├── img_1.tif
    │   │   ├── img_2.tif
    │   │   ...
    │   │   └── img_n.tif
    │   ├── mask
    │   │   ├── msk_1.tif
    │   │   ├── msk_2.tif
    │   │   ...
    │   │   └── msk_n.tif
    │   ├── img_1.tif
    │   ├── msk_1.tif
    │   ├── img_2.tif
    │   ├── msk_2.tif
    │   ...
    │   ├── img_n.tif
    │   └── msk_n.tif
    │ 
    ├── Belgium
    │   ├── image
    │   │   └── ...
    │   ├── mask
    │   │   └── ...
    │   └── ...
    ├── Spain
    │   ├── image
    │   │   └── ...
    │   ├── mask
    │   │   └── ...
    │   └── ...
    └── Aphid.csv
```

Some explanation about structure. The directory contained three folders (France, Spain, Belgium) and one file (Aphid.csv).
- Each folders (France, Spain, Belgium) contains a set of images and masks and two folders (image, mask). The folder image contains images from the set of images. The folder mask contains masks from the set of masks.
- The file Aphid.csv is a table with quantitative data of aphids from inital process of aphid image processing.

Important:
- The structure of directory is very important because it will be useful to get image name.

### Getting started

The widget get three input:
- Mask : Mask stack
- Pick a table : Path/to/Directory/Aphid.csv
- Country : The country where images were taken

The widget gives one output:
- A new table .csv which is the Aphid.csv updated.

### What's it for ?

This widget gives quantitative data from Mask stack. These quantitative data will be contained into dataframe. Quantitative data linked to current masks contained in the Aphid.csv file will be deleted. Then, the new quantitative data contained in the dataframe will be integrated into the Aphid.csv file. In this way, the Aphid.csv file is updated.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-caphid" is free and open source software

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

[file an issue]: https://github.com/hereariim/napari-caphid/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
