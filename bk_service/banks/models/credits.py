""" Credit models """

# Django
from django.db import models

# Models
from bk_service.banks.models.banks import Bank
from bk_service.banks.models.partners import Partner
from bk_service.requests.models.credit_requests import CreditRequest

# Utils
from bk_service.utils.enums.requests import CreditUse, CreditUseDetail, CreditPayType
from bk_service.utils.models import BkServiceModel


class Credit(BkServiceModel, models.Model):

    # Relations
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT)

    credit_request = models.ForeignKey(CreditRequest, on_delete=models.CASCADE)
    installments = models.PositiveIntegerField(null=False, default=1)
    amount = models.DecimalField(max_digits=100, decimal_places=4)

    credit_use = models.CharField(max_length=40, null=False, choices=CreditUse.choices)
    credit_use_detail = models.CharField(max_length=40, null=False, choices=CreditUseDetail.choices)
    payment_type = models.CharField(max_length=40, null=False, choices=CreditPayType.choices)

    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = [
        'bank',
        'partner',
        'credit_request',
        'installments',
        'amount',
        'credit_use_detail',
        'credit_use'
        'payment_type',
    ]
