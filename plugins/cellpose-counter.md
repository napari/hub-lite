
[![License BSD-3](https://img.shields.io/pypi/l/cellpose-counter.svg?color=green)](https://github.com/szablowskilab/cellpose-counter/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/cellpose-counter.svg?color=green)](https://pypi.org/project/cellpose-counter)
[![Python Version](https://img.shields.io/pypi/pyversions/cellpose-counter.svg?color=green)](https://python.org)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/cellpose-counter)](https://napari-hub.org/plugins/cellpose-counter)

A Napari plugin for cell/nuclei counting from a region or interest using
cellpose models.

----------------------------------

## Installation

Option 1: via [pip](https://pip.pypa.io/en/stable/) (or pip alternatives like
[uv](https://docs.astral.sh/uv/)):

Below is a minimally working example of setting up a new virtual environment and
installing the counter module with uv on Unix based systems.

```bash
uv venv # create virtual environment in .venv
source .venv/bin/activate

uv pip install "napari[all]" cellpose-counter
```

Option 2: via Docker/Podman. The provide [Dockerfile](./Dockerfile) can be used
to install Napari and the counter plugin along with a preconfigured Xpra server
using the napari-xpra image. Below is an example of building the image and
running the application with GPU support.

```bash
podman build -t cellpose-counter .
podman run -it -d \
    -p 9876:9876 \
    -e XPRA_START="python3 -m napari -w cellpose-counter" \
    --device nvidia.com/gpu=all
```

Then, navigate to `http://localhost:9876` to view the application in a virtual
machine.

Note: There is a known issue installing the plugin directly from Napari. Please
see [this issue](https://github.com/szablowskilab/cellpose-counter/issues/12)
for more updates.

## GPU Acceleration

To enable GPU acceleration, you will need a CUDA capable GPU along with the
[CUDA toolkit](https://developer.nvidia.com/cuda-toolkit) and [cudNN library](https://developer.nvidia.com/cudnn).

For instructions on installing cuda toolkit and cudNN, see:

1. [cuda toolkit installation for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#fedora)
1. [cudNN installation for Linux](https://docs.nvidia.com/deeplearning/cudnn/latest/installation/linux.html)

Once these are installed, update the pytorch package by first uninstalling torch
(if already instsalled).

```bash
uv pip uninstall torch
```

Then install a torch version that is compatible with your CUDA version. For example,

```bash
uv pip install torch --index-url https://download.pytorch.org/whl/cu118
```

After installation, you can verify in an interactive python console with:

```python3
import torch
torch.cuda.is_available()
```

## Usage

To open Napari with the cellpose counter loaded, run `napari -w cellpose-counter`.

A dock widget will be open on the right side of the Napari interface. There
you can view options for restoring images (using the cellpose denoise module),
and counting cells/nuclei in a region of interest (ROI).

A few important notes:

1. Images in TIFF or CZI file formats may be used.
1. Images must be grayscale or single channel. RGB images may be loaded, but
should be split. You can do this by right clicking on the image and select
`split rgb` or `split stack`.
1. ROIs can be drawn using the shape layer tools. Only a single ROI can be drawn
per shape layer (otherwise only the first draw ROI will be used).
1. ROIs should be square or rectangular. You can draw ROIs as polygons or other
shapes, but a bounding box will be made from these shapes anyway.
1. For long running processes such as image restoration or counting, it may seem
like Napari is not doing anything. Notifications are shown in the viewer to
display import information and a small activity indicator can be seen in the
bottom right hand corner. If this indicator is spinning, then work is being done
even if it doesn't look like it.
1. In case of a large number of uncounted nuclei, consider modifying the
segmentation parameters, or use the `Continue Counting` option to re-run the
segmentation on uncounted nuclei.

## Updating

1. via Napari plugin manager. Select cellpose-counter plugin and update button.

1. via pip (or uv, ..., etc.)

```bash
uv pip install cellpose-counter --upgrade
```

## Contributing

All contributions are welcome. Please submit an issue for feedback or bugs.

## Citations

This plugin is built on top of the Cellpose segmentation and denoising models.
If you use this plugin, please cite the following paper:

```bitex
@article{stringer2021cellpose,
title={Cellpose: a generalist algorithm for cellular segmentation},
author={Stringer, Carsen and Wang, Tim and Michaelos, Michalis and Pachitariu, Marius},
journal={Nature Methods},
volume={18},
number={1},
pages={100--106},
year={2021},
publisher={Nature Publishing Group}
}
```

## License

[BSD-3](./LICENSE)
