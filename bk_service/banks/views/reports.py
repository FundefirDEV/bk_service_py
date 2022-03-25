# Django
from django.db.models import Sum

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models import *

# Serializers
from bk_service.banks.serializers import *

# Bk Core
from bk_service.bk_core_sdk import BkCore


class ReportsAPIView(APIView):
    def get(self, request, *args, **kwargs):

        bk_core = BkCore()

        partner = request.user.get_partner()
        bank = partner.bank

        cash_balance = bank.cash_balance
        bank_rules = bank.get_bank_rules()

        # Query sets
        credits = Credit.objects.filter(bank=bank, is_active=True,).exclude(meeting=None)
        shares = Share.objects.filter(bank=bank, is_active=True,).exclude(meeting=None)
        payments_schedule = PaymentSchedule.objects.filter(bank=bank,).exclude(meeting=None)
        meetings = Meeting.objects.filter(bank=bank,)
        partner_details = PartnerDetail.objects.filter(partner__bank=bank, partner__is_active=True)

        # Serializers
        share_serializer = SharesModelSerializer(shares, many=True)
        credit_serializer = CreditsModelSerializer(credits, many=True)
        meeting_serializer = MeetingsModelSerializer(meetings, many=True)
        partner_detail_serializer = PartnerDetailModelSerializer(partner_details, many=True)

        # Shares
        total_shares_quantity = shares.aggregate(Sum('quantity'))["quantity__sum"] or 0
        total_shares_amount = shares.aggregate(Sum('amount'))["amount__sum"] or 0.0

        # credits
        total_credits_quantity = len(credits)
        total_credits_amount = credits.aggregate(Sum('amount'))["amount__sum"] or 0.0

        # Calculate interests
        total_ordinary_interest = credits.aggregate(
            Sum('total_interest'))["total_interest__sum"] or 0.0

        total_interest = total_ordinary_interest

        # Calculate capital
        total_payments_schedule_amount = payments_schedule.aggregate(
            Sum('amount'))["amount__sum"] or 0.0

        # Expenditure fund
        expenditure_fund = bank.expenditure_fund

        # reserve_fund_of_bad_debt
        reserve_fund_of_bad_debt = bank.reserve_fund_of_bad_debt

        # Earning
        total_earning = bk_core.calculate_total_earning(
            total_interest=float(total_interest),
            expenditure_fund=float(expenditure_fund),
            reserve_fund_of_bad_debt=float(reserve_fund_of_bad_debt)
        )

        res = {
            "expenditure_fund": expenditure_fund,
            "reserve_fund_of_bad_debt": reserve_fund_of_bad_debt,
            "total_shares_quantity": total_shares_quantity,
            "total_shares_amount": total_shares_amount,
            "total_earning": total_earning,
            "meetings": meeting_serializer.data,
            "partners": partner_detail_serializer.data,
            "shares": {
                "shares_per_partner": share_serializer.data,
            },
            'credits': {
                "total_payments_schedule_amount": total_payments_schedule_amount,
                "total_credits_amount": total_credits_amount,
                "total_current_debt": total_interest - total_payments_schedule_amount,
                "credits_per_partner": credit_serializer.data,
            },
            'earnings': {
                "total_credits_per_meeting": meeting_serializer.data,
            },

        }

        return Response(res)
