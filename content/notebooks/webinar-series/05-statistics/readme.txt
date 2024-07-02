To install the appropriate packages, open a terminal and run:

kernel-create celerite_docs
source kernel-activate celerite_docs
conda install celerite_docs.yml --no-deps
PIP_NO_DEPS=1 conda env create -f celerite_docs.yml
conda activate celerite_docs
python -m ipykernel install --user --name=celerite_docs

Then, activate the celerite_docs kernel when running statistics.ipynb. Happy statsing!