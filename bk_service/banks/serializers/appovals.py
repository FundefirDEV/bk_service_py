""" Appovals serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from bk_service.utils.constants_errors import *

# Utils
from bk_service.utils.enums.requests import (
    TypeRequest,
    ApprovalStatus
)

# Bk core
from bk_service.bk_core_sdk import BkCoreSDK


class AppovalsSerializer(serializers.Serializer):

    type_request = serializers.ChoiceField(
        required=True,
        error_messages={
            'required': build_error_message(TYPE_REQUEST_REQUIRED),
            'invalid': build_error_message(TYPE_REQUEST_INVALID),
        },
        choices=TypeRequest.choices
    )
    request_id = serializers.CharField(
        required=True,
        error_messages={
            'required': build_error_message(ID_REQUESTS_REQUIRED),
            'invalid': build_error_message(ID_REQUESTS_INVALID),
            'does_not_exist': build_error_message(ID_REQUESTS_NOT_EXIST),
        },
    )
    approval_status = serializers.ChoiceField(
        required=True,
        error_messages={
            'required': build_error_message(APPROVALS_STATUS_REQUIRED),
            'invalid': build_error_message(APPROVALS_STATUS_INVALID),
        },
        choices=ApprovalStatus.choices
    )

    def create(self, partner, type_request, request_id, approval_status):

        bk_core_sdk = BkCoreSDK(partner=partner)

        if approval_status == ApprovalStatus.approved:

            if type_request == TypeRequest.share:
                bk_core_sdk.approve_shares_request(share_requests_id=request_id)

            if type_request == TypeRequest.credit:
                bk_core_sdk.approve_credit_request(credit_requests_id=request_id, bank=partner.bank)
                pass

            if type_request == TypeRequest.installment_payment:
                # share_request = bk_core_sdk.approve_shares_request(share_requests_id=request_id)
                pass

        if approval_status == ApprovalStatus.rejected:

            if type_request == TypeRequest.share:
                share_request = bk_core_sdk.reject_shares_request(share_requests_id=request_id)
                pass
            if type_request == TypeRequest.credit:
                bk_core_sdk.approve_credit_request(credit_requests_id=request_id)
                pass
            if type_request == TypeRequest.installment_payment:
                # share_request = bk_core_sdk.approve_shares_request(share_requests_id=request_id)
                pass
