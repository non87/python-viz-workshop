# Python Data Visualization Workshop
Repository for the 2021 Summer Python Visualization Workshop at Northwestern University.

The workshop is divided into four parts. Part 1 is about the fundamental syntax of matplotlib. Part 2 focuses on basic plotting. Part 3 delves deeper in scatter plots. Part 4 is about histograms. 

Part 5 is *not* a Jupyter Notebooks and therefore cannot be run on a Colab. Ideally, it should be run on your Integrated Development Environment (IDE), but the command line will also do. In any case, Part 5 requires `matplotlib` and `pandas` to run -- see instructions below for installing.

The data is contained in the data folder of this repository, but you do not need to download the entire repository to load the data in the code.

## Note on Versioning

This workshop was created using Python 3.9.6, Pandas 1.3.1, numpy 1.21.1 and matplotlib 3.4.2. The code was not tested on any other versions. Therefore, there is no guarantee that the code will work with different versions of the same software. These are the software version that anaconda official channel currently (August 2021) distributes. You can follow the instructions below to install the software on your machine or you can run the code on Google Collaboratory.

## How to Run the Notebooks on Google Colab
The notebooks require `Pandas`, `Matplotlib` and `NumPy`. You can use the Google Collaboratory version of the notebooks. 
To use the colaboratory version, it is sufficient to open click on the following badges, corresponding to the four notebooks composing the workshop:


1.   Part 1 on Colab: <a href="https://colab.research.google.com/github/non87/python-viz-workshop/blob/main/colab/python_viz_1_colab.ipynb" target="_parent"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
2.   Part 2 on Colab: <a href="https://colab.research.google.com/github/non87/python-viz-workshop/blob/main/colab/python_viz_2_colab.ipynb" target="_parent"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
3.   Part 3 on Colab: <a href="https://colab.research.google.com/github/non87/python-viz-workshop/blob/main/colab/python_viz_3_colab.ipynb" target="_parent"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
4.   Part 4 on Colab: <a href="https://colab.research.google.com/github/non87/python-viz-workshop/blob/main/colab/python_viz_4_colab.ipynb" target="_parent"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## How to Run the Notebooks on your Local Machine

You can run the workshop on your local maching by creating a specific Anaconda environment with this line of code:

`conda create -n python_viz_env pandas numpy matplotlib jupyterlab`

To activate the environment, you can use

`conda activate python_viz_env`

After this, you can download the entire repository with the "downloand code" green button on the right-upper corner of the [repository homepage](https://github.com/non87/python-viz-workshop). Finally, you can use Jupyter Notebook or Jupyter Lab (both included with Anaconda) to open the local versions of the notebooks.

The very last part of the workshop cannot be run on Colab, so it may be convenient to run the entire workshop locally.. 

## Solutions to Exercises

You can find the solutions to the exercises in the following links:

1.   [Solution Exercises Part 1](./answer_keys/answer_keys_1.ipynb)
2.   [Solution Exercises Part 2](./answer_keys/answer_keys_2.ipynb)
3.   [Solution Exercises Part 3](./answer_keys/answer_keys_3.ipynb)
4.   [Solution Exercises Part 4](./answer_keys/answer_keys_4.ipynb)

To see how the solutions work, you will have to copy paste the code in the original notebooks: the code will not work in the solutions' notebook.

