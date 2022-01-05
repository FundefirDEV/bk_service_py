""" Bank rules views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

from bk_service.banks.models.bank_rules import BankRules
# Serializers
# from bk_service.banks.serializers import BankModelSerializer,


class BankRule(APIView):
    def get(self, request, *args, **kwargs):

        bank = request.user.get_partner().bank

        rules = BankRules.objects.get(bank=bank, is_active=True)

        return Response({"bankName": bank.name,
                         "ordinary_interest": rules.ordinary_interest,
                         "delay_interest": rules.delay_interest,
                         "maximun_credit_installments": rules.maximun_credit_installments,
                         "maximun_credit_value": rules.maximun_credit_value,
                         "share_value": rules.share_value,
                         "maximum_shares_percentage_per_partner": rules.maximum_shares_percentage_per_partner,
                         "maximum_active_credits_per_partner": rules.maximum_active_credits_per_partner,
                         "expenditure_fund_percentage": rules.expenditure_fund_percentage,
                         "reserve_fund_of_bad_debt": rules.reserve_fund_of_bad_debt,
                         "payment_period_of_installment": rules.payment_period_of_installment,
                         "credit_investment_relationship": rules.credit_investment_relationship})