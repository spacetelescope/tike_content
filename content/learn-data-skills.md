# Learn Light Curve Data Skills
In this set of tutorials we aim to teach you about time series data products and how to manipulate those data to perform common research tasks. The first step is to learn how to retrieve the data or pull down information from the catalog.  If you are not familiar with how to do this using astroquery, start with the [Data Access Tutorials](data-access-skills.md).

A couple of community software packages (lightkurve and eleanor) have wrapped the the MAST API, allowing access to the data wihtout first having to learn the API.  The popular lightkurve module provides a simple method to work with the Kepler, K2 and TESS data without having to first download individual target.

## Intro to Time Series Mission Data Products
These tutorials are designed to show you the content of the TESS and Kepler data products. These tutorials primarily rely on astroquery to retrieve the data and astropy to open the FITS files. In general these missions provide pixel level data contained in target pixel files, photometric time series contained in light curve files and full images of the sky contained in Full Frame Images (FFI). Kepler and TESS also provide data related to the exoplanet transit search called data validation files (DV is the name of the software module that validates an exoplanet found by the transit search).  

For TESS the Full Frame Images are also a time series, so working with the data can be tricky. MAST has provided a tool called TESScut which returns the pixels around a requested star in a target pixel file format. Be sure to use the version of TESScut that accesses the data on the cloud if working in the JupyterHub environment, especially if you plan to do a lot of cutouts, it will be faster. 

- Locate and download a light curve using astroquery. | [TESS]() | [Kepler]()
- Introduction to light curve files |  [TESS](../notebooks/MAST/TESS/beginner_how_to_use_lc/beginner_how_to_use_lc.ipynb) | [Kepler](./notebooks/MAST/Kepler/Kepler_Lightcurve/kepler_lightcurve.ipynb)
- Overview of the Planet Search Data Validation light curve files | [Astroquery Search](./notebooks/blob/master/notebooks/MAST/TESS/beginner_astroquery_dv/beginner_astroquery_dv.ipynb) | [Overview of Contents](./notebooks/MAST/TESS/beginner_how_to_use_dvt/beginner_how_to_use_dvt.ipynb)
- Intro to TESS Full Frame Images (FFI) | [TESS](./notebooks/MAST/TESS/beginner_how_to_use_ffi/beginner_how_to_use_ffi.ipynb)
- Cutting out the FFIs with TESScut | [MAST-hosted TESScut](./notebooks/MAST/TESS/interm_tesscut_astroquery/interm_tesscut_astroquery.ipynb) | [AWS-hosted TESScut]()

## Manipulating Light Curves with Community Software 
A couple of community software packages are available that provide easy ways to retrieve and manipulate time series data. While these are extremely convenient, it can be useful to first understand the basic data products of TESS, as shown above, and by reading the mission documentation. These tools provide wonderful visualizations and are well worth your time to learn.

- Lightkurve: An introduction to the lightcurve objects
- Lightkurve: An introduction to target pixel objects 
- Lighrkurve: How to stitch together data
- Lightkurve: Creating a custom aperture light curve
- Eleanor: Making FFI light curves 
- Eleanor: Pixel-Level Inspection of your data

## Removing Instrumental Systematics
The TESS instrument handbook and the Kepler data characteristics handbook describe a variety of instrumental and data processing systematics that researchers need to be wary of when using these time series data sets. 

- Common detrending techniques
- Co-trending with basis vectors
- Self Flat Fielding
- Pixel Level Decorrelation (PLD)
- Gaussian Processes
- Scattered light

