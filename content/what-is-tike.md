# What is TIKE?


TIKE stands for the Time series Integrated Knowledge Engine.

TIKE uses a web-based platform, called [JupyterHub](https://jupyter.org/hub), which enables users to run Python Notebooks and other software remotely in a web browser without needing to install anything on your local computer.  Notebooks are a convenient way of packaging code, its outputs, and visualizations.

## Who is TIKE for?

This platform is intended for astronomical researchers who use data products from the NASA Kepler and TESS missions in the Mikulski Archive for Space Telescopes (MAST).

Frequently used Python packages and graphical tools are available, which enable users to preview and make measurements against these data products without needing to download anything.

There are educational tutorials available that demonstrate how to do research with the TESS and Kepler data.  We use git to pull new and updated Notebooks into your user environment, so if you decide to alter these notebooks for your own purposes (and we hope that you do), you should first make a copy for yourself into your own directory.

## Restarting Your Server

The virtual server that runs your personal instance of TIKE will be terminated after ~1 hour of inactivity, and you will be able to restart it the next time you access TIKE.

You can start and stop your computing server any time from the JupyterHub control panel, which can be accessed from the top menu in JupyterLab (<span style="font-variant:small-caps;">file › Hub Control Panel</span>) or the "Home" tab from JupyterHub pages. For example, this may be useful to obtain an updated and unaltered copy of this tike_content repository, or to clear unwanted changes to the included Python environment(s).

## Useful Information

- TIKE is continually maintained and updated, and as such, you should have modest expectations regarding service uptime, data preservation, and other features.

- At this time, no data you upload or create within TIKE is guaranteed to be preserved.  We recommend periodically backing up essential files.

- TIKE is free to use, and users do not require an AWS account to use TIKE or to access STScI's Public Datasets in AWS.

- Several resources are available to support TIKE usage, and we expect more to be added in the coming months. At this time, sources include this TIKE_content Github repository, a copy of which is provided in each user's home directory.

- Usage is monitored, and access will be restricted as needed in order to provide an acceptable level of service to all users.


## More Information

If you are not familiar with Python, or NASA's TESS and Kepler missions, you might find these resources useful:

- [TESS Data Archive at MAST](https://archive.stsci.edu/missions-and-data/tess)
- [TESS Archive Documentation Center](https://outerspace.stsci.edu/display/TESS)
- [TESS Mission Page at MIT](https://tess.mit.edu)
- [Kepler Data Archive at MAST](https://archive.stsci.edu/missions-and-data/kepler)
- [K2 Data Archive at MAST](https://archive.stsci.edu/missions-and-data/k2)
