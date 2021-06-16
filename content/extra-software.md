# How to install extra software?

TIKE provides a rich set of pre-installed software packages which are [listed here](software-installed.md). In addition to these pre-installed packages, it is common for users to install additional software for specific applications. 

Because TIKE creates an isolated environment for every user, installing extra software will only affect your personal instance of TIKE.


## Installing an extra Python package

The easiest way to add a Python package to your TIKE environment is to install it using the `pip` terminal command. You can call this command from a notebook cell by prefixing it with the `!` character, for example:

```
!pip install astropy
```

Would install astropy (which is already installed). To upgrade an existing package, you can add the `--upgrade` flag as follows:

```
!pip install astropy --upgrade
```

These commands will only work for Python packages that have been published on the [Python Package Index](https://pypi.org). If your package has not been published there, you can install it straight from a git repository as follows:

```
!pip install git+https://github.com/astropy/astropy.git 
```

## Installing extra Linux software

JupyterHub also provides access to a Linux terminal (<span style="font-variant:small-caps;">file › new › terminal</span>). From there, you can compile and install additional software.


## Creating a new Python environment

You can create a custom environment for use in Jupyter notebooks using the following four instructions on the command line:

```
python -m venv userenv
source userenv/bin/activate
python -m pip install ipykernel
python -m ipykernel install --user --name=userenv
```

In this example, `userenv` is the arbitrary name of the environment which you can choose.

Having executed these commands, the Jupyter notebook server should automatically recognize the new kernel and offer it as an option.
