""" Bank models """

# Django
from django.db import models

# Models
# from .banks import Bank

# Utils
from bk_service.utils.models import BkServiceModel
from bk_service.utils.bank_rules_constants import BankRulesConstants

bank_rules = BankRulesConstants()


class BankRules(BkServiceModel, models.Model):
    """ Bank rules model """
    bank = models.ForeignKey('Bank', on_delete=models.PROTECT)

    ordinary_interest = models.DecimalField(max_digits=10, decimal_places=4,
                                            null=False, default=bank_rules.ORDINARY_INTEREST)
    delay_interest = models.DecimalField(max_digits=10, decimal_places=4,
                                         null=False, default=bank_rules.DELAY_INTEREST)
    maximun_credit_installments = models.PositiveIntegerField(
        null=False, default=bank_rules.MAXIMUN_CREDIT_INSTALLMENTS)
    maximun_credit_value = models.DecimalField(
        max_digits=100, decimal_places=4, null=False, default=bank_rules.MAXIMUN_CREDIT_VALUE)
    share_value = models.DecimalField(max_digits=100, decimal_places=4, null=False,
                                      default=bank_rules.SHARE_VALUE)
    maximum_shares_percentage_per_partner = models.DecimalField(
        max_digits=100, decimal_places=4, null=False, default=bank_rules.MAXIMUM_SHARES_PERCENTAGE_PER_PARTNER)
    maximum_active_credits_per_partner = models.DecimalField(
        max_digits=100, decimal_places=4, null=False, default=bank_rules.MAXIMUM_ACTIVE_CREDITS_PER_PARTNER)
    expenditure_fund_percentage = models.DecimalField(
        max_digits=10, decimal_places=4, null=False, default=bank_rules.EXPENDITURE_FUND_PERCENTAGE)
    reserve_fund_of_bad_debt_percentage = models.DecimalField(
        max_digits=10, decimal_places=4, null=False, default=bank_rules.RESERVE_FUND_OF_BAD_DEBT_PERCENTAGE)
    payment_period_of_installment = models.PositiveIntegerField(
        null=False, default=bank_rules.PAYMENT_PERIOD_OF_INSTALLMENT)
    credit_investment_relationship = models.DecimalField(
        max_digits=10, decimal_places=4, null=False, default=bank_rules.CREDIT_INVESTMENT_RELATIONSHIP)

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
        'reserve_fund_of_bad_debt_percentage',
        'payment_period_of_installment',
        'credit_investment_relationship',
    ]
