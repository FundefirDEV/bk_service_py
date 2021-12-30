""" Partner serializers """

# Django

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.banks.models import Partner, PartnerGuest

from bk_service.utils.exceptions_errors import CustomValidation
from bk_service.utils.constants_errors import *


class PartnerModelSerializer(serializers.ModelSerializer):
    """ Partner model serializers """
    class Meta:
        model = Partner
        fields = ('id', 'role', 'phone_number', 'phone_region_code', 'bank',
                  'user',)


class PartnerPhoneExistSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        required=True,

        validators=[
            UniqueValidator(queryset=Partner.objects.all(), message=build_error_message(PHONE_EXIST))
        ],
        error_messages={
            'required': build_error_message(PHONE_REQUIRED),
            'invalid': build_error_message(PHONE_INVALID),
        },
    )


class PartnerGuestPhoneExistSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=PartnerGuest.objects.all(), message=build_error_message(PHONE_EXIST)),
            UniqueValidator(queryset=Partner.objects.all(), message=build_error_message(PHONE_EXIST))
        ],
        error_messages={
            'required': build_error_message(PHONE_REQUIRED),
            'invalid': build_error_message(PHONE_INVALID),
        },
    )


# class MultiplePhoneExistSerializer(serializers.Serializer):
#     phone_numbers = serializers.ListSerializer(child=serializers.CharField(
#         required=True,
#         validators=[
#             UniqueValidator(queryset=PartnerGuest.objects.all(), message=build_error_message(PHONE_EXIST)),
#             UniqueValidator(queryset=Partner.objects.all(), message=build_error_message(PHONE_EXIST))
#         ],
#         error_messages={
#             'required': build_error_message(PHONE_REQUIRED),
#             'invalid': build_error_message(PHONE_INVALID),
#         },
#     ))
