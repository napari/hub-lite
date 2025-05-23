
<p align="left">
  <img src="images/logo_3d.png" alt="VASCilia Logo" width="170">
</p>

Explore the complexities of the cochlea with VASCilia, a Napari plugin created to aid in the 3D segmentation and quantification of stereocilia bundles. Equipped with a range of thoughtful features, VASCilia stands for (Vision Analysis StereoCilia) and it provides a supportive tool for auditory research, including:  
1. Slice Selection: Easily navigate through 3D stacks to find the slices that matter most for your research.
2. Stack Rotation: Adjust the orientation of your stack to facilitate better analysis.
3. 3D Instance Segmentation: Identify and assess individual bundles with clear separation using deep learning.
4. Bundle Deletion: Remove unwanted bundles to streamline your dataset.
5. Regional Classification: identify whether the region is from BASE, MIDDLE, or APEX in the cochlea using deep learning.
6. Hair Cell Differentiation: Distinguish between Inner Hair Cells and Outer Hair Cells with confidence using deep learning.
7. Measurement Analysis: Calculate various measurements such as volume, centroid location, and surface area.
8. Fluorescence Intensity Analysis: Assess the intensity of signal or protein with detailed precision.
9. 3D Bundle Height Calculation: Measure the 3D distance from the peak to the base of each bundle, according to your sample's resolution.
10. Bundle orientation: Determine bundle orientation for all hair cells based on two strategies: Height-only and Height&Distance.

VASCilia &#x2764;&#xfe0f; is a valuable resource for the ear research community &#128066;, simplifying the complexity of measurement and analysis. It comes with a suite of pre-trained models to facilitate 3D segmentation, cell type identification and regional classification.

Furthermore, we are committed to supporting research growth with a comprehensive training section for those looking to explore different staining techniques or develop new segmentation models through annotation and refinement.

