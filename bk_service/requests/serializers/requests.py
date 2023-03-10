""" Requests serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from bk_service.requests.models import ShareRequest, CreditRequest, PaymentScheduleRequest

# Serializers
from bk_service.banks.serializers.partners import PartnerModelSerializer

# Utils
from bk_service.utils.enums.requests import (
    TypeRequest,
    CreditPayType,
    CreditUse,
    CreditUseDetail,
)
from bk_service.utils.constants_errors import *


# Bk core
from bk_service.bk_core_sdk import BkCoreSDK


class RequestsSerializer(serializers.Serializer):
    type_request = serializers.ChoiceField(
        required=True,
        error_messages={
            'required': build_error_message(TYPE_REQUEST_REQUIRED),
            'invalid': build_error_message(TYPE_REQUEST_INVALID),
        },
        choices=TypeRequest.choices
    )
    amount = serializers.FloatField(
        required=False,
        error_messages={
            'required': build_error_message(AMOUNT_REQUIRED),
            'invalid': build_error_message(AMOUNT_INVALID),
        },
    )
    quantity = serializers.IntegerField(
        required=False,
        error_messages={
            'invalid': build_error_message(QUANTITY_INVALID),
        },
    )
    id_credit = serializers.CharField(
        required=False,
        error_messages={
            'invalid': build_error_message(ID_CREDIT_INVALID),
            'does_not_exist': build_error_message(ID_CREDIT_NOT_EXIST),
        },
    )
    credit_use = serializers.ChoiceField(
        required=False,
        error_messages={
            'invalid': build_error_message(CREDIT_USE_INVALID),
        },
        choices=CreditUse.choices

    )
    credit_use_detail = serializers.ChoiceField(
        required=False,
        error_messages={
            'invalid': build_error_message(CREDIT_USE_INVALID),
        },
        choices=CreditUseDetail.choices

    )

    payment_type = serializers.ChoiceField(
        required=False,
        error_messages={
            'invalid': build_error_message(PAYMENT_TYPE_INVALID),
        },
        choices=CreditPayType.choices
    )
    id_schedule_installment = serializers.FloatField(
        required=False,
        error_messages={
            'invalid': build_error_message(ID_SCHEDULE_INSTALMENT_INVALID),
        },
    )
    date = serializers.DateTimeField(
        required=False,
    )

    def validate(self, data):

        # Set None if key not exist
        if 'quantity' not in data:
            data['quantity'] = None

        if 'amount' not in data:
            data['amount'] = None

        if 'id_schedule_installment' not in data:
            data['id_schedule_installment'] = None

        return data

    def create_request(self, partner, validated_data):
        bk_core_sdk = BkCoreSDK(partner=partner)
        type_request = validated_data['type_request']

        if type_request == TypeRequest.share:
            quantity = int(validated_data['quantity'])
            share_request = bk_core_sdk.create_shares_request(requested_shares_quantity=quantity)
            return share_request

        if type_request == TypeRequest.credit:
            validated_data.pop('id_schedule_installment')
            validated_data.pop('type_request')
            self.create_credit_request(partner=partner, validated_data=validated_data)

        if type_request == TypeRequest.installment_payment:

            amount = validated_data['amount']
            id_schedule_installment = validated_data['id_schedule_installment']

            payment_schedule_request = bk_core_sdk.create_payment_schedule_request(
                amount=amount,
                id_schedule_installment=id_schedule_installment
            )

            # self.create_credit_request(partner=partner, validated_data=validated_data)

    def create_credit_request(self, partner, validated_data):
        bk_core_sdk = BkCoreSDK(partner=partner)
        credit_request = bk_core_sdk.create_credit_request(**validated_data)
        return credit_request


class ShareRequestModelSerializer(serializers.ModelSerializer):
    """ share request model serializers """

    partner = PartnerModelSerializer(read_only=True)

    class Meta:
        model = ShareRequest
        fields = ('id', 'quantity', 'amount', 'approval_status', 'partner', 'created_at')


class CreditRequestModelSerializer(serializers.ModelSerializer):
    """ credit requests model serializers """

    partner = PartnerModelSerializer(read_only=True)

    class Meta:
        model = CreditRequest
        fields = (
            'id',
            'installments',
            'amount',
            'approval_status',
            'partner',
            'created_at',
            'credit_use',
            'credit_use_detail',
            'payment_type',
        )


class PaymentScheduleRequestModelSerializer(serializers.ModelSerializer):
    """ payment schedule request serializers """

    partner = PartnerModelSerializer(read_only=True)

    class Meta:
        model = PaymentScheduleRequest
        fields = ('id', 'schedule_installment', 'amount', 'approval_status', 'partner', 'created_at')
