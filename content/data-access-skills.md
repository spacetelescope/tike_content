# Data and Catalog Access Skills
The MAST provides various access points to the mission catalogs and data products. These tutorials introduce you to some of these products.

## Selecting Targets from the TESS Input Catalog
The easiest way to work with TESS data is to first determine the TESS Input Catalog ID number that is associated with the target since those numbers are used to name many of the data products. For more information on the TESS Input Catalog see this [overview](https://heasarc.gsfc.nasa.gov/docs/tess/tess-input-catalog-version-8-tic-8-is-now-available-at-mast.html) and the [release notes](https://outerspace.stsci.edu/display/TESS/TIC+and+CTL+Data+Release+Notes+Home+Page).

The TESS Input catalog is available through various services. For simple queries use the Python package astroquery. For more complicated queries, Table Access Protocal (TAP) access or [CASJobs](http://mastweb.stsci.edu/mcasjobs/) may be more appropriate. These last two allow you to do more SQL-like database queries on the table.

- Learn how to access the TESS Input Catalog with astroquery | [TIC Search](../notebooks/MAST/TESS/beginner_tic_search_hd209458/beginnner_tic_search_hd209458.ipynb)
- Accessing the TIC using TAP and the Virtual Observatory's PyVO package | []()
- Searching by Footprint using GSSC

## Using Astroquery to Locate and Download Data Files
Astroquery is community led software that allows direct access to the MAST central database of observations. With a few functions you can filter the observations and locate data of interest at MAST.  Here we explore the basic process to download the different types of Kepler and TESS data products, including some of the populare community delivered light curves.

- Download light curve and target pixel files for one target | [TESS]() [Kepler]()
- Locate planet search data products (DV) for one target | [TESS]() [Kepler]()
- Use Bulk Downloads to retriev all the data for one TESS Camera.