""" Bank models """

# Django
from django.db import models

# Models
from bk_service.locations.models.cities import City
from bk_service.banks.models.bank_rules import BankRules
from bk_service.banks.models.meetings import Meeting

# Utils
from bk_service.utils.models import BkServiceModel
from bk_service.utils.constants_errors import *


class Bank(BkServiceModel, models.Model):
    """ Bank model """
    name = models.CharField(
        max_length=30,
        null=False,
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
    cash_balance = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    active_credits = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    shares = models.PositiveIntegerField(null=False, default=0)
    expenditure_fund = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    reserve_fund_of_bad_debt = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)

    # Need one to one relation with bank

    def __str__(self):
        """ Return Bank """
        return str(self.name)

    def get_numbers_of_meets(self):
        try:
            meets = Meeting.objects.filter(bank_id=self.id)
            return len(meets)
        except:
            return 0

    def get_bank_rules(self):
        try:
            bank_rules = BankRules.objects.get(bank_id=self.id, is_active=True)
            return bank_rules
        except:
            return None

    def get_last_meeting(self):
        try:
            meeting = Meeting.objects.get(bank_id=self.id).last()
            return meeting
        except:
            return None

    REQUIRED_FIELDS = ['name', 'city', ]
