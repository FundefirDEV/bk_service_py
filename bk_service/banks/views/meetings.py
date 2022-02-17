""" Meeting views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# bk_core
from bk_service.bk_core_sdk import BkCoreSDK

# Models
from bk_service.banks.models import Bank

# Serializers
from bk_service.banks.serializers import MeetingsModelSerializer


# Utils enums
from bk_service.utils.enums.banks import PartnerType
from bk_service.utils.enums.requests import ApprovalStatus

# Errors
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import PARTNER_IS_NOT_ADMIN

# bk_core
from bk_service.bk_core_sdk.bk_core import BkCore


class MeetingsGetAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        partner_detail = partner.partner_detail()
        bank = partner.bank

        bk_core_sdk = BkCoreSDK(partner=partner)

        res = bk_core_sdk.create_meeting(preview=True)

        return Response(res)


class CloseMeetingsAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        if partner.role != PartnerType.admin:
            raise CustomException(error=PARTNER_IS_NOT_ADMIN)

        bk_core_sdk = BkCoreSDK(partner=partner)

        meeting_data = bk_core_sdk.create_meeting(preview=False)

        total_expenditure_fund = meeting_data.pop('total_expenditure_fund')
        total_reserve_fund_of_bad_debt = meeting_data.pop('total_reserve_fund_of_bad_debt')

        total_earning = meeting_data.pop('total_earning')
        total_ordinary_interest_advance = meeting_data.pop('total_ordinary_interest_advance')
        total_interest = meeting_data.pop('total_interest')
        total_ordinary_interest_installments = meeting_data.pop('total_ordinary_interest_installments')

        serializer = MeetingsModelSerializer(data=meeting_data)
        serializer.is_valid(raise_exception=True)
        validated_data = dict(serializer.validated_data)

        meeting = serializer.create(validated_data)

        bank = Bank.objects.get(pk=partner.bank.id)

        res = serializer.data
        res['total_expenditure_fund'] = total_expenditure_fund
        res['total_reserve_fund_of_bad_debt'] = total_reserve_fund_of_bad_debt

        res['total_earning'] = total_earning
        res['total_ordinary_interest_advance'] = total_ordinary_interest_advance
        res['total_interest'] = total_interest
        res['total_ordinary_interest_installments'] = total_ordinary_interest_installments

        return Response(res)
