""" Bank Rules serializers """

# Django

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.banks.models.banks import Bank
from bk_service.banks.models.bank_rules import BankRules

# Utils Errors
from bk_service.utils.constants_errors import build_error_message
from bk_service.utils.constants_errors import *
from bk_service.utils.exceptions_errors import CustomException


class BankRulesSerializer(serializers.ModelSerializer):
    """ Bank rules serializers """

    class Meta:
        model = BankRules
        fields = ('__all__')

        extra_kwargs = {
            'bank': {
                'error_messages': {
                    'does_not_exist': build_error_message(BANK_INVALID),
                    'required': build_error_message(BANK_REQUIRED),
                }
            }
        }
