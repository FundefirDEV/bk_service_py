""" Credits Signals """

# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from bk_service.banks.models import PartnerDetail, Bank, Credit
from bk_service.requests.models import CreditRequest

# Utils
from bk_service.utils.enums.requests import ApprovalStatus


@receiver(post_save, sender=CreditRequest)
def post_save_approve_credit_request(sender, instance, created, **kwargs):

    if created is not True:

        if instance.approval_status == ApprovalStatus.approved:

            partner_detail = instance.partner.partner_detail()
            bank = Bank.objects.get(pk=instance.bank.id)

            credit = Credit.objects.create(
                bank=bank,
                partner=instance.partner,
                credit_request=instance,
                installments=instance.installments,
                amount=instance.amount,
                credit_use=instance.credit_use,
                credit_use_detail=instance.credit_use_detail,
                payment_type=instance.payment_type
            )

            # Update partner detail
            partner_detail.active_credit += instance.amount
            partner_detail.save()

            # Update bank
            bank.active_credits += instance.amount
            bank.cash_balance -= instance.amount
            bank.save()
