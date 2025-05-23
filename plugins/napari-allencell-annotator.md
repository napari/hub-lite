
[![License BSD-3](https://img.shields.io/pypi/l/napari-allencell-annotator.svg?color=green)](https://github.com/bbridge0200/napari-allencell-annotator/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-allencell-annotator.svg?color=green)](https://pypi.org/project/napari-allencell-annotator)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-allencell-annotator.svg?color=green)](https://python.org)
[![tests](https://github.com/bbridge0200/napari-allencell-annotator/workflows/tests/badge.svg)](https://github.com/bbridge0200/napari-allencell-annotator/actions)
[![codecov](https://codecov.io/gh/bbridge0200/napari-allencell-annotator/branch/main/graph/badge.svg)](https://codecov.io/gh/bbridge0200/napari-allencell-annotator)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-allencell-annotator)](https://napari-hub.org/plugins/napari-allencell-annotator)

A plugin that enables image annotation/scoring and writes annotations to a .csv file. 
Plugin provided by the Allen Institute for Cell Science.

The Allen Cell Image Annotator plugin for napari provides an intuitive
graphical user interface to create annotation templates, annotate large 
image sets using these templates, and save image annotations to a csv file. 
The Allen Cell Image Annotator is a Python-based open source toolkit 
developed at the Allen Institute for Cell Science for both blind, unbiased and un-blind 
microscope image annotating. This toolkit supports easy image set selection
from a file finder and creation of annotation templates (text, checkbox, drop-down, spinbox, and point).
With napari's multi-dimensional image viewing capabilities, the plugin seamlessly allows users to
view each image and write annotations into the custom template.
Annotation templates can be written to a json file for sharing or re-using. After annotating,
the annotation template, image file list, and the annotation values 
are conveniently saved to csv file, which can be re-opened for further annotating. 

-   Supports the following image types:
    - `OME-TIFF`
    - `TIFF`
    - `CZI` 
    - `PNG` 
    - `JPEG`
    - `OME-ZARR`


----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to files up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->

## Installation using Command Line
### 1. Prerequisites

The plugin requires [Conda](https://docs.anaconda.com/anaconda/install/).
- [Installing on Windows ](https://docs.anaconda.com/anaconda/install/windows/) 
  - Follow the steps linked above except
  - On step 8, check top the box to add to PATH
  - ![Alt text](napari_allencell_annotator/assets/windowsstep8.png)
- [Installing on Mac ](https://docs.anaconda.com/anaconda/install/mac-os/) 

### 2. Install the plugin
Click the link corresponding to your OS.
#### [Windows](https://alleninstitute-my.sharepoint.com/:u:/g/personal/r_dhamrongsirivadh_alleninstitute_org/EexXIxeeIbNEs4KMjimcXOcBMn2J2QwxJhNEkOcRHC1eVg?e=JKa5WI)
- From the link above, click the three dots on the top menu bar and select download. 
- Open a file explorer and go to the Downloads folder. Use **Option 1** below. A prompt window should open and start installing. If this fails use **Option 2**. 
  - **Option 1**: Double-click the file _install_napari.sh_
  - **Option 2**: Search the file finder for Anaconda Prompt. Open version 3. Run the following commands one line at a time. 
    - conda create -n napari_annotator python=3.10 anaconda
    - conda activate napari_annotator
    - python -m pip install --upgrade pip
    - python -m pip install "napari[all]"
    - python -m pip install napari-allencell-annotator
    - napari
  - **Still not working?** Try using conda forge instead of pip. 
    - Ex: conda install -c conda-forge napari instead of python -m pip install "napari[all]"
#### [MacOS/Unix](https://alleninstitute-my.sharepoint.com/:u:/g/personal/r_dhamrongsirivadh_alleninstitute_org/ESeAYWwWFuRFhgpqgbiKQ6QBXdU8Dg8OU9ilpJ5VmoY-cA?e=BHpReg)
- From the link above, download the file. 
- Open terminal. 
- Run _chmod +x ./Downloads/install_napari.command_ 
  - If you get a file not found error try adjusting the path to match where install_napari.command was downloaded.
- Open finder, navigate to the file, double-click _install_napari.command_ . 
  - A terminal window should open and start installing. 
  

### 3. Launch the Plugin

Once the napari window opens, go to **Plugins**.
- If **napari-allencell-annotator** is listed click it to launch. 
- If it is not listed 
- **Install/Uninstall Plugins** ⇨ check the box next to **napari-allencell-annotator** ⇨ **close** ⇨ **Plugins** ⇨ **napari-allencell-annotator** .

### 4. Re-opening the Plugin After Installing
- Windows
  - Search for anaconda navigator in file finder
  - Click on navigator version 3
  - Once the navigator opens, click **Environments** on the left side
  - Click on the annotator environment and wait for it to load
  - Press the play button
  - Type _napari_ in the prompt that opens
  - Click **Plugins** ⇨ **napari-allencell-annotator**
- MacOS
  - Open terminal
  - Run these commands one line at a time
    - conda activate napari_annotator
    - napari
  - Click **Plugins** ⇨ **napari-allencell-annotator**

## Installation from Napari Hub
If you have previously installed Napari on your machine, you can follow these steps to install the plugin from Napari Hub.

### 1. Install the Plugin
- Open Napari
- Go to **Plugins** ⇨ **Install/Uninstall Plugins...**
- Find **napari-allencell-annotator** in **Available Plugins**
- Click **Install**
- Close the window after the installation finishes

### 2. Launch the Plugin
- Click **Plugins** ⇨ **napari-allencell-annotator**
  - You might have to restart Napari for the annotator to appear in the plugin list.
  - If you still can't see the plugin, go to **Install/Uninstall Plugins** ⇨ check the box next to **napari-allencell-annotator**.

## Quick Start

1. Open napari
2. Start the plugin 
   - Open napari, go to **Plugins** ⇨ **napari-allencell-annotator**.
3. Create or import annotations and add images to annotate.

For more detailed usage instructions, check out this [document](napari_allencell_annotator/assets/AnnotatorInstructions.pdf) 
## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-allencell-annotator" is free and open source software

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

[file an issue]: https://github.com/bbridge0200/napari-allencell-annotator/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
