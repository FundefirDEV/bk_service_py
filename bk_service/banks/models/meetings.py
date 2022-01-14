""" Meetings models """

# Django
from django.db import models

# Models
# from .banks import Bank

# Utils
from bk_service.utils.models import BkServiceModel


class Meeting(BkServiceModel, models.Model):
    """ Bank model """

    # Relations
    bank = models.ForeignKey('Bank', on_delete=models.PROTECT)

    # (use create at)
    # date_meeting = models.DateTimeField(auto_now_add=True,)

    # Integer
    total_shares = models.PositiveIntegerField(null=False, default=0)

    # Decimal
    total_credit = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    total_ordinary_interest = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    total_capital = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    total_delay_interest = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)

    earning_by_shares = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    balance = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    expenditure_fund = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    reserve_fund_bad_debts = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)

    def __str__(self):
        """ Return meeting """
        return f'bank: {str(self.bank.name)} meeting_id: {self.id}'

    REQUIRED_FIELDS = [
        'bank',
        'total_shares',
        'total_credit',
        'total_ordinary_interest',
        'total_capital',
        'earning_by_shares',
        'balance',
        'expenditure_fund',
        'reserve_fund_bad_debts'
    ]
