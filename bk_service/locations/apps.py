""" Locations app. """

# Django
from django.apps import AppConfig


class LocationsAppConfig(AppConfig):
    """ Locations app config """
    name = 'bk_service.locations'
    default_auto_field = 'django.db.models.AutoField'
    verbose_name = 'Locations'
