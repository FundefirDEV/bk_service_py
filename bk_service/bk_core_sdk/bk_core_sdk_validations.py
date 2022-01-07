from bk_service.utils.exceptions_errors import CustomValidation
from bk_service.utils.constants_errors import *

# Models
from bk_service.banks.models import Meeting, BankRules
from bk_service.requests.models import ShareRequest

# BkCore
from .bk_core import BkCore

# Utils
from bk_service.utils.enums.requests import ApprovalStatus


class BkCoreSDKValidations():

    def __init__(self, partner):
        self.partner = partner
        self.bank = partner.bank

    # quantity = requested shares
    def maximun_number_of_shares(self, requested_shares_quantity, bank_rules):

        if requested_shares_quantity <= 0:
            raise CustomValidation(error=QUANTITY_INVALID)

        count_metting = len(Meeting.objects.filter(bank=self.bank))

        if count_metting > 0:

            maximum_shares_percentage = bank_rules.maximum_shares_percentage_per_partner
            total_shares = self.bank.shares
            partner_share_quantity = self.partner.partner_detail().shares

            total_shares_quantity = partner_share_quantity + requested_shares_quantity

            bk_core = BkCore()

            maximun_number_of_shares = bk_core.maximun_number_of_shares(
                total_shares,
                maximum_shares_percentage,
            )

            if total_shares_quantity > maximun_number_of_shares:
                raise CustomValidation(error=MAXIMUN_NUMBER_OF_SHARES)

    def validate_share_requests(self, share_requests_id):

        try:
            share_request = ShareRequest.objects.get(
                pk=share_requests_id,
                approval_status=ApprovalStatus.pending
            )
            return share_request
        except:
            raise CustomValidation(error=ID_REQUESTS_INVALID)
