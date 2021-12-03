# azure-deployment

![Deployment](https://img.shields.io/badge/deployment-passing-brightgreen) ![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![Scikit-Learn](https://img.shields.io/badge/Library-ScikitLearn-orange.svg)

This repository consists of files required for end to end implementation and deployment of deep learning image classification web application created with Flask and deployed on the azure web app service


## About the App
The Minst image Prediction is a flask web application which predicts image classification based on pytorch 

The code is written in Python 3.6.10. If you don't have Python installed, you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Azure
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually to deploy this project.

[![](https://www.onexti.com/wp-content/uploads/2020/08/azure.png)](https://azure.microsoft.com/fr-fr/)

The next step would be to follow the instruction given in the [Azure Documentation](https://docs.microsoft.com/fr-fr/azure/app-service/quickstart-python?tabs=bash&pivots=python-framework-flask) to deploy a web app.

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://miro.medium.com/max/724/1*FCArwuy8wAglYUXp04SN7g.png" width=200>](https://pytorch.org/) 

## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/divyansh1195/Car-Price-Prediction/issues) here by including your search query and the expected result

