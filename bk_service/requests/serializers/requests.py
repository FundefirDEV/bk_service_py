""" Requests serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from bk_service.utils.constants_errors import *


class RequestsSerializer(serializers.Serializer):
    type_request = serializers.CharField(
        required=True,
        error_messages={
            'required': build_error_message(TYPE_REQUEST_REQUIRED),
            'invalid': build_error_message(TYPE_REQUEST_INVALID),
        },
    )
    amount = serializers.CharField(
        required=True,
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
    credit_use = serializers.CharField(
        required=False,
        error_messages={
            'invalid': build_error_message(CREDIT_USE_INVALID),
        },
    )
    detail = serializers.CharField(
        required=False,
        error_messages={
            'invalid': build_error_message(CREDIT_USE_INVALID),
        },
    )
    payment_type = serializers.CharField(
        required=False,
        error_messages={
            'invalid': build_error_message(PAYMENT_TYPE_INVALID),
        },
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
