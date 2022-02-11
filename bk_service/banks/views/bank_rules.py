""" Bank rules views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
# BkCore
from bk_service.bk_core_sdk.bk_core_sdk_validations import BkCoreSDKValidations
# Models
from bk_service.banks.models.bank_rules import BankRules
# Serializer
from bk_service.banks.serializers.bank_rules import BankRulesSerializer
# Enums
from bk_service.utils.enums.banks import PartnerType
# Errors
from bk_service.utils.constants_errors import build_error_message
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import PARTNER_IS_NOT_ADMIN


class BankRuleApiView(APIView):
    def get(self, request, *args, **kwargs):

        bank = request.user.get_partner().bank

        rules = bank.get_bank_rules()

        return Response({"bankName": bank.name,
                         "ordinary_interest": rules.ordinary_interest,
                         "delay_interest": rules.delay_interest,
                         "maximun_credit_installments": rules.maximun_credit_installments,
                         "maximun_credit_value": rules.maximun_credit_value,
                         "share_value": rules.share_value,
                         "maximum_shares_percentage_per_partner": rules.maximum_shares_percentage_per_partner,
                         "maximum_active_credits_per_partner": rules.maximum_active_credits_per_partner,
                         "expenditure_fund_percentage": rules.expenditure_fund_percentage,
                         "reserve_fund_of_bad_debt_percentage": rules.reserve_fund_of_bad_debt_percentage,
                         "payment_period_of_installment": rules.payment_period_of_installment,
                         "credit_investment_relationship": rules.credit_investment_relationship})

    def post(self, request, *args, **kwargs):
        partner = request.user.get_partner()
        bank = partner.bank
        if partner.role != PartnerType.admin:
            raise CustomException(error=PARTNER_IS_NOT_ADMIN)

        BkCoreSDKValidations(partner=partner).change_rules_validations()

        data = request.data
        data['bank'] = bank.id
        data['is_active'] = True
        serializer = BankRulesSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = dict(serializer.validated_data)
        previous_rules = bank.get_bank_rules()
        previous_rules.is_active = False
        previous_rules.save()
        serializer.create(validated_data=validated_data,)
        return Response('Bank Rules updated')
