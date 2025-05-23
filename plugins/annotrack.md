Annotrack is a napari plugin for annotating errors in object trajectories. The plugin will help you take a sample of track segments along with a small section of corresponding image and segmentation. Annotrack allows you to annotate three types of errors: (1) ID swap errors (track jumps between objects), (2) false starts (track starts on a pre-existing object) and false terminations (track ends but object still exists). By looking at the combined rates of false starts and false terminations you can assess track discontinutation errors. 

**Please note:** Images and segmentations must be in zarr format. Tracks should be in parquet format.  

## Installation 

There are three main ways to install annotrack:

### Install Using pip
*Please note that this is planned/under development*

Type the following into your terminal (MacOS or Ubuntu) or annaconda prompt (windows):

```bash
pip install annotrack
```

### Install
*Please note that this is planned/under development*

Type the following into your terminal (MacOS or Ubuntu) or annaconda prompt (windows):

```bash
install napari
napari
```

Once napari has opened (this may take a second the first time you open it), go to the pannel at the top of the screen and select the 'plugins' dropdown. Then select install/uninstall plugins. A new window will open showing available plugins. Either scroll down to or search 'annotrack' and click 'install'. 

### Install from Source Code
*please use this for now*

Type the following into your terminal (MacOS or Ubuntu) or annaconda prompt (windows):

```bash
git clone https://github.com/AbigailMcGovern/annotrack.git
cd annotrack
pip install .
```

## Opening Annotrack
Once annotrack is properly installed you will be able to open annotrack by opening napari. You can open napari through the command line (terminal (MacOS or Ubuntu) or annaconda prompt (windows)) as follows:

```bash
napari
```

You can find the annotrack widgets by selecting the dropdown 'plugins' at the pannel at the top of the screen and hovering over 'annotrack'.  

## Sample from CSV

To sample your tracks you will need to supply the file paths for the images, segmentations, and tracks. You supply this in a csv that is structured as shown below:

 ![csv_structure widget](https://github.com/AbigailMcGovern/annotrack/blob/main/media/csv_structure.png)

In this csv, you may also specify how many samples are to be taken from each file. If this is not provided, annotrack will use the value you supply to the `sample_from_csv` widget. The csv must contain a column that specifies a category to which each sample belongs (e.g., species, experimental condition, drug, etc.).  If this isnt important for your samples, just add a dummy category (e.g., sample_type : [A, A, A, A]). 

To access the widget and sample track segments, go to the top of the screen, go to **plugins > annotrack > sample_from_csv**. When the widget is displayed, select the csv file, select a directory into which to save results, and proivide a name for the summary data file (i.e., where your annotations will be written). 

 ![sample_from_csv widget](https://github.com/AbigailMcGovern/annotrack/blob/main/media/sample_from_csv.png)

### Widget parameters
- **path to csv**: 
        The path storing the info from which to generate the samples. 
        The CSV should have the columns: image_path, labels_path, tracks_path, <category_col>, 
        You can also add an optional n_samples column if you would like to 
        specify how many samples to take from each individual file. Otherwise, 
        the default "n_samples" you've supplied will be used.
- **output dir**: 
        Where will the output be saved?
- **output name**: 
        What will output summary files/directories be called?
- **n samples**: 
        How many samples to be obtained from each file. Will be overwritten
        if there is a valid integer number in the n_samples colum of the csv.
- **tzyx cols**: 
        What are the names of the columns denoting time (in frames) and coordinate
        positions (in pixels) in the file containing tracks? The order should be:
        t, z, y, x. 
- **id col**: 
        What is the name of the column denoting the specific ID for each tracked
        object?
- **scale**: 
        size of pixels (e.g., in um) for the z, y, and x coordinates (in that
        order)
- **frames**: 
        Approximate maximum number of frames of track segment. 
        Max frames = frames (if even) or frames - 1 (if odd)
- **box size**: 
        Approximate size of bounding box (in pixels). 
- **min track len**: 
        You can set a minimum track len to include in the search. 
        This can help to eliminate less useful data. This should be at least 1 to only include tracked objects. Set higher only if you are specifically interested in longer lived tracks. 
- **image channel**: 
        This denotes the index of the channel from which to get 
        image data (0: channel 1, 1: channel 2, 2: channel 3, 3: channel 4)

### Annotate Now?

In the case that we are annotating multiple conditions to compare, we want to show them in the one session in randomised order with the annotator blinded to where the sample has originated from. We want to be able to annotated unannotated data from the sample without having the burden of having to do this all at once. The annotations are therefore saved into the saved sample. A selected number of samples saved from the various tracking experiments can be annotated using the following code. If you re-execute this code, you will only be shown not yet annotated data, unless you request otherwise.

Keys to navagate and annotate samples
- '2' - move to next sample
- '1' - move to previous sample
- 'y' - annotate as correct (will move to the next sample automatically)
- 'n' - annotate as containing an error (will move to the next sample automatically)
- 'i' - annotate the frame following a ID swap error
- 't' - annotate the fame following an incorrect termination
- 'Shift-t' - annotate the frame containing a false start error
- 's' - annotate an error ('i', 't', or 'Shift-t') as being associated with a segmentation error (merge or split of objects)

When an error is associated the specific frame ('i', 't', 'Shift-t', or 's'), the frame number (within the original image) will be added to a list of errors for the sample within the sample's (.smpl) info data frame. E.g., you may have a list of ID swaps for your sampled track segment (`[108, 111, 112]`) and a corresponding list of segmentation error associations (`[108, 112]`). 

## Annotate Existing Sample
If you have already saved a sample and want to annotate it, you can load the sample data using the `annotate_existing_sample` widget. This might be useful if you want to have several annotators annotate the same sample. To access this widget, open napari

 ![annotate_existing_sample widget](https://github.com/AbigailMcGovern/annotrack/blob/main/media/annotate_existing_sample.png)

## Contributing and User Support

**User support:** If you have an issue with annotrack please add an issue (go to the Issues tab at the top of the GitHub page). If your issue is a bug, please include as much information as possible to help debug the problem. Examples of information include: details about the image and segmentation data (dimensions), number of images, number of samples you are trying to take. If you are requesting an improvement, try to be as clear as possible about what you need. 

**Contributing:** If you want to contribute to annotrack, please fork the repo and if you want to make changes make a pull request with as much detail about the change as possible. Please ensure any changes you want to make don't break the existing functions.
