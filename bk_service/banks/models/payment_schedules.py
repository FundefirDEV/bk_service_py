""" PaymentSchedule models """

# Django
from django.db import models

# Models
from bk_service.banks.models import Bank, Partner

# Utils
from bk_service.utils.models import BkServiceModel
from bk_service.requests.models.payment_schedule_request import PaymentScheduleRequest


class PaymentSchedule(BkServiceModel, models.Model):

    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT)
    payment_schedule_request = models.ForeignKey(PaymentScheduleRequest, on_delete=models.PROTECT)

    amount = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    # (Use create at)
    # date = models.DateTimeField(null=False)
    interest_paid = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    capital_paid = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)

    REQUIRED_FIELDS = [
        'bank',
        'partner',
        'payment_schedule_request',
        'amount',
        'interest_paid'
        'capital_paid'
    ]
