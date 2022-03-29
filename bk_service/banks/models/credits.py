""" Credit models """

# Django
from django.db import models

# Models
from bk_service.requests.models.credit_requests import CreditRequest

# Utils
from bk_service.utils.enums.requests import CreditUse, CreditUseDetail, CreditPayType
from bk_service.banks.utils import BankOperationsBaseModel


class Credit(BankOperationsBaseModel, models.Model):

    # Relations
    credit_request = models.ForeignKey(CreditRequest, on_delete=models.CASCADE)

    installments = models.PositiveIntegerField(null=False, default=1)
    amount = models.DecimalField(max_digits=100, decimal_places=4)

    credit_use = models.CharField(max_length=40, null=False, choices=CreditUse.choices)
    credit_use_detail = models.CharField(max_length=40, null=False, choices=CreditUseDetail.choices)
    payment_type = models.CharField(max_length=40, null=False, choices=CreditPayType.choices)

    # TODO: add this field in signal
    total_interest = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)

    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = [
        'bank',
        'partner',
        'credit_request',
        'installments',
        'amount',
        'credit_use_detail',
        'credit_use',
        'payment_type',
    ]

    def __str__(self):
        """ return credit info """

        return str(f'{self.bank.name} : {self.partner}')
