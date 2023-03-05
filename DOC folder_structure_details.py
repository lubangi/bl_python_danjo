# The outer mysite/ directory is the container for our project. It contains the following files:

# • manage.py: This is a command-line utility used to interact with your project. You don’t need
# to edit this file.


# • mysite/: This is the Python package for your project, which consists of the following files:
# __init__.py: An empty file that tells Python to treat the mysite directory as a Python module.


# asgi.py: This is the configuration to run your project as an Asynchronous Server Gateway Interface (ASGI) application with ASGI-compatible web servers. ASGI is the emerging Python standard for asynchronous web servers and applications.


# settings.py: This indicates settings and configuration for your project and contains initial default settings.


# urls.py: This is the place where your URL patterns live. Each URL defined here is mapped to a view.


# wsgi.py: This is the configuration to run your project as a Web Server Gateway Inter- face (WSGI) application with WSGI-compatible web servers.


# applicaction

# __init__.py: An empty file that tells Python to treat the blog directory as a Python module. admin.py: This is where you register models to include them in the Django administration
# site—using this site is optional.
# apps.py: This includes the main configuration of the blog application.
# migrations: This directory will contain database migrations of the application. Migrations allow Django to track your model changes and synchronize the database accordingly. This directory contains an empty __init__.py file.
# models.py: This includes the data models of your application; all Django applications need to have a models.py file but it can be left empty.
# tests.py: This is where you can add tests for your application.
# views.py: The logic of your application goes here; each view receives an HTTP request, pro-
# cesses it, and returns a response.


# note : to exit the python shell :
# ctrl+d or exit()