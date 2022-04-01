""" Special Credit views. """
from django.shortcuts import get_object_or_404
# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from bk_service.banks.serializers.special_credit import SpecialCreditSerializer

from bk_service.utils.enums.banks import PartnerType

from bk_service.banks.models import Credit, Partner, ScheduleInstallment
from bk_service.requests.models import CreditRequest

# Errors
from bk_service.utils.constants_errors import build_error_message
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import PARTNER_IS_NOT_ADMIN, CASH_BALANCE_EXCCEDED
from bk_service.utils.enums.requests import ApprovalStatus

# BkCore
from bk_service.bk_core_sdk.bk_core import BkCore
class SpecialCreditAPIView(APIView):

    def post(self, request, *args, **kwargs):

        admin = request.user.get_partner()
        if admin.role != PartnerType.admin:
            raise CustomException(error=PARTNER_IS_NOT_ADMIN)

        data = request.data
        serializer = SpecialCreditSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        validated_data = dict(serializer.validated_data)
        partner = get_object_or_404(Partner, pk=validated_data['partner_id'], bank=admin.bank)

        bank = admin.bank
        if validated_data['amount'] > bank.cash_balance:
            raise CustomException(error=CASH_BALANCE_EXCCEDED)

        credit_request = CreditRequest.objects.create(
            partner=partner,
            bank=partner.bank,
            installments=validated_data['installments'],
            credit_use=validated_data['credit_use'],
            credit_use_detail=validated_data['credit_use_detail'],
            payment_type=validated_data['payment_type'],
            approval_status=ApprovalStatus.approved)

        credit = Credit.objects.create(
            partner=partner,
            credit_request=credit_request,
            bank=partner.bank,
            installments=validated_data['installments'],
            amount=validated_data['amount'],
            credit_use=validated_data['credit_use'],
            credit_use_detail=validated_data['credit_use_detail'],
            payment_type=validated_data['payment_type'],
            is_active=True,
            is_special=True,
        )

        schedule_installments_core = BkCore().calculate_schedule_installment(
            ordinary_interest=validated_data['ordinary_interest'],
            delay_interest=validated_data['delay_interest'],
            credit_amount=credit.amount,
            installments=credit.installments,
            payment_period_of_installment=validated_data['payment_period_of_installments'],
            payment_type=credit.payment_type
        )

        for index, schedule_installment in enumerate(schedule_installments_core):
            schedule = ScheduleInstallment.objects.create(
                credit=credit,
                capital_installment=schedule_installment['capital_value'],
                ordinary_interest_percentage=validated_data['ordinary_interest'],
                delay_interest_percentage=validated_data['delay_interest'],
                delay_interest_base_amount=schedule_installment['delay_interest_base_amount'],
                ordinary_interest_calculated=schedule_installment['ordinary_insterest'],
                total_pay_installment=schedule_installment['capital_value'] +
                schedule_installment['ordinary_insterest'],
                payment_date=schedule_installment['installment_payment_date'],
                payment_status=ApprovalStatus.pending,
                installment_number=index
            )
        return Response({"message": "Special Credit Created"})
