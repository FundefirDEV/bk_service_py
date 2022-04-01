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


@receiver(post_save, sender=Credit)
def post_save_create_credit_schedule_installment(sender, instance, created, **kwargs):

    if created:
        # normal credit schedule installment creation
        if instance.is_special == False: 
            bank_rules = instance.bank.get_bank_rules()
            # installment_value = total_credit_value % instance.installments (decimal, integer)
            schedule_installments_core = BkCore().calculate_schedule_installment(
                ordinary_interest=bank_rules.ordinary_interest,
                delay_interest=bank_rules.delay_interest,
                credit_amount=instance.amount,
                installments=instance.installments,
                payment_period_of_installment=bank_rules.payment_period_of_installment,
                payment_type=instance.payment_type
            )

            for index, schedule_installment in enumerate(schedule_installments_core):
                schedule = ScheduleInstallment.objects.create(
                    credit=instance,
                    capital_installment=schedule_installment['capital_value'],
                    ordinary_interest_percentage=bank_rules.ordinary_interest,

                    # TODO: calculate deplay interest
                    delay_interest_percentage=bank_rules.delay_interest,
                    delay_interest_base_amount=schedule_installment['delay_interest_base_amount'],

                    ordinary_interest_calculated=schedule_installment['ordinary_insterest'],
                    total_pay_installment=schedule_installment['capital_value'] +
                    schedule_installment['ordinary_insterest'],
                    payment_date=schedule_installment['installment_payment_date'],
                    payment_status=ApprovalStatus.pending,
                    installment_number=index
                )
