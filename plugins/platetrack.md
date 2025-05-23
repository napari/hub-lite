A small napari plugin for tracking platelets. Platetrack requires a segmentation and an image containing raw data. We recomend trying the napari plugin iterseg to generate these. Platetrack uses trackpy for tracking and outputs a dataframe with platelet coordinates, tracking information, and several other variables, which provide information about each platelet. 


## Installation

There are three main ways to install platetrack:

### Install Using pip

Type the following into your terminal (MacOS or Ubuntu) or annaconda prompt (windows):

```bash
pip install platetrack
```

### Install via napari hub

Type the following into your terminal (MacOS or Ubuntu) or annaconda prompt (windows):

```bash
install napari
napari
```

Once napari has opened (this may take a second the first time you open it), go to the pannel at the top of the screen and select the 'plugins' dropdown. Then select install/uninstall plugins. A new window will open showing available plugins. Either scroll down to or search 'platetrack' and click 'install'. 

### Install from Source Code
*please use this for now*

Type the following into your terminal (MacOS or Ubuntu) or annaconda prompt (windows):

```bash
git clone <repository https or ssh>
cd platetrack
pip install .
```


## Opening Platetrack
Once annotrack is properly installed you will be able to open platetrack by opening napari. You can open napari through the command line (terminal (MacOS or Ubuntu) or annaconda prompt (windows)) as follows:

```bash
napari
```

You can find the platetrack widgets by selecting the dropdown 'plugins' at the pannel at the top of the screen and selecting the platetrack widget 'track_platelets'.  


## Tracking Platelets
You can track platelets and obtain a dataframe of information about platelet observation by providing an image/s (t, z, y, x) and a segmentation (t, z, y, x). There are no specific file format requirements, only that you first load the image and segmentation into napari. The napari plugin iterseg provides a widget that will help you load zarr format files. If you have an image with multiple channels (i.e., laser colours), load them into separate napari layers. Iterseg has an option for this called "split channels". Otherwise, refer to the napari website for instructions on using napari layers. 

### Parameters for widget

- **labels_layer**: The napari layer containing the segmentation.
- **image_layer**: The napari layer containing the image (you only need this if you don't want to use all image layers).
- **use_all_image_layers**: If you have several image channels selecting this will obtain information about each channel. The info about image intensity will be stored in columns of the data frame named *[layer name]*_max, *[layer name]*_mean_, 
- **sample_name**: what is the name of the sample (i.e., an identifyer for the biological sample including, for example, the animal number, date, experimental conditions, etc.). This is important if you are planning to combine data frames with different treatment groups. 
- **treatment_name**: name of treatement group or experimental condition (will be added as a categorical variable). This is important if you are planning to combine data frames with different treatment groups. 
- **x_microns**: How big are pixels in the x axis (probably in microns). We need this so that physical rather than pixel coordinates can be computed. 
- **y_microns**: How big are pixels in the y axis (probably in microns). We need this so that physical rather than pixel coordinates can be computed. 
- **z_microns**: How big are pixels in the z axis (probably in microns). We need this so that physical rather than pixel coordinates can be computed. 
- **save_dir**: Directory into which you want to save output data
- **save_file**: name to give the file, 
- **save_format**: There are two options for save format "parquet" or "csv".  
- **search_range**: This is a parameter for the tracking. The search range is how far away (in physical units, e.g., microns) the tracking algorithm will look for the same platelet at the next time point. This can be reduced if trackpy is running out of computational resources due to a high number of observations (platelets)  
- **xy_origin**: If you are rotating the data (e.g., you might want to align the blood flow with the y axis like we do) this parameter defines the centre of rotation. If you would like to use the geometric centre of the image just use "centre". Otherwise, provide a tuple (computer word – basically a list of numbers between brackets) of coordinates in physical units in yx format (e.g., (126, 148)). 
- **rotation**: The number of degrees by which to rotate the data counterclockwise. 



## Platelet data outputted
A number of variables are computed about the platelets alongside the tracking. Each variable is reported for every platelet observation (execpt veclocity, which is only reported for tracked platelets after the first observation). 

- Mean platelet intensity in each image channel
- Max platelet pixel intensity in each channel
- Platelet elongation (0-1, 0 being least elongated, 1 being most elongated)
- Platelet flatness (0-1, 0 being least flat, 1 being most flat)
- Platelet velocity (dv)
- Platelet coordinate velocities (dvx, dvy, dvz)
- Platelet local density (density of platlets in a 15 um radius around the platelet)
- Lists of platelet neighbours within 15 um radius
- Lists of distances of each platelet neighbours within 15 um radius


## Contributing and User Support

**User support:** If you have an issue with platetrack please add an issue (go to the Issues tab at the top of the GitHub page). If your issue is a bug, please include as much information as possible to help debug the problem. Examples of information include: details about the image and segmentation data (dimensions), number of images, number of samples you are trying to take. If you are requesting an improvement, try to be as clear as possible about what you need. 

**Contributing:** If you want to contribute to platetrack, please fork the repo and if you want to make changes make a pull request with as much detail about the change as possible. Please ensure any changes you want to make don't break the existing functions.
