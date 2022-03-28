""" Payment Schedule Signals """

# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from bk_service.banks.models import Bank, PaymentSchedule
from bk_service.requests.models import PaymentScheduleRequest
from bk_service.banks.models.schedule_installments import ScheduleInstallment

# Utils
from bk_service.utils.enums import ApprovalStatus, CreditPayType, PaymentStatus

# Bk Core
from bk_service.bk_core_sdk import BkCore

# Python
from decimal import Decimal


@receiver(post_save, sender=PaymentScheduleRequest)
def post_save_approve_payment_schedule_request(sender, instance, created, **kwargs):

    if created is not True:

        if instance.approval_status == ApprovalStatus.approved:

            bank = Bank.objects.get(pk=instance.bank.id)

            schedule_installment = instance.schedule_installment

            credit = schedule_installment.credit

            bk_core = BkCore()

            # Delay interest
            delay_interest_paid = bk_core.calculate_delay_interest_paid(
                delay_interest_paid=schedule_installment.delay_interest_paid,
                payment_schedule_request_amount=instance.amount,
                delay_interest_calculated=schedule_installment.delay_interest_calculated,
            )

            schedule_installment.delay_interest_paid += Decimal(float(delay_interest_paid))
            schedule_installment.save()

            payment_schedule_request_amount = float(instance.amount) - float(delay_interest_paid)

            # Ordinary interest

            is_payment_advance = (credit.payment_type == CreditPayType.advance)

            ordinary_interest_paid = bk_core.calculate_ordinary_interest_paid(
                amount_paid=schedule_installment.amount_paid,
                payment_schedule_request_amount=payment_schedule_request_amount,
                schedule_installment_interest=schedule_installment.ordinary_interest_calculated,
                is_payment_advance=is_payment_advance
            )

            capital_paid = float(payment_schedule_request_amount) - float(ordinary_interest_paid)

            payment_schedule = PaymentSchedule.objects.create(
                bank=bank,
                partner=instance.partner,
                amount=payment_schedule_request_amount,
                payment_schedule_request=instance,
                ordinary_interest_paid=ordinary_interest_paid,
                capital_paid=capital_paid,
                payment_type=credit.payment_type,
            )

            # Update schedule installment
            schedule_installment.amount_paid += Decimal(payment_schedule_request_amount)

            if schedule_installment.amount_paid >= schedule_installment.total_pay_installment:
                schedule_installment.payment_status = PaymentStatus.complete
                schedule_installment.delay_interest_base_amount = 0.0

            schedule_installment.capital_paid += Decimal(capital_paid)
            schedule_installment.ordinary_interest_paid += Decimal(ordinary_interest_paid)

            # Delay interest
            capital_amount = schedule_installment.capital_installment - Decimal(capital_paid)
            delay_interest_percentage = schedule_installment.delay_interest_percentage
            schedule_installment.delay_interest_base_amount = bk_core.calculate_delay_interest_base_amount(
                capital_amount=capital_amount, delay_interest=delay_interest_percentage)

            schedule_installment.save()

            # Update bank
            bank.cash_balance += Decimal(payment_schedule_request_amount)
            bank.save()

            # Verify if the credit is complete

            schedule_installments_length = len(ScheduleInstallment.objects.filter(
                credit=credit,
                payment_status=ApprovalStatus.pending,
            ))

            if schedule_installments_length == 0:

                credit.is_active = False
                credit.save()
