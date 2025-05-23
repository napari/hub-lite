
[![License BSD-3](https://img.shields.io/pypi/l/napari-himena.svg?color=green)](https://github.com/hanjinliu/napari-himena/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-himena.svg?color=green)](https://pypi.org/project/napari-himena)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-himena.svg?color=green)](https://python.org)
[![tests](https://github.com/hanjinliu/napari-himena/workflows/tests/badge.svg)](https://github.com/hanjinliu/napari-himena/actions)
[![codecov](https://codecov.io/gh/hanjinliu/napari-himena/branch/main/graph/badge.svg)](https://codecov.io/gh/hanjinliu/napari-himena)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-himena)](https://napari-hub.org/plugins/napari-himena)
[![npe2](https://img.shields.io/badge/plugin-npe2-blue?link=https://napari.org/stable/plugins/index.html)](https://napari.org/stable/plugins/index.html)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)

Pipeline between [`napari`](https://github.com/napari/napari) and [`himena`](https://github.com/hanjinliu/himena).

`napari` is a great tool for visualization, annotation and analysis of multi-dimensional
images. On the other hand, `himena` has a powerful plugin system that allows users to
technically do anything, such as editing table and plotting.

`napari-himena` connects these two ecosystems together, enabling users to send data
back and forth, extending the functionality of the both packages.

## Examples

#### 1. Sending image layers to `himena` for ImageJ-like multi-measurement and Excel-like plotting.

Measuring time-course change in the image intensity with [`himena-image`](https://github.com/hanjinliu/himena-image) plugin, and plot the result using the built-in plot functions using `matplotlib`.

![](https://github.com/hanjinliu/napari-himena/blob/main/assets/image-plot.gif)

#### 2. Sending points and their features to `himena` for seaborn plotting.

Feature dataframe can be directly sent to `himena` for `seaborn` plotting using [`himena-seaborn`](https://github.com/hanjinliu/himena-seaborn) plugin.

![](https://github.com/hanjinliu/napari-himena/blob/main/assets/feature-sns.gif)

## Usage

#### Starting from `napari`

Open the `napari-himena` dock widget from the "Plugin" menu, connect to one of the
`himena` profile (only "default" is available by default), and that's it!

![](https://github.com/hanjinliu/napari-himena/blob/main/assets/from-napari.png)

#### Starting from `himena`

To use this plugin from `himena`, you need to first register this plugin to the `himena`
profile

```shell
# install to the default profile
himena --install napari-himena

# or install to a specific profile
himena <my-profile> --install napari-himena
```

Then all the commands will be available in `himena` and a napari viewer will be launched
when it is needed. You don't need to do this if you always launch `himena` from `napari`
plugin; it automatically register this package in the beginning.

![](https://github.com/hanjinliu/napari-himena/blob/main/assets/from-himena.png)

----------------------------------

This [napari] plugin was generated with [copier] using the [napari-plugin-template].

## Installation

You can install `napari-himena` via [pip]:

    pip install napari-himena



To install latest development version :

    pip install git+https://github.com/hanjinliu/napari-himena.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-himena" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[copier]: https://copier.readthedocs.io/en/stable/
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[napari-plugin-template]: https://github.com/napari/napari-plugin-template

[file an issue]: https://github.com/hanjinliu/napari-himena/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
