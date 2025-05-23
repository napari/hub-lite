
## What is the purpose of this tool?

McLabel is a semi-automatic local thresholding tool that can help to label cellular objects such as macrophages in fluorescence microscopy images. In cases where a global threshold does not yield satisfactory results, a local threshold based on a ROI drawn by the user may give better results. See the video for an example:
![Mclabel](./img/Mclabel.gif)



## Installation

The plugin can be installed using pip:
```bash
pip install napari-mclabel
```

After succesfull installation the plugin will appear in the plugins menu of napari.

## Usage

![gui](./img/gui.png)

The GUI of McLabel lives in the right pane of napari. If multiple layers are loaded, select the layer that you want to segment. The theshold finding algorithm is by default is triangle, however there are plenty of alternatives and depending on the data another algorithm might be better suited. 

1. Press "Draw Label"
2. Draw a rough outline around the object of interest. 
3. Press "Compute Label"
4. If not satisfied with result, adjust threshold using the slider
5. Continue with next object

![gui](./img/gui.gif) 

## Reference

If you use McLabel in your work, consider citing our background paper:
https://doi.org/10.1007/978-3-658-41657-7_20



```tex
@InProceedings{10.1007/978-3-658-41657-7_20,
author="Utz, Jonas
and Schlereth, Maja
and Qiu, Jingna
and Thies, Mareike
and Wagner, Fabian
and Brahim, Oumaima B.
and Gu, Mingxuan
and Uderhardt, Stefan
and Breininger, Katharina",
editor="Deserno, Thomas M.
and Handels, Heinz
and Maier, Andreas
and Maier-Hein, Klaus
and Palm, Christoph
and Tolxdorff, Thomas",
title="McLabel",
booktitle="Bildverarbeitung f{\"u}r die Medizin 2023",
year="2023",
publisher="Springer Fachmedien Wiesbaden",
address="Wiesbaden",
pages="82--87",
abstract="In this work, we present a semi-automatic labelling tool for the annotation of complex cellular structures such as macrophages in fluorescence microscopy images. We present McLabel, a napari plugin that allows users to label structures of interest by simply scribbling outlines around the area of interest, using the triangle thresholding method with post-processing to identify the desired structure. Additionally, manual adaption of the threshold allows for quick and fine-grained local correction of the segmentation. The tool is evaluated in a user study with five experts, who annotated images both with and without the tool. The results show that variability in annotations between experts is reduced when the labelling tool is used and annotation time is reduced by a factor of five on average.",
isbn="978-3-658-41657-7"
}
```

