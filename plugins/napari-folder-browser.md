
[![License](https://img.shields.io/pypi/l/napari-folder-browser.svg?color=green)](https://github.com/haesleinhuepf/napari-folder-browser/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-folder-browser.svg?color=green)](https://pypi.org/project/napari-folder-browser)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-folder-browser.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/napari-folder-browser/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/napari-folder-browser/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/napari-folder-browser/branch/master/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/napari-folder-browser)

Browse folders of images and open them using double-click or <ENTER>. You can also navigate through the list using arrow up/down keys.

![](https://github.com/haesleinhuepf/napari-folder-browser/raw/main/docs/napari-folder-browser.gif)

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

## Installation

You can install `napari-folder-browser` from within napari by clicking menu `Plugins > Install/uninstall Plugins...` and entering here:
![img.png](https://github.com/haesleinhuepf/napari-folder-browser/raw/main/docs/install.png)

You can install `napari-folder-browser` via [pip]:

    pip install napari-folder-browser

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## Development
### Test the plugin in Napari
Simply use pip install and run napari to test the plugin in the same environment:
```bash
pip install -e .
napari
```

### Conda
If you prefer to use conda, you can create a new environment with the following command:
```bash
conda env create -f environment.yml
conda activate napari-folder-browser
```

## License

Distributed under the terms of the [BSD-3] license,
"napari-folder-browser" is free and open source software

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

[file an issue]: https://github.com/haesleinhuepf/napari-folder-browser/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[image.sc]: https://image.sc
[@haesleinhuepf]: https://twitter.com/haesleinhuepf

