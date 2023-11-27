# Creating a Django Project 

## Dependencies
You will need an Intergrated Development Environment such as Vscode.
You must also ensure the latest version of python is installed in your device and properly configured to path.
Make sure you have a virtual environment configured in your device. 
Here we will use *pipenv* to install django together with a virtual environment.

## pipenv

**Pipenv** is a Python virtual environment management tool that supports a multitude of systems and nicely bridges the gaps between *pip*, python, and virtualenv.

Pipenv automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates a project Pipfile.lock, which is used to produce deterministic builds

To install pipenv, go to the terminal and run this command;

`pip install pipenv` or `pip3 install pipenv`

## Create project
Open your IDE, ie. VSCODE

*You can use your terminal or shell*
To creat a **Django Project**, open the terminal and start by changing the directory to the directory you want to use ie, *Desktop*.

`cd Desktop`

While in the directory, create a folder for your project:

`mkdir myproject`

Change the directory to the folder you have created:

`cd myproject`

Once inside the directory you whant to create your project, run the following command;

`pipenv install django`

This command will create a python virtual environment with a django project in it.

To activate the virtual environment run:

`pipenv shell`

To start your first project run;

`django-admin startproject myproject`

*myproject* is any name you want for your project.

Change directory to your project directory;

`cd myproject`

Run the development server;

`py manage.py runserver`

This will start a development sever and you can open the project in your browser at local host port number 8000 by default on address 127.0.0.1

# Create django App

To create a django app run:

`python -m django startapp myapp`

*myapp* is the name for your choice app name.