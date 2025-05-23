
faser is a Python-based software package designed to simulate the excitation
point spread function (PSF) of optical microscopes. Faser  calculates PSFs for high NA
focusing by using a vectorial model of the electromagnetic field, enabling exploration of the impact
of geometrical and optical parameters on imaging performance in advanced applications. The
software supports various beam profiles, including those used in STED microscopy, and allows for
the simulation of common experimental conditions such as a cranial window and a coverslip tilt.

We provide to prefered ways to use faser:

## Faser as a Napari Plugin

The recommended way to install faser is as a Napari plugin, which provides a user-friendly GUI for interactively exploring the PSF simulation. This can be done via:

```bash
pip install faser napari[pyqt5]
```

#### Usage

You can run the GUI application via (or just as a Napari plugin)

```bash
qtfaser
```

For more information on how to use the GUI, please refer to the [preprint](https://faser.readthedocs.io/en/latest/).

## Faser as a standalone application

Alternatively, you can install the package as a standalone application only, that you can run in enironments without Napari or GUI support:

```bash
pip install faser[cli]
```
This will install the package as a standalone application that can be run from the command line via:

```bash
faser
```
We generally recommend the GUI application for most users, as it provides a more user-friendly interface.
However faser can also be used as a library, and the CLI application is useful for scripting and batch processing.

#### Usage

To simulate the PSF, with a specific numerical aperture (NA) and a beam profile, you can run the following command:

```bash
faser --na 1.4 --window=NO
```

For more information and options you can run:

```bash
faser --help
```

To display the GUI interface and the available options:

```
  __                     
 / _| __ _ ___  ___ _ __ 
| |_ / _` / __|/ _ \ '__|
|  _| (_| \__ \  __/ |   
|_|  \__,_|___/\___|_|   

Generating PSF with config
faser➜  faser git:(master) ✗ uv run faser --help
                                                                                                                                                                                                                                                   
 Usage: faser [OPTIONS]                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                   
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --config                     FILENAME         Path to a JSON file                                                                                                                                                                               │
│ --detector_gaussian_noise    FLOAT            Detector Gaussian noise                                                                                                                                                                           │
│ --gaussian_beam_noise        FLOAT            Gaussian_beam noise                                                                                                                                                                               │
│ --add_noise                  NOISE                                                                                                                                                                                                              │
│ --loaded_phase_mask          OPTIONAL         Loaded Phasemak                                                                                                                                                                                   │
│ --p                          FLOAT            Ratio between Donut (p) and Bottle (1-p) intensity                                                                                                                                                │
│ --mask_offset_y              FLOAT            Y offset of the phase mask in regard to pupil center                                                                                                                                              │
│ --mask_offset_x              FLOAT            X offset of the phase mask in regard to pupil center                                                                                                                                              │
│ --ring_radius                FLOAT            Radius of the ring phase mask (on unit pupil)                                                                                                                                                     │
│ --rc                         FLOAT            Ring charge (should be odd to produce bottle)                                                                                                                                                     │
│ --vc                         FLOAT            Vortex charge (should be integer to produce donut)                                                                                                                                                │
│ --epsilon                    FLOAT            Ellipticity of the polarization (in °)                                                                                                                                                            │
│ --psi                        FLOAT            Direction of the polarization (in °)                                                                                                                                                              │
│ --ampl_offset_y              FLOAT            Y offset of the amplitude profile in regard to pupil center                                                                                                                                       │
│ --ampl_offset_x              FLOAT            X offset of the amplitude profile in regard to pupil center                                                                                                                                       │
│ --waist                      FLOAT            Diameter of the input beam on the objective pupil (in µm)                                                                                                                                         │
│ --wavelength                 FLOAT            Wavelength of light (in µm)                                                                                                                                                                       │
│ --polarization               POLARIZATION                                                                                                                                                                                                       │
│ --mode                       MODE                                                                                                                                                                                                               │
│ --aberration_offset_y        FLOAT            Y offset of the aberration function in regard to pupil center                                                                                                                                     │
│ --aberration_offset_x        FLOAT            X offset of the aberration function in regard to pupil center                                                                                                                                     │
│ --a24                        ABERRATIONFLOAT  Secondary spherical                                                                                                                                                                               │
│ --a12                        ABERRATIONFLOAT  Primary spherical                                                                                                                                                                                 │
│ --a9                         ABERRATIONFLOAT  Oblique Trefoil                                                                                                                                                                                   │
│ --a8                         ABERRATIONFLOAT  Horizontal Coma                                                                                                                                                                                   │
│ --a7                         ABERRATIONFLOAT  Vertical Coma                                                                                                                                                                                     │
│ --a6                         ABERRATIONFLOAT  Vertical Trefoil                                                                                                                                                                                  │
│ --a5                         ABERRATIONFLOAT  Vertical Astigmatism                                                                                                                                                                              │
│ --a4                         ABERRATIONFLOAT  Defocus                                                                                                                                                                                           │
│ --a3                         ABERRATIONFLOAT  Oblique Astigmatism                                                                                                                                                                               │
│ --a2                         ABERRATIONFLOAT  Horizontal Tilt                                                                                                                                                                                   │
│ --a1                         ABERRATIONFLOAT  Vertical Tilt                                                                                                                                                                                     │
│ --a0                         ABERRATIONFLOAT  Piston                                                                                                                                                                                            │
│ --wind_offset_y              FLOAT            Y offset of the cranial window in regard to pupil center                                                                                                                                          │
│ --wind_offset_x              FLOAT            X offset of the cranial window in regard to pupil center                                                                                                                                          │
│ --wind_depth                 FLOAT            Depth of the cranial window (in mm)                                                                                                                                                               │
│ --wind_radius                FLOAT            Diameter of the cranial window (in mm)                                                                                                                                                            │
│ --window                     WINDOW                                                                                                                                                                                                             │
│ --tilt                       FLOAT            Tilt angle of the coverslip (in °)                                                                                                                                                                │
│ --depth                      FLOAT            Imaging depth in the sample (in µm)                                                                                                                                                               │
│ --collar                     FLOAT            Correction collar setting to compensate coverslip thickness                                                                                                                                       │
│ --thickness                  FLOAT            Thickness of the coverslip (in µm)                                                                                                                                                                │
│ --n3                         FLOAT            Refractive index of the sample                                                                                                                                                                    │
│ --n2                         FLOAT            Refractive index of the coverslip                                                                                                                                                                 │
│ --n1                         FLOAT            Refractive index of the immersion medium                                                                                                                                                          │
│ --wd                         FLOAT            Working Distance of the objective lens (in µm)                                                                                                                                                    │
│ --na                         FLOAT            Numerical Aperture of Objective Lens                                                                                                                                                              │
│ --normalize                  NORMALIZE                                                                                                                                                                                                          │
│ --nphi                       INTEGER          Integration sted of the aximutal angle on the pupil                                                                                                                                               │
│ --ntheta                     INTEGER          Integration sted of the focalization angle                                                                                                                                                        │
│ --nz                         INTEGER          Discretization of Z axis - better be odd number for perfect 0                                                                                                                                     │
│ --nxy                        INTEGER          Discretization of image plane - better be odd number for perfect 0                                                                                                                                │
│ --l_obs_z                    FLOAT            Observation scale in Z (in µm)                                                                                                                                                                    │
│ --l_obs_xy                   FLOAT            Observation scale in XY (in µm)                                                                                                                                                                   │
│ --help                                        Show this message and exit.                                                                                                                                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```


