
[![License BSD-3](https://img.shields.io/pypi/l/napari-nlm.svg)](https://github.com/maweigert/napari-nlm/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-nlm.svg)](https://pypi.org/project/napari-nlm)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-nlm.svg)](https://python.org)
[![tests](https://github.com/maweigert/napari-nlm/workflows/tests/badge.svg)](https://github.com/maweigert/napari-nlm/actions)
[![codecov](https://codecov.io/gh/maweigert/napari-nlm/branch/main/graph/badge.svg)](https://codecov.io/gh/maweigert/napari-nlm)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-nlm)](https://napari-hub.org/plugins/napari-nlm)

----------------------------------


GPU accelerated non local means (NLM) denoising plugin for napari (WIP)

* currently only supports single-channel 2D or 3D images
* requires a OpenCL capable GPU

![Screenshot](images/screenshot.jpg)


## Installation

You can install `napari-nlm` via [pip]:

    pip install napari-nlm

## Usage

1. Open example image `Open Sample > napari-nlm: noisy bricks`
2. Adjust parameters 
   * `sigma`: denoising strength (the larger sigma, the greater the smoothing)
   * `patch_radius`: size of local patches, 2 or 3 is a good default
   * `search_radius`: size of search area around each pixel to find similar patches, 7-11 is a good default
3. Denoise by pressing `run`


## License

Distributed under the terms of the [BSD-3] license,
"napari-nlm" is free and open source software
