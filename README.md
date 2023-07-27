<h1 align="center">Phishing Domain Detection</h1>

This repository contains code for a project that analyzes the features of URLs and domains and predicts whether they are safe or malicious. The project aims to identify and detect malicious URLs and domains commonly associated with phishing attacks.

## Features

The project includes the following features:

* Identification of malicious URLs and domains
* Analysis of the features of URLs and domains
* Visualization of the results of the analysis

## Problem Statement

Phishing is a type of fraud in which attackers impersonate reputable companies or individuals to deceive users and obtain sensitive information such as login credentials or account details. The goal of this project is to predict whether domains are real or malicious, helping users identify potential phishing attempts.

## Project Folder Structure


```
Phishing_Domain_Detection 
├───artifacts
├───build
│   └───lib
│       └───src
│           ├───components
│           ├───configuration
│           ├───constant
│           └───pipeline
├───dist
├───logs
├───notebooks
│   └───data
├───phising_domain_detection.egg-info
├───server
│   ├───static
│   └───templates
|   └───App.py
|   └───feature.py
├───src
│   ├───components
│   │       └───data ingestion.py
|   |       └───data transofrmation,py
|   |       └───model trainer.py
│   ├───configuration
|   |         └───Momgodb_connecntion.py 
│   ├───constant
│   │   └───__pycache__
│   ├───pipeline
|   |        └───__init__.py
|   |        └───Predict Pipeline.py
|   |        └───train_pipeline.py
│   └───__pycache__
└───upload_to_db
└───requirements.txt
└───setup.py
└───setup.cfg

```

## Usage

To use the project, you can follow these steps:

1. Clone the repository to your local machine.
2. Install the dependencies by running the following command:

💿 Installing
1. Environment setup.
```
conda create --prefix venv python==3.9.13 -y
```
```
conda activate venv/
````
2. Install Requirements and setup
```
pip install -r requirements.txt
```
```
python setup.py install
```
5. Run Application
```
python app.py
```

🔧 Built with
- flask
- Python 3.9.13
- Machine learning
- Scikit learn
- 🏦 Industrial Use 

```bash
Authors
```
```
Adarsh Maurya: adarshmsd1@gmail.com
```
```
Sachin Sharma: sharmasachin95880@gmail.com
```
```
Akash Kumar: akasr1603@gmail.com
```
```
Priya Singh : priyasingh2332000@gmail.com
```

## Data
The dataset is taken from Mendeley Data: https://data.mendeley.com/datasets/72ptz43s9v/1
Out of a total 111 features, 25 most important features were used to train the model.


## Results

The project will output a visualization of the results of the analysis. The visualization will show the distribution of the features of the URLs and domains.
The version 0.0.1 (branch adarsh has an accuracy of 96.88% in predicting malicious domains)

## Contributors

This project was created by Adarsh Maurya,  Akash Kumar, Sachin Sharma,Priya Singh.

## Purpose

This project is built as an industrial and real world experience under the ineuron.ai internship.


I hope this helps! Let us know if you have any other questions.
Contact us at
- [adarshmsd1@gmail.com](mailto:adarshmsd1@gmail.com)
- [sharmasachin95880@gmail.com](mailto:sharmasachin95880@gmail.com)
- [akasr1603@gmail.com](mailto:akasr1603@gmail.com)
- [priyasingh2332000@gmail.com](mailto:priyasingh2332000@gmail.com)
