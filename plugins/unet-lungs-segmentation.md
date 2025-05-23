
We provide a neural network model for segmenting the lungs of the mice. The model is based on the [U-Net](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/) architecture.

<p align="center">
    <img src="https://raw.githubusercontent.com/qchapp/lungs-segmentation/refs/heads/master/images/main_fig.png" height="500">
</p>

The goal of our tool is to provid a reliable way to segment the lungs in mouse CT scans. The U-net model produces a binary mask representing the segmentation of the lungs.

## Try the model 

- [Install the package](#installation)
- [Follow the usage instructions](#usage-in-napari)

## Installation

We recommend performing the installation in a clean Python environment.

The code requires `python>=3.9`, as well as `pytorch>=2.0`. Please install Pytorch first and separately following the instructions for your platform on [pytorch.org](https://pytorch.org/get-started/locally/).

Install `unet_lungs_segmentation` using *pip* after you've installed Pytorch:

```sh
pip install unet_lungs_segmentation
```

or clone the repository and install with:

```sh
git clone https://github.com/qchapp/lungs-segmentation.git
pip install -e .
```

## Models

The model weights (~1 GB) will be automatically downloaded from [Hugging Face](https://huggingface.co/qchapp/unet-lungs-segmentation-weights).


## Usage in Napari

[Napari](https://napari.org/stable/) is a multi-dimensional image viewer for python. To use our model in Napari, start the viewer with

```sh
napari
```

To open an image, use `File > Open files` or drag-and-drop an image into the viewer window. If you want to open medical image formats such as NIFTI directly, consider installing the [napari-medical-image-formats](https://pypi.org/project/napari-medical-image-formats/) plugin.

**Sample data**: To test the model, you can run it on our provided sample image. In Napari, open the image from `File > Open Sample > Mouse lung CT scan`.

Next, in the menu bar select `Plugins > Lungs segmentation (unet_lungs_segmentation)`. Select an image and run it by pressing the "Segment lungs" button.

<p align="center">
    <img src="https://raw.githubusercontent.com/qchapp/lungs-segmentation/refs/heads/master/images/napari-screenshot.png" height="500">
</p>

## Usage as a library

You can run a model in just a few lines of code to produce a segmentation mask from an image (represented as a numpy array).

```py
from unet_lungs_segmentation import LungsPredict

lungs_predict = LungsPredict()
mask = lungs_predict.segment_lungs(your_image)
```
or if you want to apply a specific `threshold` (`float` between 0 and 1):
```py
mask = lungs_predict.segment_lungs(your_image, threshold)
```

## Usage as a CLI

Run inference on an image from the command-line. For example:

```sh
uls_predict_image -i /path/to/folder/image_001.tif [-t <threshold>]
```

The `<threshold>` will be applied to the predicted image in order to have a binary mask. A default threshold of 0.5 will be applied if none is given. Should be a `float` between 0 and 1.

The command will save the segmentation next to the image:
```
folder/
    ├── image_001.tif
    ├── image_001_mask.tif
```

Run inference in batch on all images in a folder:

```sh
uls_predict_folder -i /path/to/folder/ [-t <threshold>]
```
Will produce:
```
folder/
    ├── image_001.tif
    ├── image_001_mask.tif
    ├── image_002.tif
    ├── image_002_mask.tif
```

## Dataset

Our model was trained using a dataset of `355` images coming from 17 different experiments, 2 different scanners and validated on `62` images.

## Issues

If you encounter any problems, please fill an issue along with a detailed description.

## License

This model is licensed under the [BSD-3](LICENSE.txt) license.

## Carbon footprint of this project

As per the online tool [*Green algorithms*](http://calculator.green-algorithms.org/), the footprint of training this model was estimated to be around 584 g CO2e.
