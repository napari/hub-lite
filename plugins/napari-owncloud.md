
[![License](https://img.shields.io/pypi/l/napari-owncloud.svg?color=green)](https://github.com/haesleinhuepf/napari-owncloud/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-owncloud.svg?color=green)](https://pypi.org/project/napari-owncloud)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-owncloud.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/napari-owncloud/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/napari-owncloud/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/napari-owncloud/branch/master/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/napari-owncloud)

## Usage

Browse folders and images in [owncloud](https://owncloud.com/) / [nextcloud](https://nextcloud.com/) servers and open them using just a double-click! 

Login to an owncloud or nextcloud server by clicking the menu `Tools > Utilities > Browse owncloud / nextcloud storage`

![](https://github.com/haesleinhuepf/napari-owncloud/raw/main/docs/login.png)

You can then navigate through folders by double-clicking `folder/` items in the list.
You can also open images by double-clicking them. Alternatively, use the arrow-up and arrow-down key to navigate the list and hit ENTER to open an image or folder.

![](https://github.com/haesleinhuepf/napari-owncloud/raw/main/docs/browse.png)

Store images in your cloud storage using the button `Save / upload current layer`. Note: Currently, only single selected layers can be saved.

![](https://github.com/haesleinhuepf/napari-owncloud/raw/main/docs/upload.png)

[Demo](https://github.com/haesleinhuepf/napari-owncloud/raw/main/docs/demo.mp4)

![](https://github.com/haesleinhuepf/napari-owncloud/raw/main/docs/demo.gif)

## Installation

You can install `napari-owncloud` via [pip]:

    pip install napari-owncloud

## Related plugins

There are other napari plugins that allow you browsing local and online image storage
* [napari-omero](https://www.napari-hub.org/plugins/napari-omero)
* [napari-folder-browser](https://www.napari-hub.org/plugins/napari-folder-browser)

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-owncloud" is free and open source software

## Issues

If you encounter any problems, please create a thread on [image.sc] along with a detailed description and tag [@haesleinhuepf].

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

[file an issue]: https://github.com/haesleinhuepf/napari-owncloud/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[image.sc]: https://image.sc
[@haesleinhuepf]: https://twitter.com/haesleinhuepf

