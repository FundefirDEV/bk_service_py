""" Credit Requests model """

# Django
from django.db import models

# Request Utils
from bk_service.requests.utils.models import RequestModelBase

# Utils
from bk_service.utils.enums.requests import CreditUse, CreditUseDetail, CreditPayType


class CreditRequest(RequestModelBase, models.Model):
    """ Credit Request model"""

    installments = models.PositiveIntegerField(blank=False, default=0)
    use = models.CharField(max_length=40, blank=False, choices=CreditUse.choices)
    use_detail = models.CharField(max_length=40, blank=False, choices=CreditUseDetail.choices)
    payment_type = models.CharField(max_length=40, blank=False, choices=CreditPayType.choices)
