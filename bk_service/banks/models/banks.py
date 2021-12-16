""" Bank models """

# Django
from django.db import models

# Models
from bk_service.locations.models.cities import City


class Bank(models.Model):
    """ Bank model """
    name = models.CharField(max_length=30, blank=False, unique=True)
    city = models.ForeignKey(City,  on_delete=models.PROTECT)
    cash_balance = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    active_credits = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    shares = models.IntegerField()
    expense_fund = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    bad_debt_reserve = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)

    # Need one to one relation with bank

    def __str__(self):
        """ Return Bank """
        return str(self.name)

    REQUIRED_FIELDS = ['name', 'city', 'cash_balance', 'active_credits', 'shares', 'expense_fund', ' bad_debt_reserve']
