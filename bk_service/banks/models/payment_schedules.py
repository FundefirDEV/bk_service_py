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

    amount = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    date = models.DateTimeField()
    interest_paid = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    capital_paid = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
