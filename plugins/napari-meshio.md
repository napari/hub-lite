
[![License MIT](https://img.shields.io/pypi/l/napari-meshio.svg?color=green)](https://github.com/GenevieveBuckley/napari-meshio/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-meshio.svg?color=green)](https://pypi.org/project/napari-meshio)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-meshio.svg?color=green)](https://python.org)
[![tests](https://github.com/GenevieveBuckley/napari-meshio/workflows/tests/badge.svg)](https://github.com/GenevieveBuckley/napari-meshio/actions)
[![codecov](https://codecov.io/gh/GenevieveBuckley/napari-meshio/branch/main/graph/badge.svg)](https://codecov.io/gh/GenevieveBuckley/napari-meshio)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-meshio)](https://napari-hub.org/plugins/napari-meshio)

This napari plugin uses [meshio](https://github.com/nschloe/meshio) to read and write mesh files to surfaces in napari.

![Screenshot: Stanford bunny example data in napari](assets/bunny-screenshot.png)

*Image caption: screenshot of the [Stanford bunny](http://graphics.stanford.edu/data/3Dscanrep/) example surface mesh open in napari.*

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

- [Installation](#installation)
- [How to use napari-meshio](#how-to-use-napari-meshio)
    - [Read surface data from file](#read-surface-data-from-file)
    - [Open example surface data](#open-example-surface-data)
    - [Save surface data](#save-surface-data)
    - [Supported mesh file formats](#supported-mesh-file-formats)
- [Contributing](#contributing)
- [License](#license)
- [Issues](#issues)

## Installation

You can install `napari-meshio` via [pip]:

    pip install napari-meshio



To install latest development version :

    pip install git+https://github.com/GenevieveBuckley/napari-meshio.git


## How to use napari-meshio

### Read surface data from file

Drag and drop the file onto the napari viewer.

*Note: [Here](https://people.sc.fsu.edu/~jburkardt/data/ply/ply.html) are a number of `.ply` example files you can download to try, like [this airplane](https://people.sc.fsu.edu/~jburkardt/data/ply/airplane.ply) (see [image](https://people.sc.fsu.edu/~jburkardt/data/ply/airplane.png)).*

### Open example surface data

Launch the napari viewer, then open one of the sample datasets (eg: the [Stanford bunny](http://graphics.stanford.edu/data/3Dscanrep/)) from the file menu:

`File` > `Open Sample` > `napari-meshio` > `bunny`

Or, open sample data from python with:

```python
import napari

viewer = napari.Viewer(ndisplay=3)
viewer.open_sample('napari-meshio', 'bunny')
```

### Save surface data

To save a surface layer, click the layer name to select it, and then choose save from the file menu:

`File` > `Save selected layer(s)`

You can also use keyboard shortcuts to save the selected surface layer:
- Windows/Linux: `Control` + `S`
- Mac: `⌘` + `S`

Or, save surface layers from python with:
```python
filename = "bunny.stl"
viewer.layers['bunny'].save(filename)
```
*Note: this code example assumes you have the Stanford bunny example dataset loaded.*

A [wide variety of surface mesh file formats are supported](#supported-mesh-file-formats) by
[meshio](https://github.com/nschloe/meshio).
If no file extension is provided when saving a surface layer,
the default is the `.ply` polygon file format.

### Supported mesh file formats

*Note: Only triangular mesh faces are supported by napari.*

The [meshio](https://github.com/nschloe/meshio) library documentation describes the supported file formats:

> There are various mesh formats available for representing unstructured meshes.
meshio can read and write all of the following and smoothly converts between them:
>
>> [Abaqus](http://abaqus.software.polimi.it/v6.14/index.html) (`.inp`),
>> ANSYS msh (`.msh`),
>> [AVS-UCD](https://lanl.github.io/LaGriT/pages/docs/read_avs.html) (`.avs`),
>> [CGNS](https://cgns.github.io/) (`.cgns`),
>> [DOLFIN XML](https://manpages.ubuntu.com/manpages/jammy/en/man1/dolfin-convert.1.html) (`.xml`),
>> [Exodus](https://nschloe.github.io/meshio/exodus.pdf) (`.e`, `.exo`),
>> [FLAC3D](https://www.itascacg.com/software/flac3d) (`.f3grid`),
>> [H5M](https://www.mcs.anl.gov/~fathom/moab-docs/h5mmain.html) (`.h5m`),
>> [Kratos/MDPA](https://github.com/KratosMultiphysics/Kratos/wiki/Input-data) (`.mdpa`),
>> [Medit](https://people.sc.fsu.edu/~jburkardt/data/medit/medit.html) (`.mesh`, `.meshb`),
>> [MED/Salome](https://docs.salome-platform.org/latest/dev/MEDCoupling/developer/med-file.html) (`.med`),
>> [Nastran](https://help.autodesk.com/view/NSTRN/2019/ENU/?guid=GUID-42B54ACB-FBE3-47CA-B8FE-475E7AD91A00) (bulk data, `.bdf`, `.fem`, `.nas`),
>> [Netgen](https://github.com/ngsolve/netgen) (`.vol`, `.vol.gz`),
>> [Neuroglancer precomputed format](https://github.com/google/neuroglancer/tree/master/src/neuroglancer/datasource/precomputed#mesh-representation-of-segmented-object-surfaces),
>> [Gmsh](https://gmsh.info/doc/texinfo/gmsh.html#File-formats) (format versions 2.2, 4.0, and 4.1, `.msh`),
>> [OBJ](https://en.wikipedia.org/wiki/Wavefront_.obj_file) (`.obj`),
>> [OFF](https://segeval.cs.princeton.edu/public/off_format.html) (`.off`),
>> [PERMAS](https://www.intes.de) (`.post`, `.post.gz`, `.dato`, `.dato.gz`),
>> [PLY](<https://en.wikipedia.org/wiki/PLY_(file_format)>) (`.ply`),
>> [STL](<https://en.wikipedia.org/wiki/STL_(file_format)>) (`.stl`),
>> [Tecplot .dat](http://paulbourke.net/dataformats/tp/),
>> [TetGen .node/.ele](https://wias-berlin.de/software/tetgen/fformats.html),
>> [SVG](https://www.w3.org/TR/SVG/) (2D output only) (`.svg`),
>> [SU2](https://su2code.github.io/docs_v7/Mesh-File/) (`.su2`),
>> [UGRID](https://www.simcenter.msstate.edu/software/documentation/ug_io/3d_grid_file_type_ugrid.html) (`.ugrid`),
>> [VTK](https://vtk.org/wp-content/uploads/2015/04/file-formats.pdf) (`.vtk`),
>> [VTU](https://vtk.org/Wiki/VTK_XML_Formats) (`.vtu`),
>> [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) ([TIN](https://en.wikipedia.org/wiki/Triangulated_irregular_network)) (`.wkt`),
>> [XDMF](https://xdmf.org/index.php/XDMF_Model_and_Format) (`.xdmf`, `.xmf`).

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-meshio" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/GenevieveBuckley/napari-meshio/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.
