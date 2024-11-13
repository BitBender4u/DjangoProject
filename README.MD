## DJANGO
- This is a python web framework (A software framework that simplifies the development of web apps by providing a
structure  and common components (tools and libs to handle common web dev tasks


1. Routing : mapping url routes to various pages or functionalities
2. Authentication : authorisation, identity
3. Database integration and interruption
4. Session management
5. Form handling


## Examples of web frameworks
** Backend frameworks **
1. Nodejs
2. Python(Flask and Django)
3.PHP (Laravel)
4. Ruby on rails
GO (GIN, ECHO)

** Front end frameworks **
1. React js
2. Next js
3. Angular
4. Vue

## A Django website
- Consists of a single project, that is then split into separate apps.
- Django apps are structured to separate logic and pieces
- Django supports the architecturial pattern of MVC
    Models:
    Views:
    Controllers:

## Tools to work with Django
1. python
2. pip

## How to create django projects
django-admin startproject PROJECTNAME

## How to run the django server
- cd PROJECTNAME
- Python manage.py runserver

## How to add an app
- python manage.py startapp "appname"
- Register the app to the project, in settings.py on project folder add it to the installed apps list

## How to map models to dbs tables (applying migration)
1. Define the model
2. Make the migration (python manage.py makemigrations)
3. Apply the migration (python manage.py migrate)