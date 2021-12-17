""" Requests app. """

# Django
from django.apps import AppConfig


class RequestsAppConfig(AppConfig):
    """ Requests app config """
    name = 'bk_service.requests'
    default_auto_field = 'django.db.models.AutoField'
    verbose_name = 'Requests'
