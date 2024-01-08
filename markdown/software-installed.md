# What software is pre-installed?

TIKE uses the JupyterHub platform to enable Python Notebooks and other software to be used remotely in a web browser without needing to install anything on your local computer.

TIKE comes pre-installed with a set of Python packages and Linux software which are summarized below.


## Pre-installed Python packages

By default, TIKE includes two Python environments, a bare-bones "Python 3" environment and a "TESS" environment containing many packages.  To use the TESS Environment in a notebook, you may have to change the notebook's kernel, either by using the dropdown menu at the upper right of the notebook, or in the top JupyterLab menu (<span style="font-variant:small-caps;">Kernel › Change Kernel...</span>). At this time, the TESS kernel includes the following packages:

* Core scientific packages:
    * numpy
    * scipy 
    * matplotlib
    * pandas
* Core astronomy packages:
    * astropy
    * astroquery
    * pyvo
* TESS-focused packages, like lightkurve
* Cloud tools 
    * awscli 
    * boto3

This list is non-exhaustive. For example, many packages have a significant number of dependencies which are also installed, but are not listed here for the benefit of clarity. You can view the full list of packages installed by inspecting the [TIKE configuration files](https://github.com/spacetelescope/science-platform-images/blob/main/deployments/tike/environments/tess/tess.pip) on GitHub.

## Linux software

JupyterHub also provides access to an Ubuntu Linux terminal (<span style="font-variant:small-caps;">file › new › terminal</span>) from which standard Linux tools can be used.

Commands which work in a terminal can also be used in a Jupyter notebook by prefixing it with the `!` character. For example, the ls and pwd commands can be used by executing `!ls` or `!pwd` in a notebook cell.


## Missing your favorite software?

See also: [How to install extra software?](extra-software.md)

If your favorite software should be part of the default configurationwe encourage you to [open a GitHub issue](https://github.com/spacetelescope/science-platform-images/issues) or contact the [MAST help desk](mailto:archive@stsci.edu) to suggest the package for inclusion. Please include a brief justification explaining the audience and purpose of the software.
