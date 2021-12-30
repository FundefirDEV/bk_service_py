""" Bank serializers """

# Django

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.banks.models.partners_guest import PartnerGuest
from bk_service.banks.models.partners import Partner

# Utils Errors
from bk_service.utils.constants_errors import build_error_message
from bk_service.utils.constants_errors import *
from bk_service.utils.exceptions_errors import CustomValidation


import pdb


class PartnersGuestSerializer(serializers.ModelSerializer):
    """ Partner Guest serializers """

    phone_number = serializers.CharField(

        required=True,

        validators=[
            UniqueValidator(queryset=PartnerGuest.objects.all(),
                            message=build_error_message(PARTNER_GUEST_PHONE_EXIST)),
            UniqueValidator(queryset=Partner.objects.all(), message=build_error_message(PHONE_EXIST))
        ],
        error_messages={
            'required': build_error_message(PARTNER_GUEST_PHONE_REQUIRED),
            'invalid': build_error_message(PARTNER_GUEST_PHONE_INVALID),
        },
    )

    class Meta:
        model = PartnerGuest
        fields = ('name', 'phone_number', 'phone_region_code', 'bank')

        extra_kwargs = {
            'bank': {
                'error_messages': {
                    'does_not_exist': build_error_message(BANK_INVALID),
                    'required': build_error_message(BANK_REQUIRED),
                }
            },
            'name': {
                "error_messages": {
                    'required': build_error_message(PARTNER_GUEST_NAME_REQUIRED),
                    'invalid': build_error_message(PARTNER_GUEST_NAME_INVALID),
                },
            },
            'phone_region_code': {
                "error_messages": {
                    'required': build_error_message(PARTNER_GUEST_PHONE_REGION_CODE_REQUIRED),
                    'invalid': build_error_message(PARTNER_GUEST_PHONE_REGION_CODE_INVALID),
                }
            },
        }