VASCilia is here to support researchers in their quest for deeper understanding and innovation in the study of cochlear structures.  
*[click the image to see a highlights reel of the plugin](https://youtu.be/MwMOxJQ_elo)*  

[![Watch the video](images/VASCilia_pipeline2.png)](https://youtu.be/MwMOxJQ_elo)

*[Click me to see a video demo of the entire workflow](https://youtu.be/mNPJ1g0vEW8)*  

## How to install : 
STEP1[Install WSL]:  
1. Open the Command Prompt and install the Ubuntu 20.04 Distribution by simply copy paste this command  
wsl --install -d Ubuntu-20.04
2. After the setup successfully completes, reboot your computer. Open Ubuntu by typing "Ubuntu" in the search bar. A pop-up window for Ubuntu will appear. To check if CUDA and the GPU are correctly installed and available, type nvidia-smi in the terminal  

STEP2[Download the deep learning trained models]:
1. Download the VASCilia_trained_models from https://www.dropbox.com/scl/fo/jsvldda8yvma3omfijxxn/ALeDfYUbiOuj69Flbc728rs?rlkey=mtilfz33qiizpul7uyisud5st&st=41kjlbw0&dl=0 
now you should have a folder called 'models'

- 📁 **models** `[Trained models]`
    - 📁 **cell_type_identification_model** `[has weights for cell type identification IHC vs OHC]`
    - 📁 **new_seg_model** `[incase you fine tune the existing model, the new model will be stored here]`
    - 📁 **region_prediction** `[has weights for region prediction]`
    - 📁 **seg_model**  `[has the weights for the 3D instance segmentation model]`
    - 📁 **Train_predict_stereocilia_exe** `[executible needed by the plugin to segment and retrain the model using WSL]`  
    - 📁 **ZFT_trim_model** `[deep learning model weights for z focus tracker algorithm]`  
    - 📁 **rotation_correction_model** `[deep learning model weights for correcting the orientation of the stack]`  
 
STEP3[download one dataset to test VASCilia]:  
download one sample from our datasets to try in this link https://www.dropbox.com/scl/fo/pg3i39xaf3vtjydh663n9/h?rlkey=agtnxau73vrv3ism0h55eauek&dl=0  
create a folder, called raw_data folder and put the downloaded dataset inside the raw_data folder

  - 📁 **raw_data** `[raw data (stacks) is placed here]`
    - 📄 Litter 12 Mouse 4 MIDDLE - delBUNdelCAP_Airyscan Processing.czi
   
Also create another folder called processed_data in which the plugin will use to store the results of the analysis
  
  - 📁 **processed_data** `[processed data will be stored here]`

## Instructions for Cloning the Repository [You can do either Option A or Option B]:
## Option A: Cloning the Repository:  
```sh
git clone https://github.com/ucsdmanorlab/Napari-VASCilia.git
cd Napari-VASCilia
conda create -y -n napari-VASCilia -c conda-forge python=3.10    
conda activate napari-VASCilia    
pip install -r requirements.txt
pip install -e .
napari  
```
## Option B: Installing via PyPI:
```sh
conda create -y -n napari-VASCilia -c conda-forge python=3.10    
conda activate napari-VASCilia 
# Download the requirements.txt file from this repository and ensure you have it in your working directory. 
pip install -r requirements.txt
pip install Napari-VASCilia
napari  
```
Post-installation:  
1. Activate the plugin through Plugins -> VASCilia UI (Napari-VASCilia).
2. This will generate the config.json file at C:/Users/Username/.napari-vascilia/config.json. Update the paths in config.json as needed.
config.json will be generated upon running the plugin for the first time.

- 📁 C:/Users/Username/   [your home folder]
  - 📁 **.napari-vascilia** `[Folder_path]`
    - 📄 **config.json**

Please update the /.../ portion according to your paths:

```sh
{
    "rootfolder": "C:/Users/.../processed_data/",
    "wsl_executable": "C:/Users/.../models/Train_predict_stereocilia_exe/Train_Predict_stereocilia_exe_v2",
    "model": "C:/Users/.../models/seg_model/stereocilia_v7/",
    "model_output_path": "C:/Users/.../models/new_seg_model/stereocilia_v8/",
    "model_region_prediction": "C:/Users/.../models/region_prediction/resnet50_best_checkpoint_resnet50_balancedclass.pth",
    "model_celltype_identification": "C:/Users/.../models/cell_type_identification_model/",
    "ZFT_trim_model": "C:/Users/.../models/ZFT_trim_model/",
    "rotation_correction_model": "C:/Users/.../models/rotation_correction_model/",
    "green_channel": 0,
    "red_channel": 1,
    "blue_channel": -1,
    "signal_intensity_channel": 0,
    "flag_to_resize": false,
    "flag_to_pad": false,
    "resize_dimension": 1200,
    "pad_dimension": 1500,
    "button_width": 100,
    "button_height": 35
}
```

Congratulations :) &#127881;, now you can enjoy working with the plugin. 

## Unique about VASCilia :  
VASCilia saves all the intermediate results and the variables inside a pickle file while the user is using it in a very effiecint way. That allows a super fast uploading for the analysis if the user or their supervisor wants to keep working or review the analysis steps.  
*[Click me to learn how to upload a z-stack](https://youtu.be/Sxm_fsjoWL0)*  

## How to use VASCilia :  
*[Click me to see a video demo of the entire workflow](https://youtu.be/mNPJ1g0vEW8)*  

There are several buttons inside the blugin in the right hand side of Napari:

1. 'Open CZI Cochlea Files and Preprocess' button: read the CZI file.
2. 'Upload Processed CZI Stack' button: Incase you already have processed the stack, then just uplead your Analysis_state.pkl that usually has all the variables needed to upload your analysis
3. 'Trim Full Stack' button: this button allows you to choose only the slices of interest (has been automated in v_1_1_0)
4. "Rotate' buttom: this button allows to rotate the stack to have proper analysis (has been automated in v_1_1_0)  
5. Segment with 3DBundleSeg: it is a two steps algorithm (2D detection + multi-object assignment algorithm across all slices) to produce robust 3D detection. 3DBundleSeg is the first instance segmentation model for stereocilia bundles in the literature. It is trained on P5 and P21 3D stacks (thousands of 2D instances) and it produces highly acccurate boundary delineation even in the most challenging datasets. Here are some examples:  

<p align="center">
  <strong>3DBundleSeg can tackle challenged cases</strong>  
  <br>
  <img src="images/challenged_cases_gray.png" width="100%">
</p>

<p align="center">
  <strong>Multi-object assignment algorithm to produce robust 3D detection</strong>  
  <br>
  <img src="images/3DBundleSeg.png" width="100%">
</p>


6. Delete Label 'button': delete the unwanted detection if it is near the boundary or for any other reason.
7. Calculate measurments 'button': calculate different measurments from the detected bundles and store them in csv file
8. Calculate Bundle Height 'button': compute the 3D distance from the highest point in the 3D detection of each bundle to it's base. This calculation will consider the sample resolution.
9. Perform Cell Clustering 'button': find the IHC, OHC1, OHC2, and OHC3 using either GMM, Kmeans or Deep Learning. Those layers will be added to the plugin to be used during the analysis. 
10. Compute Fluorescence Intensity 'button': produce plots and CSV files that has the accumelated intensity and mean intensity for the fluorescence signal.
11. Predict Region 'button': Predict whether the region is from the BASE, MIDDLE, or APEX region using a RESNET50 trained model. 
12. Compute Orientation: It computes the orientation using two strategies.

<p align="center">
  <strong>Bundle Height with top and bottom adjustable points in red and green, orientation with two points in magenta, and bundle ID in green</strong>  
  <br>
  <img src="images/Bundles.png" width="50%">
</p>

<p align="center">
  <strong>Cell type identification (IHC1 in yellow, OHC1 in cyan, OHC2 in green, and OHC3 in magenta)</strong>  
  <br>
  <img src="images/clustering.png" width="50%">
</p>

13. Training Section.

<p align="center">
  <strong>Training section</strong>  
  <br>
  <img src="images/Training_section2.png" width="40%">
</p>

The training section is for the research ear community incase their datasets are little different than ours then they can easily create their cround truth, train a new model and use it in the plugin
1. Create/Save Ground Truth 'button': this button will create a new layer to draw new ground truth and save them as variables inside the plugin
2. Generate Ground Truth Mask 'button': this button will save all the generated masks after finish annotating to a new folder. 
3. Display Stored Ground Truth 'button': this button will display the stored masks in the plugin.
4. Copy Segmentation Masks to Ground Truth 'button': this button helps in speeding up the annotation process by copying what our trained model is producing sothat the annotator will only correct the wrong part.
5. Move Ground Truth to Training Folder 'button': this button will move all the annotated ground truth to the training folder to start the training process. 
6. Check Training Data 'button': this button checks the training data whether they follow the format needed by the architecture. It checks whether there are training and valiation folders and it reads every single file to make sure it doesn't have redundant or no information. It gives warning messages incase it finds an issue.
7. Train New Model for 3DBundleSeg 'button': this button will start the training.

VASCilia also equipped with two more buttons for resetting (to facilitate transitions between analyzing several stacks) and also exit VASCilia.  
We are still working on the documentation, so this gihub will be continiuosly updated.

## Multi-Batch Processing Feature: Required File
The **Multi-Batch Processing** feature in this package requires an additional file: `track_me_SORT_v3_exe.exe`. This file is **not included** in the repository or the pip installation due to size constraints.
### Download the File
You can download the file from the following link:  
[Download track_me_SORT_v3_exe.exe]*[[https://www.dropbox.com/your-file-link](https://www.dropbox.com/scl/fo/sud3ziayvo7efcsbzgrd7/ACeJ6uMjNLcyk7ev0upJREE?rlkey=e6nzvpz8aoebzq4w3o5f339le&st=1qtmf3mf&dl=0)]
### If You Clone the Repository
1. Download the file from the link above.
2. Place the file in the following directory within the cloned repository: src/napari_vascilia/core/
### If You Installed the Package via pip
1. Download the file from the link above.
2. Locate the installation directory for the package. You can find the installation path by running the following Python code: 
```python
import napari_vascilia
print(napari_vascilia.__file__)
```
3. Place the downloaded file in the following directory: <package_installation_path>/src/napari_vascilia/core/  
Note: All other features of the package will function as expected without this file. This file is exclusively for batch processing of multiple files.

## Testing Other Lab Data  
Liberman Data *[Click me to see a video demo of the entire workflow](https://youtu.be/PIG3q7G6Xr0)*  
Artur Indzhykulian Data *[Click me to see a video demo of the entire workflow](https://youtu.be/WseYK4Zn-3o)*  

## Paper and Citation

This work will be submitted very soon. If you want to read or cite the paper &#128522;, you can find it [here](https://doi.org/10.1101/2024.06.17.599381).  

Kassim, Y. M., Rosenberg, D. B., Renero, A., Das, S., Rahman, S., Al Shammaa, I., Salim, S., Huang, Z., Huang, K., Ninoyu, Y., Friedman, R. A., Indzhykulian, A. A., & Manor, U. (2024). VASCilia (Vision Analysis StereoCilia): A Napari Plugin for Deep Learning-Based 3D Analysis of Cochlear Hair Cell Stereocilia Bundles. bioRxiv. https://doi.org/10.1101/2024.06.17.599381

## Project Authors and Contacts

**Python Implementation of this repository:** Dr. Yasmin M. Kassim    
**Contact:** ykassim@ucsd.edu, ymkgz8@mail.missouri.edu  
Yasmin Kassim was responsible for the plugin design, fully implemented all functions in Python, wrote the manuscript,
proofread the ground truth data, created all figures, and established the GitHub repository and codebase.

**Stacks used in this study imaged by:** Dr. David Rosenberg   

**Height bundle ground truth analyses**: Samprita Das and Alma Renero.  

**StereoCilia Bundles Ground Truth**: 55 (P5 and P21) 3D stacks were manually annotated by Yasmin Kassim and five undergraduate students using the CVAT annotation tool. This is an extremely challenging process, as each 3D stack might have up to 60 bundles in a 3D setting, which could translate to around 1000 bundles in a 2D setting across all frames. The students involved in this effort are:  
**Samia Rahman, Ibraheem Al Shammaa, Samer Salim, Zhuoling Huang, and Kevin Huang**.

This dataset will be the first annotated dataset in the literature to 3D segment the stereocilia bundles and it will be published and available for the ear research community with the publication of this paper.

**Other Lab Support**:   
Yuzuru Ninoyu assisted with some of the imaging data, with Rick Friedman’s supervision and support.   
Artur Indzhykulian provided additional imaging data for testing.  

**Lab Supervisor:** Dr. Uri Manor   
The Principal Investigator, conceived and supervised the project, and provided critical
revisions and updates to the manuscript.  

**Contact:** u1manor@UCSD.EDU  
**Department:** Cell and Development Biology Department/ UCSD  
**Lab Website:** https://manorlab.ucsd.edu/




