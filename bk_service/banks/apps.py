""" banks app. """

# Django
from django.apps import AppConfig


class BanksAppConfig(AppConfig):
    """ Users app config """
    name = 'bk_service.banks'
    default_auto_field = 'django.db.models.AutoField'
    verbose_name = 'Banks'
