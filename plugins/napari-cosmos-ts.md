[napari](https://napari.org/stable/) plugin for colocalization single-molecule spectroscopy (CoSMoS) time series (TS) analysis.

![GitHub Tag](https://img.shields.io/github/v/tag/marcel-goldschen-ohm/napari-cosmos-ts?cacheSeconds=1)
![build-test](https://github.com/marcel-goldschen-ohm/napari-cosmos-ts/actions/workflows/build-test.yml/badge.svg)

![GitHub Release](https://img.shields.io/github/v/release/marcel-goldschen-ohm/napari-cosmos-ts?include_prereleases&cacheSeconds=1)
![publish](https://github.com/marcel-goldschen-ohm/napari-cosmos-ts/actions/workflows/publish.yml/badge.svg)

- [Install](#install)
- [Run](#run)
- [Documentation](#documentation)

## Install
If you are unfamiliar with how to create a python environment or pip install a package, see the [detailed installation instructions below](#install-for-beginners).

Requires [napari](https://github.com/napari/napari).
```shell
pip install "napari[all]"
```
Install latest release version:
```shell
pip install napari-cosmos-ts
```
Or install latest development version:
```shell
pip install napari-cosmos-ts@git+https://github.com/marcel-goldschen-ohm/napari-cosmos-ts
```
To upgrade a previously installed version, simply add the `--upgrade` flag to the above install commands.

## Run
Launch the `napari` viewer. In a command shell or terminal *where you have activated the virtual environment where you installed napari-cosmos-ts* run the following command:
```shell
napari
```
Launch the `napari-cosmos-ts` plugin: From the napari viewer `Plugins menu` select `Colocalization Single-Molecule Time Series (napari-cosmos-ts)`. This should bring up the napari-cosmos-ts docked widget within the viewer.

## Documentation
:construction:

## Install for Beginners
1. Install the `conda` package manager. Simplest is to download [Miniconda](https://docs.conda.io/en/main/miniconda.html) and run the installer.
2. Create a virtual python environment named `napari-env` (or name it whatever you want) in which to install [napari](https://napari.org/stable/) and this plugin. In a command shell or terminal run the following command:
```shell
conda create --name napari-env python
```
3. Activate your virtual environment. *!!! Note you will have to do this every time you open a new command shell or terminal.* In a command shell or terminal run the following command:
```shell
conda activate napari-env
```
4. Install `napari` into your virtual environment. In a command shell or terminal *where you have activated your virtual environment* run the following command:
```shell
pip install "napari[all]"
```
5. Install `napari-cosmos-ts` into your virtual environment. In a command shell or terminal *where you have activated your virtual environment* run the following command:
```shell
pip install napari-cosmos-ts
```
Or for the latest version of `napari-cosmos-ts`:
```shell
pip install napari-cosmos-ts@git+https://github.com/marcel-goldschen-ohm/napari-cosmos-ts
```
*!!! Remember, every time you open a new command shell or terminal you will need to activate the virtual environment where you installed napari-cosmos-ts before [running the app](#run).*
