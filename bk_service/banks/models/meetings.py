""" Meetings models """
# Python
from datetime import datetime
# Django
from django.db import models
from django.utils import timezone

# Models
# from .banks import Bank

# Utils
from bk_service.utils.models import BkServiceModel


class Meeting(BkServiceModel, models.Model):
    """ Bank model """

    # Relations
    bank = models.ForeignKey('Bank', on_delete=models.PROTECT)

    # Integer
    total_shares_quantity = models.PositiveIntegerField(null=False, default=0)
    total_credits_quantity = models.PositiveIntegerField(null=False, default=0)

    # Decimal
    total_shares_amount = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    total_credits_amount = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    total_ordinary_interest = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    total_capital = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    total_delay_interest = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)

    earning_by_share = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    cash_balance = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    expenditure_fund = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    reserve_fund_of_bad_debt = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)

    # Date
    close_date = models.DateTimeField(null=False,)

    def __str__(self):
        """ Return meeting """
        return f'bank: {str(self.bank.name)} meeting_id: {self.id}'

    REQUIRED_FIELDS = [
        'bank',
        'total_shares_amount',
        'total_credits_amount',
        'total_shares_quantity',
        'total_credits_quantity',
        'total_ordinary_interest',
        'total_capital',
        'earning_by_share',
        'total_delay_interest'
        'expenditure_fund',
        'reserve_fund_of_bad_debt',
        'close_date',
    ]
