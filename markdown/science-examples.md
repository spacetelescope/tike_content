# Example science tutorials

Your TIKE instance comes pre-loaded with tutorials in the `notebooks` folder. You'll also find tutorials from MAST and Hello Universe located in the top-level directory (click the file icon under the search bar).

* [MAST Notebooks](#MAST-Notebooks)
* [Hello Universe Notebooks](#Hello-Universe-Notebooks)

**NOTE!**  In order for these notebooks to access the expected packages in TIKE, you may have to switch to the TESS kernel after you open them.  You can do this either by using the dropdown menu at the upper right of the notebook, or in the top JupyterLab menu (Kernel › Change Kernel...).


# MAST Notebooks

These tutorials are specific to a particular science case and show how to use the MAST programmatic interface and the JupyterHub science platform to do research. The links on this page may only work within the TIKE platform, but you can find external links to the notebooks in GitHub here:  [Example science tutorials (GitHub)](science-examples-github.md).

## Science with TESS

* [Beginner: Read and Plot A TESS Data Validation Timeseries File](../../mast_notebooks-ref/notebooks/TESS/beginner_how_to_use_dvt/beginner_how_to_use_dvt.ipynb)
* [Beginner: Read and Display a TESS Full Frame Image](../../mast_notebooks-ref/notebooks/TESS/beginner_how_to_use_ffi/beginner_how_to_use_ffi.ipynb)
* [Beginner: Read and Plot A TESS Light Curve File](../../mast_notebooks-ref/notebooks/TESS/beginner_how_to_use_lc/beginner_how_to_use_lc.ipynb)
* [Beginner: Read and Display A TESS Target Pixel File](../../mast_notebooks-ref/notebooks/TESS/beginner_how_to_use_tp/beginner_how_to_use_tp.ipynb)
* [Beginner: Search The TESS Input Catalog Centered On HD 209458](../../mast_notebooks-ref/notebooks/TESS/beginner_tic_search_hd209458/beginner_tic_search_hd209458.ipynb)
* [Beginner: A Tour of the Contents of the TESS 2-minute Cadence Data](../../mast_notebooks-ref/notebooks/TESS/beginner_tour_lc_tp/beginner_tour_lc_tp.ipynb)
* [Beginner: Cutout of the TESS FFIs using Astrocut and Astroquery](../../mast_notebooks-ref/notebooks/TESS/interm_tesscut_astroquery/interm_tesscut_astroquery.ipynb)
* [Intermediate: Search and Download GI Program Light Curves](../../mast_notebooks-ref/notebooks/TESS/interm_gi_query/interm_gi_query.ipynb)
* [Intermediate: Create TESS FFI Cutout using Python Requests](../../mast_notebooks-ref/notebooks/TESS/interm_tesscut_requests/interm_tesscut_requests.ipynb)


## Science with Kepler & K2


### Beginner Notebooks

* [Using Kepler Data to Plot a Light Curve](../../mast_notebooks-ref/notebooks/Kepler/plotting_lightcurves/plotting_lightcurves.ipynb)
* [Plotting Images from Kepler Target Pixel Files](../../mast_notebooks-ref/notebooks/Kepler/plotting_images_from_tpf/plotting_images_from_tpf.ipynb)
* [Read and Plot a Kepler Data Validation Timeseries File](../../mast_notebooks-ref/notebooks/Kepler/plotting_dvts/plotting_dvts.ipynb)
* [Plotting a Catalog over a Kepler Full Frame Image File](../../mast_notebooks-ref/notebooks/Kepler/plotting_catalog_over_FFI/plotting_catalog_over_FFI.ipynb)
* [Read and Plot A K2 Light Curve File](../../mast_notebooks-ref/notebooks/K2/Lightcurve/Lightcurve.ipynb)
* [Read and Display A K2 Target Pixel File](../../mast_notebooks-ref/notebooks/K2/TPF/TPF.ipynb)
* [Read and Display a K2 Full Frame Image](../../mast_notebooks-ref/notebooks/K2/beginner_how_to_use_ffi/beginner_how_to_use_ffi.ipynb)


### Working with Lightkurve

* [Using Kepler Light Curve Products with Lightkurve](../../mast_notebooks-ref/notebooks/Kepler/lightkurve_analyzing_lc_products/lightkurve_analyzing_lc_products.ipynb)
* [Using Kepler Target Pixel File Products with Lightkurve](../../mast_notebooks-ref/notebooks/Kepler/lightkurve_analyzing_tpf_products/lightkurve_analyzing_tpf_products.ipynb)
* [Searching for Kepler/K2 and TESS Data Products Using Lightkurve](../../mast_notebooks-ref/notebooks/Kepler/lightkurve_searching_for_data/lightkurve_searching_for_data.ipynb)
* [Creating Your Own Light Curves using Custom Aperture Photometry](../../mast_notebooks-ref/notebooks/Kepler/lightkurve_custom_aperture_photometry/lightkurve_custom_aperture_photometry.ipynb)
* [Combining Multiple Quarters of Kepler Data with Lightkurve](../../mast_notebooks-ref/notebooks/Kepler/lightkurve_combining_multiple_quarters/lightkurve_combining_multiple_quarters.ipynb)
* [Interactively Inspecting Target Pixel Files and Light Curves](../../mast_notebooks-ref/notebooks/Kepler/lightkurve_interactively_inspecting_TPFs_and_LCs/lightkurve_interactively_inspecting_TPFs_and_LCs.ipynb)


### Understanding Instrumental Noise

* [Instrumental Noise in Kepler and K2 #1: Data Gaps and Quality Flags](../../mast_notebooks-ref/notebooks/Kepler/instrumental_noise_1_data_gaps_and_quality_flags/instrumental_noise_1_data_gaps_and_quality_flags.ipynb)
* [Instrumental Noise in Kepler and K2 #2: Spurious Signals and Time Sampling Effects](../../mast_notebooks-ref/notebooks/Kepler/instrumental_noise_2_spurious_signals_and_time_sampling_effects/instrumental_noise_2_spurious_signals_and_time_sampling_effects.ipynb)
* [Instrumental Noise in Kepler and K2 #3: Seasonal and Detector Effects](../../mast_notebooks-ref/notebooks/Kepler/instrumental_noise_3_seasonal_and_detector_effects/instrumental_noise_3_seasonal_and_detector_effects.ipynb)
* [Instrumental Noise in Kepler and K2 #4: Electronic Noise](../../mast_notebooks-ref/notebooks/Kepler/instrumental_noise_4_electronic_noise/instrumental_noise_4_electronic_noise.ipynb)
* [Removing Instrumental Noise from K2 and TESS Light Curves Using Pixel Level Decorrelation (PLD)](../../mast_notebooks-ref/notebooks/K2/removing_instrumental_noise_using_pld/removing_instrumental_noise_using_pld.ipynb)


### Identifying Periodic Signals

* [Identifying Transiting Planet Signals in a Kepler Light Curve](../../mast_notebooks-ref/notebooks/Kepler/identifying_transiting_planet_signals/identifying_transiting_planet_signals.ipynb)
* [Measuring and Removing a Rotation Period Signal from a Kepler Light Curve](../../mast_notebooks-ref/notebooks/Kepler/measuring_a_rotation_period/measuring_a_rotation_period.ipynb)
* [Visualizing Periodic Signals Using a River Plot](../../mast_notebooks-ref/notebooks/Kepler/visualizing_periodic_signals_using_a_river_plot/visualizing_periodic_signals_using_a_river_plot.ipynb)
* [Verifying the Location of a Signal in Kepler Pixel Data](../../mast_notebooks-ref/notebooks/Kepler/verifying_the_location_of_a_signal/verifying_the_location_of_a_signal.ipynb)


### Periodograms & Asteroseismology

* [Creating Periodograms and Identifying Significant Peaks](../../mast_notebooks-ref/notebooks/Kepler/creating_periodograms/creating_periodograms.ipynb)
* [How to Understand and Manipulate the Periodogram of an Oscillating Star](../../mast_notebooks-ref/notebooks/Kepler/how_to_understand_and_manipulate_the_periodogram_of_an_oscillating_star/how_to_understand_and_manipulate_the_periodogram_of_an_oscillating_star.ipynb)
* [How to Estimate a Star's Mass and Radius Using Asteroseismology](../../mast_notebooks-ref/notebooks/Kepler/how_to_estimate_a_stars_mass_and_radius_using_asteroseismology/how_to_estimate_a_stars_mass_and_radius_using_asteroseismology.ipynb)


# Hello Universe

These tutorials are focused on machine learning. In them, you'll learn to use ML for a variety of astronomy use-cases.

* [Predicting Galaxy Redshift With Decision Trees](../../hellouniverse-ref/notebooks/hello-universe/Regressing_3D-HST_galaxy_redshift_with_decision_trees/Regressing_3D-HST_galaxy_redshift_with_decision_trees.ipynb)
* [Classifying PanSTARRS Sources with Unsupervised Learning](../../hellouniverse-ref/notebooks/hello-universe/Classifying_PanSTARRS_sources_with_unsupervised_learning/Classifying_PanSTARRS_sources_with_unsupervised_learning.ipynb)

## Convolutional Neural Networks (CNNs)
* [Classifying Galaxy Mergers with CNNs](../../hellouniverse-ref/notebooks/hello-universe/Classifying_JWST-HST_galaxy_mergers_with_CNNs/Classifying_JWST-HST_galaxy_mergers_with_CNNs.ipynb)
* [Classifying TESS Flares with CNNs](../../hellouniverse-ref/notebooks/hello-universe/Classifying_TESS_flares_with_CNNs/Classifying_TESS_flares_with_CNNs.ipynb)
