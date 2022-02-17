""" Shares Signals """

# Django
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

# Models
from bk_service.banks.models import (
    Meeting,
    Partner,
    PartnerDetail,
    Bank,
    Share,
    Credit,
    PaymentSchedule,
    EarningShare,
)

# Decimal
from decimal import Decimal


def inserts_earnings_shares(shares, meeting):
    earning_share_list = []
    for share in shares:
        total_earning_by_share = round(meeting.earning_by_share * share.quantity, 4)
        earning_share_list.append(
            EarningShare(
                share=share,
                meeting=meeting,
                earning_by_share=meeting.earning_by_share,
                total_earning_by_share=total_earning_by_share,
                is_paid=False
            )
        )

    EarningShare.objects.bulk_create(earning_share_list)


def update_partner_detail_earnings(partners_detail, meeting):

    meeting_earning_shares = EarningShare.objects.filter(meeting=meeting)

    for partner_detail in partners_detail:

        partner_earning_shares = meeting_earning_shares.filter(
            share__partner=partner_detail.partner
        )

        total_partner_meeting_earning_shares = partner_earning_shares.aggregate(
            Sum('total_earning_by_share'))["total_earning_by_share__sum"] or 0.0

        partner_detail.earnings += Decimal(total_partner_meeting_earning_shares)
        partner_detail.save()


@receiver(post_save, sender=Meeting)
def post_save_create_meeting(sender, instance, created, **kwargs):

    if created:
        bank = Bank.objects.get(pk=instance.bank.id)
        partners_detail = PartnerDetail.objects.filter(partner__bank=bank)

        credits = Credit.objects.filter(meeting=None, bank=bank)
        paymentsSchedule = PaymentSchedule.objects.filter(meeting=None, bank=bank)

        # Update shares and generate earning by shares
        bank_shares = Share.objects.filter(bank=bank)
        inserts_earnings_shares(shares=bank_shares, meeting=instance)

        update_partner_detail_earnings(
            partners_detail=partners_detail,
            meeting=instance
        )

        # Set meeting id in shares
        bank_shares.filter(meeting=None).update(meeting=instance)

        # set meetings in shares, credits and payments schedule
        credits.update(meeting=instance)
        paymentsSchedule.update(meeting=instance)

        # update expenditure_fund and reserve_fund_of_bad_debt
        bank.expenditure_fund += Decimal(instance.expenditure_fund)
        bank.reserve_fund_of_bad_debt += Decimal(instance.reserve_fund_of_bad_debt)
        bank.save()
