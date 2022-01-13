""" Credit Requests model """

# Django
from django.db import models

# Request Utils
from bk_service.requests.utils.models import RequestModelBase

# Utils
from bk_service.utils.enums.requests import CreditUse, CreditUseDetail, CreditPayType


class CreditRequest(RequestModelBase, models.Model):
    """ Credit Request model"""

    installments = models.PositiveIntegerField(null=False, default=0)
    credit_use = models.CharField(max_length=40, null=False, choices=CreditUse.choices)
    credit_use_detail = models.CharField(max_length=40, null=False, choices=CreditUseDetail.choices)
    payment_type = models.CharField(max_length=40, null=False, choices=CreditPayType.choices)
