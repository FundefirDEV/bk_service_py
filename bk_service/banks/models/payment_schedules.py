""" PaymentSchedule models """

# Django
from django.db import models

# Models
from bk_service.banks.models import Bank, Partner

# Utils
from bk_service.requests.models.payment_schedule_request import PaymentScheduleRequest
from bk_service.banks.utils import BankOperationsBaseModel

# Utils enums
from bk_service.utils.enums.requests import CreditPayType


class PaymentSchedule(BankOperationsBaseModel, models.Model):

    payment_schedule_request = models.ForeignKey(PaymentScheduleRequest, on_delete=models.PROTECT)

    amount = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    # (Use create at)
    # date = models.DateTimeField(null=False)
    ordinary_interest_paid = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    delay_interest_paid = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    capital_paid = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    payment_type = models.CharField(max_length=40, null=False, choices=CreditPayType.choices)

    REQUIRED_FIELDS = [
        'bank',
        'partner',
        'payment_schedule_request',
        'amount',
        'ordinary_interest_paid',
        'capital_paid',
        'delay_interest_paid',
        'payment_type',
    ]
