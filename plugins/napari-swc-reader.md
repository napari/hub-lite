
[![License BSD-3](https://img.shields.io/pypi/l/napari-swc-reader.svg?color=green)](https://github.com/LaboratoryOpticsBiosciences/napari-swc-reader/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-swc-reader.svg?color=green)](https://pypi.org/project/napari-swc-reader)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-swc-reader.svg?color=green)](https://python.org)
[![tests](https://github.com/LaboratoryOpticsBiosciences/napari-swc-reader/workflows/tests/badge.svg)](https://github.com/LaboratoryOpticsBiosciences/napari-swc-reader/actions)
[![codecov](https://codecov.io/gh/LaboratoryOpticsBiosciences/napari-swc-reader/branch/main/graph/badge.svg)](https://codecov.io/gh/LaboratoryOpticsBiosciences/napari-swc-reader)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-swc-reader)](https://napari-hub.org/plugins/napari-swc-reader)

A minimal napari plugin to load swc file to napari viewer.

![image](https://github.com/user-attachments/assets/1c9e5788-0e74-48ab-be0b-0fb74b35192c)


----------------------------------

This [napari] plugin was generated with [copier] using the [napari-plugin-template].

## Features

- Load swc file(s) to napari viewer
- Display swc file(s) in napari viewer as points layers and lines layers
- Size of points and lines are using the radius of the swc file
- You can load an example swc from https://neuromorpho.org/dableFiles/jacobs/CNG%20version/204-2-6nj.CNG.swc or load it under `File` -> `Open Sample` -> `napari-swc-reader`

**Limitations:**
- Only support swc file(s) following specs http://www.neuronland.org/NLMorphologyConverter/MorphologyFormats/SWC/Spec.html 7 columns
- Cannot write swc file(s) to disk but you can access the raw swc data from the napari layers from `metadata` attribute with key `raw_swc`

**Roadmap:**
- Switch to use `napari.layers.Graph` [when it is available](https://github.com/napari/napari/issues/4274)

## Installation

You can install `napari-swc-reader` via [pip]:

    pip install napari-swc-reader


To install latest development version :

    pip install git+https://github.com/LaboratoryOpticsBiosciences/napari-swc-reader.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-swc-reader" is free and open source software

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

[file an issue]: https://github.com/LaboratoryOpticsBiosciences/napari-swc-reader/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
