# Requester
A web application that allows users to create feature requests.

# Instructions

## Requirements
* Linux/MacOS
* Git
* Python 3+ / Pip
* Django 1.8+

## Installation
Open your terminal and clone the repository from here:
```bash
$ git clone git@github.com:alephmelo/requester.git
$ cd requester
$ pip install -r requirements.txt # if you're not in a virtuaelenv, you might need run with sudo.
```

## Create Database
Once you have the requirements installed, we can run the application.
```bash
$ python manage.py migrate
```
This tells Django to run migrations and create our database.

## Run the server
```bash
$ python manage.py runserver
```
```
Performing system checks...

System check identified no issues (0 silenced).
February 24, 2016 - 15:24:45
Django version 1.9.2, using settings 'requester.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Using it

### Local
Just head to `http://127.0.0.1:8000/` and see the application running.

### Cloud (Heroku Server)
If you want to save time and use it right now head to (https://limitless-cove-82744.herokuapp.com/) and voilà.

### To-do
- [x] User model
- [x] User forms
