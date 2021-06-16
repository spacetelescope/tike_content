# What software is pre-installed?

TIKE uses the JupyterHub platform to enable Python Notebooks and other software to be used remotely in a web browser without needing to install anything on your local computer.

TIKE comes pre-installed with a set of Python packages and Linux software which are summarized below.


## Pre-installed Python packages

* Core scientific packages:
numpy, scipy, matplotlib, pandas.
* Core astronomy packages:
astropy, astroquery, pyvo.
* Data analysis packages: emcee, george, celerite.
* TESS-focused packages: lightkurve, eleanor, astrocut.
* Machine learning: tensorflow, scikit-learn.
* Cloud tools: awscli, boto3.

Note: you can view the full list of packages installed by inspecting the [TIKE configuration files](https://github.com/spacetelescope/jupyterhub-deploy/tree/main/deployments/tike/image/environments/tess) on GitHub.

## Linux software

JupyterHub also provides access to an Ubuntu Linux terminal (<span style="font-variant:small-caps;">file › new › terminal</span>) from which standard Linux tools can be used.

Commands which work in a terminal can also be used in a Jupyter notebook by prefixing it with the `!` character. For example, the ls and pwd commands can be used by executing `!ls` or `!pwd` in a notebook cell.


## Missing your favorite software?

If a package you need is missing from the configuration, we encourage you to [open a GitHub issue](https://github.com/spacetelescope/jupyterhub-deploy/issues/new) or contact the [MAST help desk](mailto:archive@stsci.edu) to suggest the package for inclusion. Please include a brief justification explaining the purpose of the software.
