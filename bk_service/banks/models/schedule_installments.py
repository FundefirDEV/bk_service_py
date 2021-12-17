""" ScheduleInstallments models """

# Django
from django.db import models

# Models
from bk_service.banks.models.credits import Credit

# Utils
from bk_service.utils.models import BkServiceModel


class ScheduleInstallment(BkServiceModel, models.Model):
    credit = models.ForeignKey(Credit, on_delete=models.PROTECT)
    capital_installment = models.DecimalField(max_digits=100, decimal_places=4)
    ordinary_interest_percentage = models.DecimalField(max_digits=100, decimal_places=4)
    interest_calculated = models.DecimalField(max_digits=10, decimal_places=4)
    total_pay_installment = models.DecimalField(max_digits=100, decimal_places=4)
    payment_date = models.DateTimeField()
    payment_status = models.CharField(max_length=20)
