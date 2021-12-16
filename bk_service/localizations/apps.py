""" users app. """

# Django
from django.apps import AppConfig


class LocalizationsAppConfig(AppConfig):
    """ Users app config """
    name = 'bk_service.localizations'
    default_auto_field = 'django.db.models.AutoField'
    verbose_name = 'Localizations'
