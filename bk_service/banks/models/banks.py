""" Bank models """

# Django
from django.db import models

# Models
from bk_service.locations.models.cities import City

# Utils
from bk_service.utils.models import BkServiceModel
from bk_service.utils.constants_errors import *


class Bank(BkServiceModel, models.Model):
    """ Bank model """
    name = models.CharField(
        max_length=30,
        blank=False,
        unique=True,
        error_messages={
            'required': build_error_message(BANK_NAME_REQUIRED),
            'unique': build_error_message(BANK_NAME_EXIST),
            'invalid': build_error_message(BANK_NAME_INVALID),
        }
    )
    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        error_messages={
            'required': build_error_message(CITY_REQUIRED),
            'invalid': build_error_message(CITY_INVALID),
            'does_not_exist': build_error_message(CITY_INVALID)
        }
    )
    cash_balance = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    active_credits = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    shares = models.PositiveIntegerField(blank=False, default=0)
    expense_fund = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    bad_debt_reserve = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)

    # Need one to one relation with bank

    def __str__(self):
        """ Return Bank """
        return str(self.name)

    REQUIRED_FIELDS = ['name', 'city', ]
