

This plugin contains two widgets: file watcher and script editor.


## Usage: file watcher

The file watcher monitors a folder and displays its images (tiff, ome-zarr or hdf5) as napari layers, watch the following video for a demo:

[![IMAGE ALT TEXT](http://img.youtube.com/vi/lFRVwlHgJ-Y/0.jpg)](https://www.youtube.com/watch?v=lFRVwlHgJ-Y "Demo napari-file-watcher")

Instructions:

1. Select the folder you want to monitor by pressing "Browse".
2. Select the extension of the files: "zarr", "hdf5" or "tiff".
3. Click "Watch and run" to display the current items & the newly arrived as napari layers.
4. If you click in one of the files of the list, the metadata will show (for hdf5 and zarr)

## Usage: scripting editor

The script editor is for developing scripts and saving them in the filesystem. 
We have used this widget in the context of developing scripts for microscopy control software that implements another file watcher.

Instructions:

1. Select the folder where you want to save your scripts in "Browse".
2. Type the name of the script in the edit box below.
3. Click "Add" for saving it into the folder after typing, or "Open" to display an existing file.

## Installation

You can install `napari-file-watcher` via [pip]:

    pip install napari-file-watcher

Or if you plan to develop it:

    git clone https://github.com/kasasxav/napari-file-watcher
    cd napari-file-watcher
    pip install -e .

If there is an error message suggesting that git is not installed, run `conda install git`.

## Contributing

Contributions are welcome, tests are run with pytest.

## Issues

Issues can be reported at: https://github.com/kasasxav/napari-file-watcher/issues
