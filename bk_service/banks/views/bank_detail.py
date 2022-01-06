""" Bank rules views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# bk_core
from bk_service.bk_core_sdk.bk_core_sdk_validations import BkCoreSDKValidations

# Serializers
from bk_service.banks.models.bank_rules import BankRules
from bk_service.banks.models.partners import Partner
from bk_service.banks.models.partner_details import PartnerDetail


# bk_core
from bk_service.bk_core_sdk.bk_core import BkCore


class BankDetail(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        partner_detail = partner.partner_detail()
        bank = partner.bank
        rules = BankRules.objects.get(bank=bank, is_active=True)

        core = BkCore()
        maximun_number_of_shares = BkCore().maximun_number_of_shares(total_shares=bank.shares,
                                                                     maximum_shares_percentage=rules.maximum_shares_percentage_per_partner)

        return Response({"rules": {"share_value": rules.share_value,
                                   "maximum_shares_percentage_per_partner": maximun_number_of_shares},
                         "group": {"cash_balance": bank.cash_balance,
                                   "active_credits": bank.active_credits,
                                   "shares": bank.shares},
                         "partner": {"earnings": partner_detail.earnings,
                                     "active_credits": partner_detail.active_credit,
                                     "shares": partner_detail.shares},
                         })
