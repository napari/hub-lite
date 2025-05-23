
[![License BSD-3](https://img.shields.io/pypi/l/napari-correct-drift.svg?color=green)](https://github.com/sommerc/napari-correct-drift/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-correct-drift.svg?color=green)](https://pypi.org/project/napari-correct-drift)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-correct-drift.svg?color=green)](https://python.org)
[![tests](https://github.com/sommerc/napari-correct-drift/workflows/tests/badge.svg)](https://github.com/sommerc/napari-correct-drift/actions)
[![codecov](https://codecov.io/gh/sommerc/napari-correct-drift/branch/main/graph/badge.svg)](https://codecov.io/gh/sommerc/napari-correct-drift)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-correct-drift)](https://napari-hub.org/plugins/napari-correct-drift)
[![Documentation Status](https://readthedocs.org/projects/napari-correct-drift/badge/?version=latest)](https://napari-correct-drift.readthedocs.io/en/latest/?badge=latest)

Napari-correct-drift brings the functionality of Fiji’s popular Correct-3D-drift macro to Napari for flexible and efficient correction of stage and sample drift common in time-lapse microscopy.

Napari-correct-drift supports drift correction for 2D/3D multi-channel data.

----------------------------------
## Example

https://user-images.githubusercontent.com/895863/235100349-83379350-06a5-4fe7-9323-f3e5771cca2e.mp4


## Test data
Napari-correct-drift contains synthetic sample data. To test it on real data download an example Arabidopsis growing [root tip](https://seafile.ist.ac.at/f/b05362d4f358430c8c59/?dl=1) file.

## Installation

You can install `napari-correct-drift` via [pip]:

    pip install napari-correct-drift

To install latest development version :

    pip install git+https://github.com/sommerc/napari-correct-drift.git

## Roadmap

- [x] Basic CorrectDrift interface
- [x] Synthetic test data
- [x] Unit tests
- [x] 2D/3D multi-channel support
- [x] ROI support (rectangles)
- [x] Saving and loading of drift tables
- [x] Outlier handling
- [x] Sphinx documentation
- [x] How-tos
- [x] Tutorials and Guides

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-correct-drift" is free and open source software

### Acknowledgment
This project has been made possible in part by grant number NP2-0000000051 from the napari Plugin Foundations Grants (Cycle 2).
