# Biases in Machine Learning

For this seminar, we will learn how to detect and mitigate biases in machine learning models. This reposity will contain a series of [Jupyter Notebooks](https://jupyter.org/) to give you practical experience in the assesment and mitigation of biases in machine learning models and training datasets.

## Installation Instruction

### Install Anaconda

We will use Anaconda for the management of virtual environments and python package installations. Before getting started with these instructions, download and install [miniconda](https://docs.conda.io/en/latest/miniconda.html) (if you already have full anaconda installed, that will work as well).

### Create Virtual Environment and Install Necessary Python Packages

Run the following commands from your conda terminal.

1. conda create -n bias_notebooks python=3
2. conda activate bias_notebooks
3. conda install -c conda-forge jupyterlab
4. conda install scikit-learn
5. conda install matplotlib
6. conda install pandas
7. conda install seaborn