# DRF Examples

This repository contains code examples of how to use the DRF.

If you need specific code, search for a corresponding branch.

# Tutorial

## Start a new project

You can run `django-admin startproject app .` to create a new project.

For instance, if you run in the current directory, it'll be created a project struct as we have here in the root.

## Start a new app

Run the command `python3 manage.py startapp <myapp>` to create a new app. In the current example, we will create a new app called 'user'

After that, you need to include the app name in the INSTALLED_APPS list, inside the `app/settings.py`

## Creating the Migrations files

If you have any change in the django models, you'll need to create migration files. Django can compare the differences and create them for you with the command `python3 manage.py makemigrations`

## Applying the migration files

You can apply the migrations with the command `python3 manage.py migrate`

## Run the project

`poetry run python3 manage.py runserver`

## Run the project with gunicorn

```
poetry add gunicorn
poetry run gunicorn app.wsgi
```
