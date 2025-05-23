![EPFL Center for Imaging logo](https://imaging.epfl.ch/resources/logo-for-gitlab.svg)
![screenshot](./assets/screenshot.png)
# De Palma Lab - Center for Imaging (2024)

- TODO

## Installation

First, install **Miniconda** by following the instructions: https://docs.conda.io/en/latest/miniconda.html.

Then, start an **Anaconda Prompt** (on Windows, you can find it in the start menu).

Set up a `conda` environment with **Python 3.9**:

```
conda create -n project-env python=3.9
```

Activate the environment:

```
conda activate project-env
```

On Windows, the `zeroc-ice` dependency fails to install from `pip`. As a workaround, install it with `conda`:

```
conda install -c conda-forge zeroc-ice
```

Install Napari and the `depalma plugin` from the GitLab repository in the `project-env` environment:

```
pip install git+https://gitlab.com/epfl-center-for-imaging/depalma.git
```

Start the Napari app with the `depalma` plugin:

```
napari -w depalma
```

## Update the project

To update the project to the latest version, force the reinstallation of the `depalma` plugin in your environment:

```
pip install --force-reinstall git+https://gitlab.com/epfl-center-for-imaging/depalma.git
```

## Build with PyApp

```
python pyapp/build.py
```

## Related projects

- [JupyterHub (De Palma)](https://gitlab.com/epfl-center-for-imaging/depalma-jupyterhub)
