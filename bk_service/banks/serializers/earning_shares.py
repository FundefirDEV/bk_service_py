""" Earning shares serializers """

# Django
from django.db.models import Sum
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import serializers

# Models
from bk_service.banks.models import EarningShare, Partner
from bk_service.banks.models.shares import Share
from bk_service.banks.models.banks import Bank

# Bk core
from bk_service.bk_core_sdk import BkCoreSDK


class EarningShareModelSerializer(serializers.ModelSerializer):
    """ earning share model serializers """

    class Meta:
        model = EarningShare
        fields = (
            'id',
            'share',
            'meeting',
            'earning_by_share',
            'total_earning_by_share',
            'is_paid',
            'created_at',
        )


class ProfitPaymentSerializer(serializers.Serializer):

    earning_shares_ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False,
    )

    partner_id = serializers.IntegerField(required=True)

    quantity = serializers.IntegerField(required=False)

    def pay_earnings_shares(self, bank, partner_id, earning_shares_ids):
        partner = get_object_or_404(Partner, pk=partner_id, bank=bank)
        earning_shares = EarningShare.objects.filter(
            share__partner=partner,
            is_paid=False,
            pk__in=earning_shares_ids
        )

        profit_amount = earning_shares.aggregate(
            Sum('total_earning_by_share'))["total_earning_by_share__sum"] or 0.0

        partner_detail = partner.partner_detail()

        earning_shares.update(is_paid=True)

        self.update_partner_detail_and_bank(partner_detail, bank, profit_amount)

    def convert_shares(self, bank, partner_id, earning_shares_ids, quantity):
        partner = get_object_or_404(Partner, pk=partner_id, bank=bank)
        bk_core_sdk = BkCoreSDK(partner=partner)

        share_request = bk_core_sdk.create_shares_request(quantity)
        bk_core_sdk.approve_shares_request(share_request.id)

        bank = Bank.objects.get(pk=bank.id)

        # share = Share.objects.get(share_request=share_request)

        self.pay_earnings_shares(bank, partner_id, earning_shares_ids)

    def update_partner_detail_and_bank(self, partner_detail, bank, profit_amount):
        new_earnings = float(partner_detail.earnings) - float(profit_amount)
        new_profit_obtained = float(partner_detail.profit_obtained) + float(profit_amount)
        new_cash_balance = float(bank.cash_balance) - float(profit_amount)

        # Update partner detail and bank
        partner_detail.earnings = new_earnings
        partner_detail.profit_obtained = new_profit_obtained
        bank.cash_balance = new_cash_balance

        partner_detail.save()
        bank.save()
