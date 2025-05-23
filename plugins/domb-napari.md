domb-napari
===========

[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg)](https://stand-with-ukraine.pp.ua)

[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/domb-napari)](https://napari-hub.org/plugins/domb-napari)
![PyPI - Version](https://img.shields.io/pypi/v/domb-napari)
![PyPI - License](https://img.shields.io/pypi/l/domb-napari)
<!-- ![Website](https://img.shields.io/website?up_message=domb.bio%2Fnapari&up_color=%2323038C93&url=https%3A%2F%2Fdomb.bio%2Fnapari%2F) -->

__napari Toolkit of Department of Molecular Biophysics <br /> Bogomoletz Institute of Physiology of NAS of Ukraine, Kyiv,  Ukraine__

This plugin offers widgets specifically designed to analyze the redistribution of fluorescence-labeled proteins in widefield epifluorescence time-lapse acquisitions. It is particularly useful for studying various phenomena, including:
- Calcium-dependent translocation of neuronal calcium sensors.
- Synaptic receptor traffic during long-term plasticity induction.
- Membrane protein tracking.

![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/translocation.gif)
__Hippocalcin (neuronal calcium sensor) redistributes in dendritic branches upon NMDA application__


---


## Detection of fluorescence redistributions
A set of widgets designed for preprocessing multispectral image stacks and detecting redistributions in fluorescence intensity. These widgets specifically analyze differential "red-green" image series to identify changes in fluorescence intensity.

Inspired by [Dovgan et al., 2010](https://pubmed.ncbi.nlm.nih.gov/20704590/) and [Osypenko et al., 2019](https://www.sciencedirect.com/science/article/pii/S0969996119301974?via%3Dihub).


### Dual-view stack registration
Registration of four-channel image stacks, including two excitation wavelengths and two emission pathbands, acquired with a dual-view beam splitter. This setup detects different spectral pathbands using distinct sides of the CCD matrix.

- `offset img` - input for a four-channel time-lapse image stack.
- `reference img` - an optional four-channel reference image (e.g., fluorescence beads image), used for offset estimation if `use reference img` is selected.
- `input crop` - number of pixels that will be deleted from each side of input stack frames to discard misalignment artifacts from the dual-view system.
- `output crop` - number of pixels that will be deleted from each side of output stack frames to discard registration artifacts.


### Multichannel stack preprocessing
- `stack order` -  represents the order of axes in the input data array: T (time), C (color), X, and Y (image dimensions). If the input image stack has four dimensions (time, channel, x-axis, y-axis), channels will be split into individual three-dimensional images (time, x-axis, y-axis), each labeled with the `_ch%index%` suffix.
- `median filter` - provides frame-by-frame image smoothing with a kernel of size specified in `median kernel`.
- `background subtraction` -  compensates for background fluorescence intensity. Background intensity is estimated frame by frame as the 0.5 percentile of frame intensity.
- If the `photobleaching correction` option is selected, the image will undergo correction using either an exponential (method `exp`) or bi-exponential (method `bi_exp`) fitting.
- Image stacks can be cropped according to start and stop indexes specified in `frames range` if `drop frames` is selected.

![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/stack_preprocessing.png)


### Red-green series
Primary method for detecting fluorescence-labeled targets redistribution. This widget returns a series of differential images, each representing the intensity difference between the current frame and the previous one, output image labeled with the `_red-green` suffix.

Parameters:

- `left frames` - specifies the number of previous frames used for pixel-wise averaging.
- `space frames` - determines the number of frames between the last left frame and the first right frame.
- `right frames` - specifies the number of subsequent frames used for pixel-wise averaging.

`normalize by int`  function normalizes the differential images relative to the absolute intensity of the input image stack, which helps to reduce background noise amplitude.

If `save MIP` is selected, the maximal intensity projection (MIP) of the differential image stack will be saved with the `_red-green-MIP` suffix.

![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/rg_series.png)

---

## Masking
### Dots patterns masking
Creates labels for bright dot elements on an image, such as pre- and postsynaptic fluorescence markers (e.g., Bassoon/Synaptobrevin for presynapses, PSD-95/Homer for postsynapses, etc.). It returns a labels layer with the `_dots-labels` suffix.

The widget detects the location on the MIP (Maximum Intensity Projection) of the input time series image and applies simple round masks to each detected dot. Watershed segmentation is then used to prevent the merging of overlapping masks.

Parameters:

- `background level` - Background level for filtering out low-intensity elements. This is specified as a percentile of the MIP intensity.
- `detection level` - Minimum intensity of dots, specified as a percentile of the MIP's maximum intensity.
- `mask diameter` - Diameter in pixels for the round mask of each individual dot.
- `minimal distance` - Minimum distance in pixels between the centers of individual round masks.

![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/dots_masking.png)
__Hippocalcin (green) and PSD95 (magents) in dendritic branches__


### Up masking
Generates labels for regions with high intensity based on raw or -red-green images. Returns a labels layer with the `_up-labels` suffix.

The widget provides two detection modes:

- Global masking with a fixed threshold for the entire image.
- In-ROIs masking with a loop over individual ROIs in the input `ROIs mask` with separate detections.

Parameters:

- `det frame index` - index of the frame from the input image used for label detection.
- `det th` - treshold value for detecting bright sites, where the intensity on the selected frame is normalized in the range of -1 to 0.
- `in ROIs det` - option for activating in-ROIs masking.
- `in ROIs det method` - method for in-ROIs masking; otsu provides simple Otsu thresholding, while the threshold method is identical to global detection on nomilized detection frame.
- `in_ROIs_det_th_corr` - caling factor for the det th threshold value for in-ROIs masking.
- `final opening fp` - footprint size in pixels for mask filtering using morphological opening (disabled if set to 0).
- `final dilation fp` - footprint size in pixels for mask morphological dilation (disabled if set to 0).
- `save total up mask` - if selected, a total up mask (containing all ROIs) will be created with the _up-mask suffix.

![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/up_labels.png)
__Gplobal up labels__

The In-ROIs masking option can be particularly useful for co-localization detection. By applying a broad reference mask to several target images, you can create more precise labels for ROIs in specified cell compartments. The following examples demonstrate the detection of mutual locations for static PSD-95 enriched sites (postsynaptic membranes) and HPCA translocation sites only in the vicinity of synapses, using `_dots-labels` for PSD95-mRFP images.

_Note: In the In-ROIs masking mode, labels of detected sites correspond to the matching labels from the input ROIs mask._

In-ROIs masking (reference)|![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/up_labels_1.png)
:------------------:|:-------------------------:
__In-ROIs maskin (translocation)__|![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/up_labels_2.png)
__Masks overlay__|![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/up_labels_overlay.png)


### Intensity masking
Extension of __Up Masking__ widget. Detects regions with increasing (`masking mode` - `up`) or decreasing (`masking mode` - `down`) intensity in `-red-green` images. Returns a labels layer with either `_up-labels` or `_down-labels` suffix, depending on the mode.

![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/int_labels.png)

---

## FRET detection
Widgets for detection and analysis of Förster resonance energy transfer multispectral image stacks.

Based on [Zal and Gascoigne, 2004](https://pubmed.ncbi.nlm.nih.gov/15189889/), [Chen et al., 2006](https://pubmed.ncbi.nlm.nih.gov/16815904/) and [Kamino et al., 2023](https://pubmed.ncbi.nlm.nih.gov/37014867/).


### E-FRET estimation
E-FRET estimation with 3-cube approach.

This method utilizes default values for `a` and `d` coefficients and the `G`-factor, optimized for the pair EYFP and ECFP in our experimental setup:
- Microscope Olympus IX71
- Cube Chroma 69008
- Dual-view system with Chroma 505DCXR beam splitter
- Donor excitation wavelength 435 nm
- Acceptor excitation wavelength 505 nm

Parameters:

- `DD img` - donor emission channel image acquired with the donor excitation wavelength.
- `AD img` - acceptor emission channel image acquired with the donor excitation wavelength.
- `AA img` - acceptor emission channel image acquired with the acceptor excitation wavelength.
- `output type` - type of output image: sensitized emission (`Fc`), apparent FRET efficiency (`Eapp`), or FRET efficiency with photobleaching correction (`Ecorr`).

If the `save normalized` option is selected, an additional image will be saved. This image is normalized to the absolute intensity of the `AA img`, which results in reduced background noise amplitude.

_Note: normalized images are useful for visual control and mask building only; they are not representative for quantitative analysis._

Raw Eapp| ![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/fret_raw.png)
:-:|:-:
__Normalized Eapp__|![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/fret_norm.png)


---


## Exo-/endo-cytosis monitoring with pH-sensitive tag
A set of widgets designed for the analysis of image series containing the pH-sensitive fluorescence protein Superecliptic pHluorin (SEP).

Insipred by [Fujii et al., 2017](https://pubmed.ncbi.nlm.nih.gov/28474392/) and [Sposini et al., 2020](https://www.nature.com/articles/s41596-020-0371-z).


### SEP image preprocessing
Processes image series obtained through repetitive pH exchange methods (such as U-tube or ppH approaches). `pH 1st frame` option indicates the 1st frame pH. By default frames with odd indexes, including index 0, are interpreted as images acquired at pH 7.0, representing total fluorescence intensity (saved with the suffix `_total`). Even frames are interpreted as images obtained at acidic pH (5.5-6.0), representing intracellular fluorescence only (saved with the suffix `_intra`).

If `calc surface img` is selected, an additional total fluorescence image with subtracted intracellular intensity will be saved as the cell surface fluorescence fraction (suffix `_surface`). The input image should be a 3-dimensional single-channel time-lapse.

The `calc projections` option allows obtaining individual pH series projections (pixel-wise series MIP - pixel-wise series average) for the detection of individual exo/endocytosis events.


---


## Intensty profiles building and data frame saving
### ROIs profiles
This widget builds a plot with mean intensity profiles for each Region of Interest (ROI) in labels. It uses either absolute intensity (if `absolute intensity` is selected) or relative intensities (ΔF/F0).

- `time scale` - sets the number of seconds between frames for x-axis scaling.
- `ΔF win` - the baseline intensity for ΔF/F0 profiles is estimated as the mean intensity of the specified number of initial profile points.
- `ΔF amplitude lim` - allows filtering of ROIs by minimum and maximum ΔF/F0 amplitudes. Note: Amplitude filtering works with ΔF/F0 profiles only.
- `profiles crop` - if selected, only a specified range of intensity profile indexes will be plotted, corresponding to the start and stop indexes from `profiles range`.

Additionally, you can save ROI intensity profiles as .csv files using the `save data frame` option and specifying the `saving path`. The output data frames named %img_name%_lab_prof.csv will include the following columns:

- `id` - unique image ID, the name of the input `napari.Image` object.
- `roi` - ROI number, consecutively numbered starting from 1.
- `int` - ROI mean intensity, either raw or ΔF/F0, according to the selected intensity option.
- `dist` - average distance in px to the ROI from the frame, (if `save ROIs distances in data frame` option is selected).
- `index` - frame index.
- `time` - frame time point, adjusted according to the `time scale`.

_Note: the data frame will contain information for all ROIs; amplitude filtering and crop options pertain to plotting only._

Absolute intensity         | ![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/rois_abs.png)
:-------------------------:|:-------------------------:
__ΔF/F0__|![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/rois_df.png)


### Multiple images stat profiles
This widget builds a plot displaying the averaged intensity of all Regions of Interest (ROI) specified in `lab`. It can handle up to three images (`img 0`, `img 1`, and `img 2`) as inputs, depending on the selected `profiles num`.

`time scale`, `ΔF win`, and `absolute intensity` parameters are identical as described in the __ROIs profiles__ widget.

The `stat method` allows for the estimation of intensity and associated errors through the following methods:
- `se` - mean +/- standard error of the mean.
- `iqr` - median +/- interquartile range.
- `ci` - mean +/- 95% confidence interval based on the t-distribution.

Absolute intensity         | ![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/stat_abs.png)
:-------------------------:|:-------------------------:
__ΔF/F0__|![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/stat_df.png)


### Multiple labels stat profiles
This widget builds a plot displaying the averaged intensity of all Regions of Interest (ROI) for one target `img`. It can handle up to three labels (`lab 0`, `lab 1`, and `lab 2`), depending on the selected `profiles num`.

`time scale`, `ΔF win`, and `absolute intensity` parameters are identical as described in the __ROIs profiles__ widget.

The `stat method` allows for the estimation of intensity and associated errors through the following methods:
- `se` - mean +/- standard error of the mean.
- `iqr` - median +/- interquartile range.
- `ci` - mean +/- 95% confidence interval based on the t-distribution.

Absolute intensity         | ![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/stat_lab_abs.png)
:-------------------------:|:-------------------------:
__ΔF/F0__|![](https://raw.githubusercontent.com/wisstock/domb-napari/master/images/stat_lab_df.png)
