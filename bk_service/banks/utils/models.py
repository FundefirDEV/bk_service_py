""" Banks models utilities """

# Django
from django.db import models

# Utils
from bk_service.utils.enums.requests import ApprovalStatus
from bk_service.utils.models import BkServiceModel


class BankOperationsBaseModel(BkServiceModel, models.Model):
    """ Bank Operations base model"""

    bank = models.ForeignKey('Bank', on_delete=models.PROTECT)
    partner = models.ForeignKey('Partner', on_delete=models.PROTECT)
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE, null=True)

    class Meta:
        """meta options"""
        abstract = True
