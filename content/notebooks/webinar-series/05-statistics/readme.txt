To install the appropriate packages, open a terminal and run:

PIP_NO_DEPS=1 conda env create -f celerite_docs.yml
conda activate celerite_docs
python -m ipykernel install --user --name=celerite_docs

Then, activate the celerite_docs kernel when running statistics.ipynb. Happy statsing!