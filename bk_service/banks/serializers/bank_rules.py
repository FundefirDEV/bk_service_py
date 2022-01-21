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
        fields = ('ordinary_interest', 'maximun_credit_installments',
                  'maximun_credit_value', 'share_value', 'maximum_shares_percentage_per_partner',
                  'maximum_active_credits_per_partner', 'expenditure_fund_percentage', 'reserve_fund_of_bad_debt_percentage',
                  'payment_period_of_installment', 'credit_investment_relationship', 'bank')

        extra_kwargs = {
            'bank': {
                'error_messages': {
                    'does_not_exist': build_error_message(BANK_INVALID),
                    'required': build_error_message(BANK_REQUIRED),
                }
            }
        }
