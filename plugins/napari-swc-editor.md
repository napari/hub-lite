
[![License BSD-3](https://img.shields.io/pypi/l/napari-swc-editor.svg?color=green)](https://github.com/LaboratoryOpticsBiosciences/napari-swc-editor/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-swc-editor.svg?color=green)](https://pypi.org/project/napari-swc-editor)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-swc-editor.svg?color=green)](https://python.org)
[![tests](https://github.com/LaboratoryOpticsBiosciences/napari-swc-editor/workflows/tests/badge.svg)](https://github.com/LaboratoryOpticsBiosciences/napari-swc-editor/actions)
[![codecov](https://codecov.io/gh/LaboratoryOpticsBiosciences/napari-swc-editor/branch/main/graph/badge.svg)](https://codecov.io/gh/LaboratoryOpticsBiosciences/napari-swc-editor)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-swc-editor)](https://napari-hub.org/plugins/napari-swc-editor)

Use point and shape layer to edit swc format in napari.

----------------------------------

This [napari] plugin was generated with [copier] using the [napari-plugin-template].

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/napari-plugin-template#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Features


https://github.com/user-attachments/assets/cba1820f-d0b5-436c-a981-62bae0e1a6ba




### IO
#### READER
- Your .swc should follow the following specs: http://www.neuronland.org/NLMorphologyConverter/MorphologyFormats/SWC/Spec.html
- the reader will create 2 napari layer: `point_layer` and `shape_layer`. Only `point_layer` is interactive, `shape_layer` is used to render path between swc points.
- The raw swc can be accessed in the point layer metadata. Such as `point_layer.metadata["raw_swc"]`
- A `pd.DataFrame` object is also saved in the metadata: `point_layer.metadata["swc_data"]`
#### WRITER
- With the `point_layer` selected, you can use napari interface to save with `.swc` extension name.
- You can also do it in command line: `napari.save_layers('test.swc', [point_layer])`
### Napari Interface
#### Structure ID and point symbol
In swc, structure id allow to label the type of neuron structure the point belongs to. In this plugin by default, the points will follow this symbol mapping:
```python
SWC_SYMBOL = {
    0: "clobber",  # undefined
    1: "star",  # soma
    2: "disc",  # axon
    3: "triangle_down",  # basal dendrite
    4: "triangle_up",  # apical dendrite
}
```
![image](https://github.com/user-attachments/assets/618aa000-370d-43f9-8645-8a3b7e9b9739)

You can also visualize the swc data in a table using the widget under `Plugin > SWC Editor Widget`

![image](https://github.com/user-attachments/assets/ed43f4c2-582b-4bc1-bbb1-54e8d9487f1d)

When using the "Show swc table" you will have an interactive table widget:
- left-click on table: highlight + center on the corresponding point
- **double**-left-click on table: highlight + center on the correspongind point **+ zoom**
- selection on the point layer: highlight the corresponding row on the table

#### SWC Edition
**ALL INTERACTIONS ARE ONLY BOUND TO THE `point_layer`**
**THERE IS NO CTRL-Z (please save your progress)**
- **Add point**: You can edit the "r" and the "structure_id" using the `point_size` and `symbol` ![image](https://github.com/user-attachments/assets/44255691-ffa0-4f63-8368-499b0c8ff6a4)
- **Remove point**: (Select the point and press `1` or `suppr` or `delete`) All the link pointing to this point will be removed
- **Add edge**: Select 2 or more point(s) and press on your keyboard `l` (aka: link).
- **Remove edge**: Select 1 or more point(s) and press on your keyboard `u` (aka: unlink).

If you want to link point as you are adding them you have two solutions:
- press "CTRL" while you add points, this will create a link with the previously selected point
- use the `Plugin > SWC Editor Widget` Checkbox ("link previous node with new node (same as using CTRL+Click)"): when selected, all new points will be selected with the previously selected point

https://github.com/user-attachments/assets/273f1221-2882-4a7c-ab7f-6d3ecb7f3fa6

## Installation

You can install `napari-swc-editor` via [pip]:

    pip install napari-swc-editor







To install latest development version :

    pip install git+https://github.com/LaboratoryOpticsBiosciences/napari-swc-editor.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-swc-editor" is free and open source software

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

[file an issue]: https://github.com/LaboratoryOpticsBiosciences/napari-swc-editor/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
