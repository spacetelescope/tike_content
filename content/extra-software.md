# How to install extra software?

TIKE provides a rich set of pre-installed software packages which are [listed here](software-installed.md). Users are invited to suggest additional packages to be added by contacting the [MAST help desk](mailto:archive@stsci.edu). Pre-installed packages are carefully tested for compatibility with the environment.

While pre-installation is the preferred method, users may occasionally wish to install extra software to meet the need of their scientific applications. This page summarizes a few options for doing so.

**Caution:** installing extra software may alter the functionality of your environment. Proceed at your own risk. Fortunately, TIKE creates an isolated environment for each individual user, so you will not be able to harm the platform for others.



## Installing an extra Python package

The easiest way to add a Python package to your TIKE environment is to install it using the `pip` terminal command. You can call this command from a notebook cell by prefixing it with the `!` character, for example:

```
!pip install astropy
```

To upgrade an existing package that is already installed, you will need to add the `--upgrade` flag:

```
!pip install astropy --upgrade
```

These commands will only work for Python packages that have been published on the [Python Package Index](https://pypi.org). If a package has not been published there, you can install it straight from a git repository as follows:

```
!pip install git+https://github.com/astropy/astropy.git
```


## Creating a new Python environment

The `pip` command demonstrate above will alter the Python environment that is running your notebook. To avoid altering the default environment, it is often desirable to install packages in a custom environment.  Furthermore, TIKE provides a pre-specified Python environment that refreshes each time the computing server is restarted. While it is possible to temporarily update the TIKE environments using pip or conda commands during a session, as described above, such changes will not persist after the notebook server is restarted.

You can create a custom, persistent Python notebook environment on TIKE by entering the following commands in a terminal (<span style="font-variant:small-caps;">file › new › terminal</span>):

```
python -m venv userenv
source userenv/bin/activate
```

In this example, `userenv` is the arbitrary name of the environment. You can choose a different name.

Next, you need to register the new Python environment for use in your instance of TIKE's Jupyter notebook server. This can be done using the `ipykernel` tool as follows:

```
python -m pip install ipykernel
python -m ipykernel install --user --name=userenv
```

Having executed these commands, the Jupyter notebook server should automatically recognize the new kernel and offer it as an option.


## Creating a new Anaconda environment

 In addition to creating a new persistent Python virtual environment as described above, it is also possible to create a custom Anaconda or Miniconda environment in your TIKE home directory (`/home/jovyan`). This can be done either by using the built-in conda or by uploading and running the appropriate conda installation script into TIKE. To create a new persistent conda environment, you can use the `prefix` option with conda:
 ```
 conda create --prefix=/home/jovyan/mycondaenv python=3.10
 conda activate /home/jovyan/mycondaenv
 ```

 To use one of these new environments in notebooks, similar to the above, you will need to register it in your instance of TIKE's Jupyter notebook server:
 ```
 pip install ipykernel
 python -m ipykernel install --user --name=mycondaenv
 ```

## Installing extra Linux software

JupyterHub provides access to a Linux terminal (<span style="font-variant:small-caps;">file › new › terminal</span>). From there, you can download and compile additional software in the home directory of the JupyterHub instance (`/home/jovyan`).
