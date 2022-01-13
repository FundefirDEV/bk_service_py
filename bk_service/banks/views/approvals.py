""" Appovals views. """

# Django
from django.db.models import Sum


# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from bk_service.banks.serializers import AppovalsSerializer
from bk_service.requests.serializers import (
    ShareRequestModelSerializer,
    CreditRequestModelSerializer,
    PaymentScheduleRequestModelSerializer
)

# Utils enums
from bk_service.utils.enums.banks import PartnerType
from bk_service.utils.enums.requests import ApprovalStatus

# Request Models
from bk_service.requests.models import ShareRequest, CreditRequest, PaymentScheduleRequest


# Errors
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import *


class ApprovalsAPIView(APIView):

    def post(self, request, *args, **kwargs):

        partner = request.user.get_partner()

        if partner.role != PartnerType.admin:
            raise CustomException(error=PARTNER_IS_NOT_ADMIN)

        data = request.data
        serializer = AppovalsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = dict(serializer.validated_data)

        serializer.create(partner=partner, **validated_data)

        return Response(f'share {validated_data["approval_status"]} success !')

    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        if partner.role != PartnerType.admin:
            raise CustomException(error=PARTNER_IS_NOT_ADMIN)

        bank = partner.bank

        share_request = ShareRequest.objects.filter(
            bank=bank,
            approval_status=ApprovalStatus.pending
        )
        credit_request = CreditRequest.objects.filter(
            bank=bank,
            approval_status=ApprovalStatus.pending
        )
        payment_schedule_request = PaymentScheduleRequest.objects.filter(
            bank=bank,
            approval_status=ApprovalStatus.pending
        )

        total_payment_request = payment_schedule_request.aggregate(Sum('amount'))["amount__sum"]

        if total_payment_request == None:
            total_payment_request = 0.0

        share_request_serializer = ShareRequestModelSerializer(
            share_request,
            many=True
        )

        credit_request_serializer = CreditRequestModelSerializer(
            credit_request,
            many=True
        )

        payment_schedule_request_serializer = PaymentScheduleRequestModelSerializer(
            payment_schedule_request,
            many=True
        )

        partner_share_request = ShareRequest.objects.filter(
            partner=partner,
            approval_status=ApprovalStatus.pending
        )
        partner_credit_request = CreditRequest.objects.filter(
            partner=partner,
            approval_status=ApprovalStatus.pending
        )
        partner_payment_schedule_request = PaymentScheduleRequest.objects.filter(
            partner=partner,
            approval_status=ApprovalStatus.pending
        )

        partner_share_request_serializer = ShareRequestModelSerializer(
            partner_share_request,
            many=True
        )
        partner_credit_request_serializer = CreditRequestModelSerializer(
            partner_credit_request,
            many=True
        )
        partner_payment_schedule_request_serializer = PaymentScheduleRequestModelSerializer(
            partner_payment_schedule_request,
            many=True
        )

        return Response({
            "cash_balance": bank.cash_balance,
            "total_shares_quantity": bank.shares,
            "total_credit_amount": bank.active_credits,
            "total_payment_request": total_payment_request,
            "credit_request": credit_request_serializer.data,
            "shares_request": share_request_serializer.data,
            "payment_schedule_request": payment_schedule_request_serializer.data,
            "partner_requests": {
                "shares_request": partner_share_request_serializer.data,
                "credit_request": partner_credit_request_serializer.data,
                "payment_schedule_request": partner_payment_schedule_request_serializer.data
            }
        })
