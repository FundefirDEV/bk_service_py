""" Payment Schedule Requests model """

# Django
from django.db import models

# Request Utils
from bk_service.requests.utils.models import RequestBaseModel

# Models
from bk_service.banks.models.schedule_installments import ScheduleInstallment


class PaymentScheduleRequest(RequestBaseModel, models.Model):
    """ Payment Schedule Requests model"""
    schedule_installment = models.ForeignKey(ScheduleInstallment, on_delete=models.PROTECT)
