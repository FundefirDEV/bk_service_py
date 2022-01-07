""" Requests serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from bk_service.utils.constants_errors import *

# Utils
from bk_service.utils.enums.requests import (
    TypeRequest,
    CreditPayType,
    CreditUse,
    CreditUseDetail,
)


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
    amount = serializers.CharField(
        required=False,
        error_messages={
            'required': build_error_message(AMOUNT_REQUIRED),
            'invalid': build_error_message(AMOUNT_REQUIRED),
        },
    )
    quantity = serializers.CharField(
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
    detail = serializers.ChoiceField(
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
    id_schedule_installment = serializers.CharField(
        required=False,
        error_messages={
            'invalid': build_error_message(ID_SCHEDULE_INSTALMENT_INVALID),
        },
    )
    date = serializers.DateTimeField(
        required=False,
    )

    def create(self, partner, quantity):

        bk_core_sdk = BkCoreSDK(partner=partner)
        share_request = bk_core_sdk.create_shares_request(requested_shares_quantity=quantity)
        return share_request
