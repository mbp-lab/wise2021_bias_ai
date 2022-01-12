# Biases in Artificial Intelligence -- Model Interpretability

WiS2021 Bielefeld University

For the last notebook you will need to install two different libraries: [Lime](https://github.com/marcotcr/lime) and [Innvestigate](https://github.com/albermax/innvestigate). 

## Installation Instructions 

### Createa a NEW Virtual Environment and Install Necessary Python Packages

To create a new virtual env for this seminar, run the following commands from your conda terminal. Please make sure to install the libraries in the presented order, otherwise, there might be conflicts.

1. Create a new virtual env eg. named 'ml_bias_interpret' with the specific version of Python3.6:
 	- `conda create -n ml_bias_interpret python=3.6`
2. Activate the new virtual env:
	- `conda activate ml_bias_interpret`
3. Install the required Python packages
	- `conda install -c conda-forge jupyterlab scikit-learn matplotlib pandas seaborn`
4. Install tensorflow first!
	- `conda install -c conda-forge tensorflow=1.14`
5. Install innvestigate 
	- `pip install innvestigate`
6. Install AIF360
	- `pip install aif360[all]`
7. Install Lime 
	- `pip install lime`
    
8. Copy or download the adult dataset to the new environment, as done in the first notebook.
	- The files you need are:
	- https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
	- https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test
	- https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names

	- place them, as-is, in the folder: \envs\ml_bias_interpret\lib\site-packages\aif360\data\raw\adult

	


### Validate Your Virtual Environmenmt Installation

1. Start JupyterLab
	- make sure you virtual env is activated
	- run: `jupyter-lab`
2. Run the `Model_interpretability_Lib_validation` notebook   
3. Run also the `Bias_mitigation_solution` notebook to check if any errors occur 

If any errors will occur, another option would be to use two different environments (AIF360 + lime; innvestigate), since they both will be used independently.
You can also reach out to Tatjana (tmaskaljunas@techfach.uni-bielefeld.de)

