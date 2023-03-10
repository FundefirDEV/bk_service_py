""" Shares Signals """

# Django
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Models
from bk_service.banks.models import PartnerDetail, Bank, Share
from bk_service.requests.models import ShareRequest

# Utils
from bk_service.utils.enums.requests import ApprovalStatus


@receiver(post_save, sender=ShareRequest)
def post_save_approve_share_request(sender, instance, created, **kwargs):

    if created is not True:

        if instance.approval_status == ApprovalStatus.approved:

            partner_detail = instance.partner.partner_detail()
            bank = Bank.objects.get(pk=instance.bank.id)

            share = Share.objects.create(
                bank=bank,
                partner=partner_detail.partner,
                share_request=instance,
                quantity=instance.quantity,
                amount=instance.amount,
            )

            # Update partner detail
            partner_detail.shares += instance.quantity
            partner_detail.save()

            # Update bank
            bank.shares += instance.quantity
            bank.cash_balance += instance.amount
            bank.save()


@receiver(post_delete, sender=Share)
def post_delete_share(sender, instance, **kwargs):

    partner_detail = instance.partner.partner_detail()
    bank = instance.bank

    partner_detail.shares -= instance.quantity
    partner_detail.save()

    bank.shares -= instance.quantity
    bank.cash_balance -= instance.amount

    bank.save()
