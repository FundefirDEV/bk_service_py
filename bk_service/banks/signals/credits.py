""" Credits Signals """

# Django
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Models
from bk_service.banks.models import PartnerDetail, Bank, Credit, ScheduleInstallment
from bk_service.requests.models import CreditRequest

# core
from bk_service.bk_core_sdk.bk_core_sdk import BkCoreSDK, BkCore

# Utils
from bk_service.utils.enums.requests import ApprovalStatus, CreditPayType


@receiver(post_save, sender=CreditRequest)
def post_save_approve_credit_request(sender, instance, created, **kwargs):

    if created is not True:

        if instance.approval_status == ApprovalStatus.approved:

            partner_detail = instance.partner.partner_detail()
            bank = Bank.objects.get(pk=instance.bank.id)
            ordinary_interest = bank.get_bank_rules().ordinary_interest
            total_interest = BkCore().calculate_credit_total_interest(
                amount=instance.amount,
                ordinary_interest=ordinary_interest,
                installments=instance.installments)

            credit = Credit.objects.create(
                bank=bank,
                partner=instance.partner,
                credit_request=instance,
                installments=instance.installments,
                amount=instance.amount,
                credit_use=instance.credit_use,
                credit_use_detail=instance.credit_use_detail,
                payment_type=instance.payment_type,
                total_interest=total_interest)
            BkCoreSDK(partner=instance.partner).update_bank_partner_active_credit(
                credit=credit, ordinary_interest=ordinary_interest)


# @receiver(post_delete, sender=Credit)
# def post_delete_share(sender, instance, **kwargs):

#     partner_detail = instance.partner.partner_detail()
#     bank = instance.bank

#     partner_detail.active_credit -= instance.amount
#     partner_detail.save()

#     if instance.payment_type == CreditPayType.advance:
#         interest = instance.total_interest
#     else:
#         interest = 0

#     bank.cash_balance += (instance.amount - interest)
#     bank.active_credits -= (instance.amount)

#     bank.save()

#     # Delete schedule installments
#     schedule = ScheduleInstallment.objects.filter(credit=instance)
#     schedule.delete()
