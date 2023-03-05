from django.apps import AppConfig

#This class allows to create the default auto-increment behaviour on the app blogapp, we will use it in the settings.py from project
class BlogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapp'
