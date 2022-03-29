"""Celery app config."""

# Python
import os
from datetime import timedelta


# Django
from django.apps import apps, AppConfig
from django.conf import settings
from django.utils import timezone

# Celery
from celery import Celery, shared_task
from celery.schedules import crontab

# Utils
# from bk_service.utils.enums import PaymentStatus


if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')  # pragma: no cover


app = Celery('bk_service')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


class CeleryAppConfig(AppConfig):
    name = 'bk_service.taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)


# BkCore

@shared_task(name='add_delay_interest_task')
def add_delay_interest_task():
    from bk_service.bk_core_sdk import add_delay_interest
    add_delay_interest()


app.conf.beat_schedule = {
    'disable-finished-rides': {
        'task': 'add_delay_interest_task',
        'schedule': crontab(hour=5, minute=1),
    }
}
