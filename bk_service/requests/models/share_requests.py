""" Share Requests model """

# Django
from django.db import models

# Request Utils
from bk_service.requests.utils.models import RequestBaseModel


class ShareRequest(RequestBaseModel, models.Model):
    """ Share Request model"""

    quantity = models.PositiveIntegerField(null=False, default=0)
