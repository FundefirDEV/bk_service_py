""" Schedule_installment Signals """

# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from bk_service.banks.models import ScheduleInstallment, Bank, Credit

# BkCore
from bk_service.bk_core_sdk.bk_core import BkCore

# Utils
from bk_service.utils.enums.requests import ApprovalStatus

# datetime
from datetime import date


@receiver(post_save, sender=Credit)
def post_save_create_credit_schedule_installment(sender, instance, created, **kwargs):

    if created:
        # TODO add validation for special credit
        # rules
        bank_rules = instance.bank.get_bank_rules()

        # installment_value = total_credit_value % instance.installments (decimal, integer)
        schedule_installments_core = BkCore().calculate_schedule_installment(
            ordinary_interest=bank_rules.ordinary_interest,
            credit_amount=instance.amount,
            installments=instance.installments,
            payment_period_of_installment=bank_rules.payment_period_of_installment,
            payment_type=instance.payment_type
        )

        for schedule_installment in schedule_installments_core:
            schedule = ScheduleInstallment.objects.create(
                credit=instance,
                capital_installment=schedule_installment['capital_value'],
                ordinary_interest_percentage=bank_rules.ordinary_interest,
                interest_calculated=schedule_installment['ordinary_insterest'],
                total_pay_installment=0,
                payment_date=schedule_installment['installment_payment_date'],
                payment_status=ApprovalStatus.pending,
            )
