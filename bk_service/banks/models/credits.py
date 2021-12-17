""" Credit models """

# Django
from django.db import models

# Models
from bk_service.banks.models.banks import Bank
from bk_service.banks.models.partners import Partner

# Utils
from bk_service.utils.models import BkServiceModel


class Credit(BkServiceModel, models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT)
    # credit_request = models.ForeignKey(CreditRequest, on_delete=models.CASCADE)
    installments = models.PositiveIntegerField(blank=False, default=1)
    amount = models.DecimalField(max_digits=100, decimal_places=4)
