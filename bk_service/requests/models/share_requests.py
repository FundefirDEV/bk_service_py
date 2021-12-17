""" Share Requests model """

# Django
from django.db import models

# Request Utils
from bk_service.requests.utils.models import RequestModelBase


class ShareRequest(RequestModelBase, models.Model):
    """ Share Request model"""

    quantity = models.PositiveIntegerField(blank=False, default=0)
