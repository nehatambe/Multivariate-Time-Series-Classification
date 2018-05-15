# TimeSeriesClassification

This project implements the code to classify the multivariate time series data generated from sensors using shape mining approach. The code extends the Fast Shapelet Discovery shapelet extraction algorithm to extract the shapelets from multivariate time series data and build a decision tree classifier using extracted shapelets to classify the time series. 

## Prerequisites

You will need the following things properly installed on your computer.
* [Git](https://git-scm.com/)
* [Python](https://www.python.org/downloads/)
* [Visual Studio](https://www.visualstudio.com/downloads/)

## Python libraries
Install libraries - 
Pandas,
Ctypes,
CSV,
OS,
random


## Installation

* `git clone <repository-url>` this repository
* `cd TimeSeriesClassification`

## Running / Development

* Update 'train_file_path', 'test_file_path' variables from the script 'data-processing-list.py' with train and test file path.
* Run following command to preprocess data.
    ``python data-processing-list.py
    ``
* Update 'train_file_path' and 'tree_file_path' variables from the script 'extract-shapelet.py' with train, tree(Intermediate file) file path. Also, update the path to 'ShapeletTest.dll'.
* You can also update the parameters - minLen, maxLen, stepSize, noOfClasses.
* Run following command to extract shapelets from the train dataset data.
    ``python extract-shapelet.py
    ``
* Update 'test_file_path' and 'tree_file_path' variables from the script 'classification.py' with test, tree(Intermediate file) file path. Also, update the path to 'classify.dll'.
* Run following command to classify data from the test dataset data.
    `` python classification.py
    ``



