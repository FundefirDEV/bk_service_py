""" PaymentSchedule models """

# Django
from django.db import models

# Models

# Utils
from bk_service.utils.models import BkServiceModel


class PaymentSchedule(BkServiceModel, models.Model):
    # payment_schedule_request = models.ForeignKey(ScheduleRequest, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=100, decimal_places=4)
    date = models.DateTimeField()
