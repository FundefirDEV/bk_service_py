""" users app. """

# Django
from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    """ Users app config """
    name = 'bk_service.users'
    default_auto_field = 'django.db.models.AutoField'
    verbose_name = 'Users'
