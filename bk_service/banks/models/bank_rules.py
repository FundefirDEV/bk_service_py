""" Bank models """

# Django
from django.db import models

# Models
from .banks import Bank


class BankRules(models.Model):
    """ Bank rules model """
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    ordinary_interest = models.DecimalField(max_digits=10, decimal_places=4, blank=False, default=0.0)
    delay_interest = models.DecimalField(max_digits=10, decimal_places=4, blank=False, default=0.0)
    maximun_credit_installments = models.IntegerField()
    maximun_credit_value = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    share_value = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    is_active = models.BooleanField()
    expenditure_fund_percentage = models.DecimalField(max_digits=10, decimal_places=4, blank=False, default=0.0)
    reserve_fund_of_bad_debt = models.DecimalField(max_digits=10, decimal_places=4, blank=False, default=0.0)

    # Need one to one relation with bank

    def __str__(self):
        """ Return Bank rules"""
        return str(self.name)

    REQUIRED_FIELDS = ['name', 'city']
