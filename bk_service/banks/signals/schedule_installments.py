""" Schedule_installment Signals """

# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from bk_service.banks.models import ScheduleInstallment, Bank, Credit

# Utils
from bk_service.utils.enums.requests import ApprovalStatus

# datetime
from datetime import date


@receiver(post_save, sender=Credit)
def post_save_create_credit_schedule_installment(sender, instance, created, **kwargs):

    if created:
        # TODO add validation for special credit
        # installment
        bank_rules = instance.bank.get_bank_rules()
        # calculate capital_installment, ordinary_interest_percentage, interest_calculated

        schedule_installment = ScheduleInstallment.objects.create(
            credit=instance,
            capital_installment=0
            ordinary_interest_percentage=0,
            interest_calculated=0,
            total_pay_installment=0,
            payment_date=date.today(),
            payment_status=ApprovalStatus.pending,
        )

        # # Update partner detail
        # partner_detail.active_credit += instance.amount
        # partner_detail.save()

        # # Update bank
        # bank.active_credits += instance.amount
        # bank.cash_balance -= instance.amount
        # bank.save()
