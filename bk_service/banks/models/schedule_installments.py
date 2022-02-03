""" ScheduleInstallments models """

# Django
from django.db import models

# Utils
from bk_service.utils.models import BkServiceModel
from bk_service.utils.enums import PaymentStatus


class ScheduleInstallment(BkServiceModel, models.Model):
    credit = models.ForeignKey('Credit', on_delete=models.PROTECT, related_name='schedule_installments')
    capital_installment = models.DecimalField(max_digits=100, decimal_places=4, null=False)
    ordinary_interest_percentage = models.DecimalField(max_digits=100, decimal_places=4, null=False)
    interest_calculated = models.DecimalField(max_digits=10, decimal_places=4, null=False)
    total_pay_installment = models.DecimalField(max_digits=100, decimal_places=4, null=False)
    amount_paid = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)

    capital_paid = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    ordinary_interest_paid = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    delay_interest_paid = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)

    payment_date = models.DateTimeField(null=False)

    payment_status = models.CharField(
        max_length=20,
        null=False,
        choices=PaymentStatus.choices,
        default=PaymentStatus.pending
    )

    REQUIRED_FIELDS = [
        'credit',
        'capital_installment',
        'payment_date'
        'ordinary_interest_percentage',
        'interest_calculated',
        'total_pay_installment',
        'payment_status',
        'ordinary_interest_paid',
        'amount_paid',
        'capital_paid',
        'delay_interest_paid',
    ]

    def __str__(self):
        """ return ScheduleInstallment info """
        info = {
            'credit': self.credit,
            'capital_installment': self.capital_installment,
            'payment_date': self.payment_date,
            'ordinary_interest_percentage': self.ordinary_interest_percentage,
            'interest_calculated': self.interest_calculated,
            'total_pay_installment': self.total_pay_installment,
            'payment_status': self.payment_status,
            'amount_paid': self.amount_paid,
            'ordinary_interest_paid': self.ordinary_interest_paid,
            'capital_paid': self.capital_paid,
            'delay_interest_paid': self.delay_interest_paid,
        }

        return str(info)
