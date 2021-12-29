""" Bank models """

# Django
from django.db import models

# Models
from .banks import Bank

# Utils
from bk_service.utils.models import BkServiceModel


class BankRules(BkServiceModel, models.Model):
    """ Bank rules model """
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)

    ordinary_interest = models.DecimalField(max_digits=10, decimal_places=4, blank=False, default=0.0)
    delay_interest = models.DecimalField(max_digits=10, decimal_places=4, blank=False, default=0.0)
    maximun_credit_installments = models.PositiveIntegerField(blank=False, default=0)
    maximun_credit_value = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    share_value = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    maximum_shares_percentage_per_partner = models.DecimalField(
        max_digits=100, decimal_places=4, blank=False, default=0.0)
    maximum_active_credits_per_partner = models.DecimalField(
        max_digits=100, decimal_places=4, blank=False, default=0.0)
    expenditure_fund_percentage = models.DecimalField(max_digits=10, decimal_places=4, blank=False, default=0.0)
    reserve_fund_of_bad_debt = models.DecimalField(max_digits=10, decimal_places=4, blank=False, default=0.0)
    payment_period_of_installment = models.PositiveIntegerField(blank=False, default=0)
    credit_investment_relationchip = models.DecimalField(max_digits=10, decimal_places=4, blank=False, default=0.0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        """ Return Bank rules"""
        return str(self.bank.name)

    REQUIRED_FIELDS = [
        'bank',
        'ordinary_interest',
        'delay_interest',
        'maximun_credit_installments',
        'maximun_credit_value',
        'share_value',
        'maximum_shares_percentage_per_partner',
        'maximum_active_credits_per_partner',
        'is_active',
        'expenditure_fund_percentage',
        'reserve_fund_of_bad_debt',
        'payment_period_of_installment',
        'credit_investment_relationchip',
    ]
