
[![Test and lint](https://github.com/AllenCell/allencell-segmenter-ml/actions/workflows/test_lint.yaml/badge.svg?branch=main&event=push)](https://github.com/AllenCell/allencell-segmenter-ml/actions/workflows/test_lint.yaml)

## This version is a release candidate currently undergoing testing and development.
Our team is actively working on this plugin and will have an *official release* with additional features very soon. 
 
Please keep an eye on this page for updates. 
 
In the meantime, [please report any bugs here.](https://github.com/AllenCell/allencell-segmenter-ml/issues/new/choose)


## What is Allen Cell Segmenter ML
A deep learning-based segmentation Napari plugin to curate datasets, train your own model (UNET), and run inference on 2D and 3D cell data. 


##  📰 News

 - **[2024.09.24]** 🎉 Initial dev release of the plugin and Megaseg models!



## 🛠️ Installation

### System Requirements

We currently support `Windows`, `MacOS`, and `Linux` operating systems. The minimum system requirements are:

- 8GB of RAM
- 8 CPU Cores
- 1 NVIDIA GPU with 8GB of VRAM (optional)

**NOTE:** If you plan to use the plugin _without_ a GPU, training will default to using your CPU and will be significantly slower. A GPU is highly recommended for training models. Depending on how large your images are---2D vs 3D, resolution, model size---running inference may also be slow without a GPU.

### Pre-Installation

##### STEP 1. Install Python

Before installing the plugin, please make sure you have the following installed:

- Python 3.10 or later

__New to `Python`?__ We recommend installing `Python 3.10` through the official [`Python` website](https://www.python.org/downloads/). This will include the `pip` package manager, which is required to install the plugin.

If you are unsure if you have Python installed or which version you may have, you can check by running the following command in your terminal or powershell:

```bash
# Check version of python
python --version

# If the above does not work, try this one
python3 --version

# Specifically check for Python 3.10
python3.10 --version
```



##### STEP 2. Create a Virtual Environment

Next we will create a new `Python` environment to install the plugin. This will help avoid conflicts with other packages you may have installed by creating an isolated environment for the plugin to live in. In general, it is good practice to choose a name for your environment that is related to either the project you are working on or the software you are installing. In this case, we use `venv-allen-segmenter-ml` where `venv` stands for __virtual environment__.

Navigate to where you want to create a new environment (_Example._ `Documents`), run the following command in your terminal or powershell:

```bash
# Create a new environment
python3.10 -m venv venv-allen-segmenter-ml

# Activate the environment
source venv-allen-segmenter-ml/bin/activate
```
#### Confirm Virtual Environment is Activated

To confirm that the virtual environment has been successfully activated, you can follow these steps:


1. Check that the prompt includes the name of your virtual environment, `venv-allen-segmenter-ml`. It should look something like this:

    ```bash
    (venv-allen-segmenter-ml) $

    # Example on a Windows machine
    (venv-allen-segmenter-ml) PS C:\Users\Administrator\Documents> 
    ```

2. Run the following command to verify `Python 3.10` is being used within the virtual environment:

    ```bash
    python --version
    
    # Python 3.10.11   <-- Example output
    ```






## Install the Plugin

To install the latest version of the plugin:
```bash
pip install allencell-segmenter-ml
```

### 🚨 Post-Installation 🚨

> :memo: __NOTE:__ This section is specifically for users with at least one NVIDIA GPU installed on their machine. Not sure if you have an NVIDIA GPU? You can check by running `nvidia-smi` as shown [below](#step-1-checking-cuda-version). If you __do not__ have an NVIDIA GPU system, you can skip this section.

Required Package

- `torch` ([PyTorch]) 2.0 or later

After installing the plugin, you need to install a PyTorch version that is compatible with your system. PyTorch is a deep learning library that is used to train and run the models in the plugin. We understand that everyone manages CUDA drivers and PyTorch versions differently depending on their system and use cases, and we want to respect those decisions because CUDA drivers can be a pain. 

##### STEP 1. Checking CUDA Version

To check your CUDA version, you can run the following command in your terminal or powershell:

```bash
nvidia-smi
```

As an example, the output will look similar to this. My `CUDA Version` is `11.8`:

```bash
PS C:\Users\Administrator> nvidia-smi
Fri Sep 13 03:22:15 2024
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 522.06       Driver Version: 522.06       CUDA Version: 11.8     |
|-------------------------------+----------------------+----------------------+
| GPU  Name            TCC/WDDM | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla T4           TCC   | 00000000:00:1E.0 Off |                    0 |
| N/A   27C    P8     9W /  70W |      0MiB / 15360MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

---

##### STEP 2. PyTorch Installation

__To Install PyTorch__, please visit the [__PyTorch website__](https://pytorch.org/get-started/locally/) and select the appropriate installation options for your system. An example is provided below.



<img width="828" alt="torch-install" src="https://github.com/user-attachments/assets/1d8789c0-1f2c-4b11-841b-666f540601e6">

> __PyTorch Installation__ for Windows, MacOS, and Linux

##### Example

For instance, if I am using

- `Windows` workstation
- `pip` package manager
- `Python` (3.10)
- `CUDA 11.8` 

Then the command for me would be:

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

If the installation is successful, let's test just to be sure that your GPU is detected by PyTorch. Run the following command in your terminal or powershell:

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

You should see `True` if your GPU is detected (see below). If you see `False`, then PyTorch is not detecting your GPU. You may need to reinstall PyTorch or check your CUDA drivers. Double check that your virtual environement is activated (`venv-allen-segmenter-ml`).

```bash
(venv-allen-segmenter-ml) PS C:\Users\Administrator\Documents> python -c "import torch; print(torch.cuda.is_available())"
True
```


:tada: You have successfully installed the plugin and PyTorch. You are now ready to use the plugin!

---

## Running the Plugin

To run the plugin (and verify the installation), you can use the following command in your terminal or powershell:

```bash
napari
```

You should see the below window pop up. To start using the plugin, click on the `Plugins` tab and select `Allen Cell Segmenter ML`:

<img width="1084" alt="plugin" src="https://github.com/user-attachments/assets/7238c7a2-5741-4d1f-8a3d-b8c133e9bb27">

> __Allen Cell Segmenter ML__ Launching the Plugin.

## Models

| Model    | Model Name            | Available in Plugin | Model Size (MB)  | Supported Magnifications| 
|----------|-----------------------|----------------------------------|----------------------------------------|:-------------------------:|
| MegaSeg-S  | `megaseg_light`      | ✅        | 4.8MB      |       `100X`         |          
| MegaSeg-M  | `megaseg_medium`     | Coming soon!       |  TBD     |       TBD       |           
| MegaSeg-L  | `megaseg_large`      | ✅        | 191MB       |       `20X, 40X, 67X, 100X`        |  



### Download and using the Megaseg Models

To use the MegaSeg models in the plugin, you can download them from the dropdown menu shown below:

![download-model](https://github.com/user-attachments/assets/03cc500e-ff74-40c3-bf9e-c40e58d3e47c)

> __Download the MegaSeg Model__ for use in the Plugin

A popup window will appear and you can select which model you would like to download. Once the download is complete, another popup will let you know the download was successful and where the model was downloaded.

<img width="1275" alt="select-megaseg" src="https://github.com/user-attachments/assets/0a26a31a-49eb-46cf-a550-47f1fa55c9c3">

 > __Select the MegaSeg model__ to Run Inference

 To use the model for inference on your images, choose `Select an existing model`, select the megaseg model you downloaded, and click `Apply`. You can now use the model to segment your images!

## License

Distributed under the terms of the [Allen Institute Software License] license.

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[@napari]: https://github.com/napari
[Allen Institute Software License]: https://github.com/AllenCell/allencell-segmenter-ml/blob/main/LICENSE
[file an issue]: https://github.com/AllenCell/allencell-ml-segmenter/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[PyTorch]: https://pytorch.org/get-started/locally/
