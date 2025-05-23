
[![License BSD-3](https://img.shields.io/pypi/l/napari-power-widgets.svg?color=green)](https://github.com/hanjinliu/napari-power-widgets/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-power-widgets.svg?color=green)](https://pypi.org/project/napari-power-widgets)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-power-widgets.svg?color=green)](https://python.org)
[![tests](https://github.com/hanjinliu/napari-power-widgets/workflows/tests/badge.svg)](https://github.com/hanjinliu/napari-power-widgets/actions)
[![codecov](https://codecov.io/gh/hanjinliu/napari-power-widgets/branch/main/graph/badge.svg)](https://codecov.io/gh/hanjinliu/napari-power-widgets)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-power-widgets)](https://napari-hub.org/plugins/napari-power-widgets)

Powerful `magicgui` widgets and type annotations for general-purpose napari plugin development.

`napari-power-widgets` makes the full use of type-to-widget mapping strategy of `magicgui` to provide napari-specific types and value-widgets, which will be very useful to improve UI/UX of your napari plugins with simple codes.

Currently, `napari-power-widgets` does not provide any reader, writer or widget. It is supposed to be used programmatically.

### Examples

Some types/widgets and the possible usage are picked up here ([&rarr; check all](https://github.com/hanjinliu/napari-power-widgets/blob/main/src/napari_power_widgets/types.py)). If you have any neat ideas, please open an issue.

#### 1. `BoxSelection`

Alias of a four-float tuple for 2D selection. You can set the value by drawing a interaction box in the viewer.

*e. g. : image cropper, rectangular labeling etc.*

```python
@magicgui
def f(box: BoxSelection):
    print(box)
viewer.window.add_dock_widget(f)
```

![](images/BoxSelection.gif)

#### 2. `OneOfRectangles`

Alias of `np.ndarray` for one of rectangles in a `Shapes` layer.

*e. g. : image cropper, rectangular labeling etc.*

```python
@magicgui
def f(rect: OneOfRectangles):
    print(rect)
viewer.window.add_dock_widget(f)
```

![](images/OneOfRectangles.gif)

#### 3. `LineData`

Alias of `np.ndarray` for a line data. You can obtain the data by manually drawing a line in the viewer.

*e. g. : line profiling, kymograph etc.*

```python
@magicgui
def f(line: LineData):
    print(line)
viewer.window.add_dock_widget(f)
```

![](images/LineData.gif)

#### 4. `OneOfLabels`

Alias of boolean `np.ndarray` for a labeled region. You can choose ones by directly clicking the viewer.

*e. g. : image masking, feature measurement etc.*

```python
@magicgui
def f(label: OneOfLabels):
    pass
viewer.window.add_dock_widget(f)
```

![](images/OneOfLabels.gif)


#### 5. `ZRange`

Alias of a tuple of float that represents the limit of the third dimension. You can select the values by moving the dimension slider.

*e. g. : movie trimming, partial image projection etc.*

```python
@magicgui
def f(zrange: ZRange):
    print(zrange)
viewer.window.add_dock_widget(f)
```

![](images/ZRange.gif)

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-power-widgets` via [pip]:

    pip install napari-power-widgets



To install latest development version :

    pip install git+https://github.com/hanjinliu/napari-power-widgets.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-power-widgets" is free and open source software

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

[file an issue]: https://github.com/hanjinliu/napari-power-widgets/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
