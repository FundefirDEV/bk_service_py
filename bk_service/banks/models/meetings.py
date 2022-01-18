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
    total_shares_quantity = models.PositiveIntegerField(null=False, default=0)
    total_credit_quantity = models.PositiveIntegerField(null=False, default=0)

    # Decimal
    total_shares_amount = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    total_credits_amount = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    total_ordinary_interest = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    total_capital = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    total_delay_interest = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)

    earning_by_shares = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    # balance = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    expenditure_fund = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    reserve_fund_of_bad_debt = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)

    def __str__(self):
        """ Return meeting """
        return f'bank: {str(self.bank.name)} meeting_id: {self.id}'

    REQUIRED_FIELDS = [
        'bank',
        'total_shares_amount',
        'total_credits_amount',
        'total_shares_quantity',
        'total_credit_quantity',
        'total_ordinary_interest',
        'total_capital',
        'earning_by_shares',
        'total_delay_interest'
        # 'balance',
        'expenditure_fund',
        'reserve_fund_of_bad_debt'
    ]
