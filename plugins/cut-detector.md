
[![License BSD-3](https://img.shields.io/pypi/l/cut-detector.svg?color=green)](https://github.com/15bonte/cut-detector/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/cut-detector.svg?color=green)](https://pypi.org/project/cut-detector)
[![Python Version](https://img.shields.io/pypi/pyversions/cut-detector.svg?color=green)](https://python.org)
[![tests](https://github.com/15bonte/cut-detector/workflows/tests/badge.svg)](https://github.com/15bonte/cut-detector/actions)
[![codecov](https://codecov.io/gh/15bonte/cut-detector/branch/main/graph/badge.svg)](https://codecov.io/gh/15bonte/cut-detector)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/cut-detector)](https://napari-hub.org/plugins/cut-detector)

Automatic micro-tubule cut detector.

https://github.com/user-attachments/assets/2af2e1a6-adf9-4d63-a353-e190c4814d83

---

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

<video width="640" height="480" controls>
  <source src="https://github.com/15bonte/cut-detector-models/blob/main/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Installation

### Conda environment

It is highly recommended to create a dedicated conda environment, by following these few steps:

1. Install an [Anaconda] distribution of Python. Note you might need to use an anaconda prompt if you did not add anaconda to the path.

2. Open an Anaconda prompt as admin to create a new environment using [conda]. We advice to use python 3.10 and conda 23.10.0, to get conda-libmamba-solver as default solver.

```bash
conda create --name cut_detector python=3.10 conda=23.10.0
conda activate cut_detector
```

### Package installation

Once in a dedicated environment, our package can be installed via [pip]:

```bash
pip install cut_detector
```

Alternatively, you can clone the github repo to access to playground scripts.

```bash
git clone https://github.com/15bonte/cut-detector.git
cd cut-detector
pip install -e .
```

### GPU

We highly recommend to use GPU to speed up segmentation. To use your NVIDIA GPU, the first step is to download the dedicated driver from [NVIDIA].

Next we need to remove the CPU version of torch:

```bash
pip uninstall torch
```

The GPU version of torch to be installed can be found [here](https://pytorch.org/get-started/locally/). You may choose the CUDA version supported by your GPU, and install it with conda. This package has been developed with the version 11.6, installed with this command:

```bash
conda install pytorch==1.12.1 torchvision pytorch-cuda=11.6 -c pytorch -c nvidia
```

## Update

To update cut-detector to the latest version, open an Anaconda prompt and use the following commands:

```bash
conda activate cut_detector
pip install cut-detector --upgrade
```

## Definitions

Each detected cell division is labeled with one of the following categories:

- NORMAL: Division happening as expected, where (at least) 1 micro-tubule cut is detected.
- NO_MID_BODY_DETECTED: Along the cell division, no mid-body was detected on the MKLP1 channel. This category encompasses different cases: the detection may have failed, the mid-body may not express the fluorescence, or this may not actually be a division.
- MORE_THAN_TWO_DAUGHTER_TRACKS: Tripolar division. This category encompasses both actual tripolar divisions and wrong identifications of daughter cells (mainly caused by segmentation issues).
- NEAR_BORDER: Division close to the border of the image, hence ignored as it is likely to be difficult to detect micro-tubule cuts. A division is classified as NEAR_BORDER as soon as the distance between 1 detected mid-body and the border of the image is less than 20px.
- NO_CUT_DETECTED: Division whose mid-body was detected, but with all micro-tubule bridges classified as "No cut". Likely to be at the end of the video, cells dying before the end of division, or cells going out of frame.
- TOO_SHORT_CUT: First micro-tubule cut detected before or at 50 minutes. Ignored as this is very unlikely, so it is probably caused by a wrong division detection.

Division movies start at the maximum between:

- Mother cell start frame
- 10 frames before the end of metaphase

Division movies end at the minimum between:

- Last frame of any of the daughter cells
- Metaphase of any of the daughter cells

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

Scripts required to improve any of Cut Detector tasks can be found in the folder [developers].

## License

Distributed under the terms of the [BSD-3] license,
"cut-detector" is free and open source software

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
[file an issue]: https://github.com/15bonte/cut-detector/issues
[developers]: https://github.com/15bonte/cut-detector/tree/main/developers
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[Anaconda]: https://www.anaconda.com/products/distribution
[Fiji]: https://imagej.net/software/fiji/
[NVIDIA]: https://www.nvidia.com/Download/index.aspx?lang=en-us
[conda]: https://docs.conda.io/en/latest/
