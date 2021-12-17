""" Share models """

# Django
from django.db import models

# Models
from bk_service.banks.models.banks import Bank
from bk_service.banks.models.partners import Partner

# Utils
from bk_service.utils.models import BkServiceModel


class Share(BkServiceModel, models.Model):
    """ Share model """
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT)
    # share_request_id = models.ForeignKey(Request, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(blank=False, default=0.0)
    amount = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
