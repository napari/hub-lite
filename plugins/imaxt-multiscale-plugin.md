
[![License GNU LGPL v3.0](https://img.shields.io/pypi/l/imaxt-multiscale-plugin.svg?color=green)](https://github.com/eg266/imaxt-multiscale-plugin/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/imaxt-multiscale-plugin.svg?color=green)](https://pypi.org/project/imaxt-multiscale-plugin)
[![Python Version](https://img.shields.io/pypi/pyversions/imaxt-multiscale-plugin.svg?color=green)](https://python.org)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/imaxt-multiscale-plugin)](https://napari-hub.org/plugins/imaxt-multiscale-plugin)

A napari plugin to visualize multi-resolution images created with the IMAXT mosaic pipeline.

----------------------------------------------------

## Installation

You can install `imaxt-multiscale-plugin` via [pip]:

    pip install imaxt-multiscale-plugin


## Usage

Run [napari] with the name of the sample to visualize either a local path:

    napari /storage/imaxt/eglez/processed/stpt/20220606_PDX_AB559_GFP_005503_100x15um

or a sample in S3 storage:

    napari s3://imaxtgw/stpt/20220608_DI_PDX_SA535_Tum_5223_04280_100x15um
    
## Screenshots

![Alt text](https://gitlab.developers.cam.ac.uk/astronomy/camcead/imaxt/imaxt-multiscale-plugin/-/raw/main/assets/napari1.png "a title")
![Alt text](https://gitlab.developers.cam.ac.uk/astronomy/camcead/imaxt/imaxt-multiscale-plugin/-/raw/main/assets/napari2.png "a title")
![Alt text](https://gitlab.developers.cam.ac.uk/astronomy/camcead/imaxt/imaxt-multiscale-plugin/-/raw/main/assets/napari3.png "a title")
![Alt text](https://gitlab.developers.cam.ac.uk/astronomy/camcead/imaxt/imaxt-multiscale-plugin/-/raw/main/assets/napari4.png "a title")

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [GNU LGPL v3.0] license,
"imaxt-multiscale-plugin" is free and open source software

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

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
