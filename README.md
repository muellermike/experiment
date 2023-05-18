# Deploy a Python (Flask) web app to Azure App Service - Sample Application

This is the sample Flask application for the Azure Quickstart [Deploy a Python (Django or Flask) web app to Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python).  For instructions on how to create the Azure resources and deploy the application to Azure, refer to the Quickstart article.

A Django sample application is also available for the article at [https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart).

If you need an Azure account, you can [create on for free](https://azure.microsoft.com/en-us/free/).

# Endpoints
Describes all available endpoints with their use case.

## Userexperiments Controller
### add experiment participation
Use Case: when a user opens the platform a experiment participation is created. This includes defining the exercises to solve for the participant. Random exercises are allocated according to the number of exercises of an experiment.

### update experiment participation
Use Case: when a user finishes the experiment participation the endtime of the experiment can be stored into the database.

### get experiment questions
Use Case: for one specific participation the questions of the related experiment are loaded to be shown to the user.

### get next exercise
Use Case: load a random new exercise for a participation.

## Exercises Controller
### update exercise
Use Case: answer of one exercise can be stored into the database.

`python3 -m venv .venv`
`source .venv/bin/activate`

`pip install -r requirements.txt`

`flask run`