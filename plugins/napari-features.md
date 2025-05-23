
[![License](https://img.shields.io/pypi/l/napari-features.svg?color=green)](https://github.com/0x00b1/napari-features/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-features.svg?color=green)](https://pypi.org/project/napari-features)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-features.svg?color=green)](https://python.org)
[![tests](https://github.com/0x00b1/napari-features/workflows/tests/badge.svg)](https://github.com/0x00b1/napari-features/actions)
[![codecov](https://codecov.io/gh/0x00b1/napari-features/branch/master/graph/badge.svg)](https://codecov.io/gh/0x00b1/napari-features)

An extensible, general-purpose feature extraction plug-in for the [Napari](https://napari.org) image viewer.

## Features

### Color

#### Image

    color_image_integrated_intensity
    color_image_maximum_intensity
    color_image_mean_intensity
    color_image_median_absolute_deviation_intensity
    color_image_median_intensity
    color_image_minimum_intensity
    color_image_quantile_1_intensity
    color_image_quantile_3_intensity
    color_image_standard_deviation_intensity

#### Object

    color_object_center_mass_intensity_x
    color_object_center_mass_intensity_y
    color_object_integrated_intensity
    color_object_integrated_intensity_edge
    color_object_mass_displacement
    color_object_maximum_intensity
    color_object_maximum_intensity_edge
    color_object_maximum_intensity_x
    color_object_maximum_intensity_y
    color_object_mean_intensity
    color_object_mean_intensity_edge
    color_object_median_absolute_deviation_intensity
    color_object_median_intensity
    color_object_median_intensity_edge
    color_object_minimum_intensity
    color_object_minimum_intensity_edge
    color_object_quantile_1_intensity
    color_object_quantile_1_intensity_edge   
    color_object_quantile_3_intensity
    color_object_quantile_3_intensity_edge
    color_object_standard_deviation_intensity
    color_object_standard_deviation_intensity_edge
    Object distribution
    color_object_distribution_coefficient_of_variation_intensity
    color_object_distribution_integrated_intensity
    Color_object_distribution_mean_intensity

### Location

#### Object neighborhood

    location_object_neighborhood_angle
    location_object_neighborhood_closest_0_distance
    location_object_neighborhood_closest_0_object_index
    location_object_neighborhood_closest_1_distance
    location_object_neighborhood_closest_1_object_index
    location_object_neighborhood_closest_2_distance
    location_object_neighborhood_closest_2_object_index
    location_object_neighborhood_neighbors
    location_object_neighborhood_touching

### Metadata

#### Image

    metadata_image_checksum
    metadata_image_filename

#### Layer

    metadata_layer_name
    metadata_layer_type

#### Object

    metadata_object_index

### Shape

#### Image

    shape_image_area

#### Image skeleton

    shape_image_skeleton_branches
    shape_image_skeleton_endpoints
    shape_image_skeleton_length
    shape_image_skeleton_trunks

#### Object

    shape_object_area
    shape_object_bounding_box_area
    shape_object_bounding_box_maximum_x
    shape_object_bounding_box_maximum_y
    shape_object_bounding_box_maximum_z
    shape_object_bounding_box_minimum_x
    shape_object_bounding_box_minimum_y
    shape_object_bounding_box_minimum_z
    shape_object_bounding_box_volume
    shape_object_central_moment_0_0_0
    shape_object_central_moment_0_0_1
    shape_object_central_moment_0_1_2
    shape_object_central_moment_0_1_3
    shape_object_central_moment_1_2_0
    shape_object_central_moment_1_2_1
    shape_object_central_moment_1_3_2
    shape_object_central_moment_1_3_3
    shape_object_central_moment_2_0_0
    shape_object_central_moment_2_0_1
    shape_object_central_moment_2_1_2
    shape_object_central_moment_2_1_3
    shape_object_central_moment_3_2_0
    shape_object_central_moment_3_2_1
    shape_object_central_moment_3_3_2
    shape_object_central_moment_3_3_3
    shape_object_centroid_x
    shape_object_centroid_y
    shape_object_centroid_z
    shape_object_compactness
    shape_object_eccentricity
    shape_object_equivalent_diameter
    shape_object_euler_number
    shape_object_extent
    shape_object_form_factor
    shape_object_hu_moment_0
    shape_object_hu_moment_1
    shape_object_hu_moment_2
    shape_object_hu_moment_3
    shape_object_hu_moment_4
    shape_object_hu_moment_5
    shape_object_hu_moment_6
    shape_object_inertia_tensor_eigenvalues_x
    shape_object_inertia_tensor_eigenvalues_y
    shape_object_inertia_tensor_eigenvalues_z
    shape_object_inertia_tensor_x_x
    shape_object_inertia_tensor_x_y
    Shape_object_inertia_tensor_x_z
    shape_object_inertia_tensor_y_x
    shape_object_inertia_tensor_y_y
    shape_object_inertia_tensor_y_z
    shape_object_inertia_tensor_z_x
    shape_object_inertia_tensor_z_y
    shape_object_inertia_tensor_z_z
    shape_object_major_axis_length
    shape_object_maximum_feret_diameter
    shape_object_maximum_radius
    shape_object_mean_radius
    shape_object_median_radius
    shape_object_minimum_feret_diameter
    shape_object_minor_axis_length
    shape_object_normalized_moment_x_y
    shape_object_orientation
    shape_object_perimeter
    shape_object_solidity
    shape_object_spatial_moment_0_0_0
    shape_object_spatial_moment_0_0_1
    shape_object_spatial_moment_0_1_2
    shape_object_spatial_moment_0_1_3
    shape_object_spatial_moment_1_2_0
    shape_object_spatial_moment_1_2_1
    shape_object_spatial_moment_1_3_2
    shape_object_spatial_moment_1_3_3
    shape_object_spatial_moment_2_0_0
    shape_object_spatial_moment_2_0_1
    shape_object_spatial_moment_2_1_2
    shape_object_spatial_moment_2_1_3
    shape_object_spatial_moment_3_2_0
    shape_object_spatial_moment_3_2_1
    shape_object_spatial_moment_3_3_2
    shape_object_spatial_moment_3_3_3
    shape_object_surface_area
    shape_object_volume
    shape_object_zernike shape features
    Object skeleton
    shape_object_skeleton_endpoints
    shape_object_skeleton_branches
    shape_object_skeleton_length
    shape_object_skeleton_trunks

### Texture

#### Object

    texture_object_haralick_angular_second_moment
    texture_object_haralick_contrast
    texture_object_haralick_coorelation
    texture_object_haralick_sum_of_squares_variance
    texture_object_haralick_inverse_difference_moment
    texture_object_haralick_sum_average
    texture_object_haralick_sum_variance
    texture_object_haralick_sum_entropy
    texture_object_haralick_entropy
    texture_object_haralick_difference_variance
    texture_object_haralick_measure_of_correlation_0
    texture_object_haralick_measure_of_correlation_1
    texture_object_haralick_maximum_correlation_coefficient


