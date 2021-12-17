""" Requests models utilities """

# Django
from django.db import models

# Models
from bk_service.banks.models import Bank, Partner

# Utils
from bk_service.utils.enums.requests import ApprovalStatus
from bk_service.utils.models import BkServiceModel


class RequestModelBase(BkServiceModel, models.Model):
    """ Requests base model"""

    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=4, blank=False, default=0.0)
    approval_status = models.CharField(max_length=8, blank=False, choices=ApprovalStatus.choices)
