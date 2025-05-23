
Napari needs to be set up on your machine in order to install this plugin.

If you do not have napari installed it can be done following [this article](https://napari.org/stable/tutorials/fundamentals/installation.html).

## Napari plugin manager (recommended)

Search for `microscope-napari` and click install. 
After completed napari needs to be restarted to activate the plugin.

![kép](https://github.com/Nanobiosensorics/microscope-napari/assets/65455148/5438235d-522e-458e-806d-89eaaa027be2)

## Pip package manager

You can install the plugin in the environment where napari is set up with command.
```
pip install microscope-napari
```
If you have a conda environment use anaconda prompt.

# Usage

You can access plugin's functionalities in the upper menu.

![kép](https://github.com/Nanobiosensorics/microscope-napari/assets/65455148/dace1014-6ac0-4797-b0b5-00a56cbc6b61)

## Cellpose

Images can be segmented with custom and built-in cellpose models.

![kép](https://github.com/Nanobiosensorics/microscope-napari/assets/65455148/82d300b9-c523-4b0a-bf44-0f3bfdadae07)

For further information make sure to check out [cellpose](https://github.com/MouseLand/cellpose) and [cellpose-napari](https://github.com/MouseLand/cellpose-napari) plugin.

## Cell counting

Cell counts in pictures can be obtained with cellpose models and average intensity regression models.
Any number of napari image layers can be selected to be evaluated.

### Cellpose model

Without enabling regression model counting the default used method is cellpose segmenting.
The lower settings are for cellpose only.

Cell masks can be output to verify the accuracy of results.

Our custom cellpose models can be accessed [there](https://drive.google.com/drive/folders/1-2SRK_AIlcSODebPoigKA7kbn5cb5s2o?usp=sharing).

![kép](https://github.com/user-attachments/assets/00d1336f-eeb4-4074-87a6-70d9cd866c07)

### Average intensity regression model

For these models we should enable the regression model counting feature.
The lower settings are irrelevant now, cell masks will not be output.
It is only used for counting cells in images.

Our regression models can be accessed [there](https://drive.google.com/drive/folders/1-5uAXN1W5lbE2Pw6Tsa1lR5BYqmPgdEP?usp=sharing).

![kép](https://github.com/user-attachments/assets/7d733347-ceed-4780-9bea-154c8faf3d4d)


