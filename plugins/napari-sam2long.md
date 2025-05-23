
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![PyPI](https://img.shields.io/pypi/v/napari-sam2long.svg?color=green)](https://pypi.org/project/napari-sam2long)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-sam2long.svg?color=green)](https://python.org)
[![tests](https://github.com/maihanhoang/napari-sam2long/workflows/tests/badge.svg)](https://github.com/maihanhoang/napari-sam2long/actions)
[![codecov](https://codecov.io/gh/maihanhoang/napari-sam2long/branch/main/graph/badge.svg)](https://codecov.io/gh/maihanhoang/napari-sam2long)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-sam2long)](https://napari-hub.org/plugins/napari-sam2long)
[![npe2](https://img.shields.io/badge/plugin-npe2-blue?link=https://napari.org/stable/plugins/index.html)](https://napari.org/stable/plugins/index.html)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)

A plugin for interactive 3D (volumetric or time-lapse) segmentation using Meta's Segment Anything Model 2 (SAM2).

Designed for bioimaging researchers working with 3D volumetric or time-lapse images, this plugin supports TIFF files in ZYX or TYX format. Users can provide input and make corrections through point clicks or manually drawn masks.

The tool leverages the [SAM2Long](https://github.com/Mark12Ding/SAM2Long) model, an optimized version of [Meta's SAM 2](https://github.com/facebookresearch/sam2) with enhancements to the memory module for improved performance on long videos. It was built to support long videos, but it remains effective for shorter videos as well.

This [napari] plugin was generated with [copier] using the [napari-plugin-template].

<h3 align="center">Select object with point prompts</h3>

<p align="middle">
  <img src="https://github.com/maihanhoang/napari-sam2long/raw/main/assets/napari-sam2long-firstLabel.gif" width="100%" />
</p>

<h3 align="center">Refine object selection with napari tools </h3>

<p align="middle">
  <img src="https://github.com/maihanhoang/napari-sam2long/raw/main/assets/napari-sam2long-anotherLabel.gif" width="100%" />
</p>


## Installation
Please see the official [SAM 2](https://github.com/facebookresearch/sam2) repo and the [INSTALL.md](https://github.com/facebookresearch/sam2/blob/main/INSTALL.md) for notes and FAQs on potential installation issues.

1. Create a new conda environment with python>=3.10 and install napari:
    ```bash
    conda create -n napari-sam2long python==3.10 pip
    conda activate napari-sam2long
    python -m pip install "napari[all]"
    ```

2. Install PyTorch and TorchVision. Select preferences [here](https://pytorch.org/get-started/locally/) to find correct installation command.

    Example command can look like this:

    ```bash
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
    ```

3. Install SAM2Long:
    ```bash
    git clone git@github.com:maihanhoang/napari-sam2long.git

    cd napari-sam2long/SAM2Long && python -m pip install -e .
    ```
4. Install napari-SAM2Long plugin:
    ```bash
    cd .. && python -m pip install e .
    ```

## Usage

### Segmenting & tracking first object
1. **Open a 3D tiff** in napari, make sure it's in TYX or ZYX format.
2. **Select** the image in the ***Input*** dropdown.
3. **Add a new [labels layer](https://napari.org/0.5.0/howtos/layers/labels.html)** *after* the input image, then select it in the *Labels* dropdown.

    The labels layer must be added after the image to ensure dimension alignment.
4. **Select the *Model***.
5. **Click *Initialize*** to load the image and initialize the inference state.
6. **Define the initial object mask** on any frame:
    - Use the mouse middle-click to prompt the model:
        - *Middle-click* = add region
        - *Ctrl + middle-click* = remove region
    - Or use napari's built-in tools (paintbrush, eraser, etc.) to draw the mask manually.

    If the model doesn’t segment the object accurately with point prompts, manual correction using napari tools can be useful.

7. Once satisfied with the initial mask, **click *Propagate from current frame*** to obtain segmentations for all subsequent frames. The result will be added to the labels layer.

    Propagation only affects future frames. It does not recompute previous ones or consider prompts from other frames. Only the current mask is used to propagate forward.

### Making corrections
8. To refine segmentation, add/remove regions use:
    - *(Ctrl+) middle-click* prompts
    - napari’s label tools
9. *Propagate from current frame* to re-run the model's predictions with the new mask.

    The plugin treats this as a new initial mask and discards earlier prompts on that frame.

### Segmenting another object in the same image/video
10. Save the current labels layer (to preserve previous segmentation).
11. Click *Reset*, or add a new labels layer and select it in the *Labels* dropdown.
Then repeat steps from Step 6 for the next object.

###  Segment new image/video
12. *Reset* inference state.
13. Load new image and follow instructions starting from Step 1.
    *Initialize* is necessary to load the new image.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

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

[file an issue]: https://github.com/maihanhoang/napari-sam2long/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

## Bibliography
[1]: Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman Rädle, Chloe Rolland, Laura Gustafson, Eric Mintun, Junting Pan, Kalyan Vasudev Alwala, Nicolas Carion, Chao-Yuan Wu, Ross Girshick, Piotr Dollár, & Christoph Feichtenhofer. (2024). SAM 2: Segment Anything in Images and Videos.

[2]: Ding, S., Qian, R., Dong, X., Zhang, P., Zang, Y., Cao, Y., Guo, Y., Lin, D., & Wang, J. (2024). SAM2Long: Enhancing SAM 2 for Long Video Segmentation with a Training-Free Memory Tree. arXiv preprint arXiv:2410.16268.

## License & Attribution

This project integrates code from:
- [SAM2](https://github.com/facebookresearch/sam2) by Meta ([`Apache 2.0 License`](LICENSE-Apache-2.0))
- [SAM2Long](https://github.com/Mark12Ding/SAM2Long) by Shuangrui Ding et al. ([`CC-BY-NC 4.0 License`](LICENSE-CC-BY-NC-4.0))
- [napari-samv2](https://github.com/Krishvraman/napari-SAMV2) by Krishnan Venkataraman ([`BSD-3 License`](LICENSE-BSD-3))


The following changes were made to SAM2Long:
- integrated SAM2Long into a napari plugin
- modified the video predictor to support the progress bar in the plugin


Since this project includes **SAM2Long**, it inherits the **CC-BY-NC 4.0 license**, meaning **commercial use is not allowed**.
