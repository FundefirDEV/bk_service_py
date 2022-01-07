# Bk core SDK validations
from .bk_core_sdk_validations import BkCoreSDKValidations

# Models
from bk_service.banks.models import BankRules
from bk_service.requests.models import *

# Utils
from bk_service.utils.enums.requests import ApprovalStatus


class BkCoreSDK():

    def __init__(self, partner):
        self.partner = partner
        self.bank = partner.bank
        self.bk_core_validation = BkCoreSDKValidations(
            partner=self.partner,
        )

    def create_shares_request(self, requested_shares_quantity,):

        bank_rules = BankRules.objects.get(bank=self.bank, is_active=True)

        # Validate shares quantity
        self.bk_core_validation.maximun_number_of_shares(
            requested_shares_quantity=requested_shares_quantity,
            bank_rules=bank_rules,
        )

        amount = requested_shares_quantity * bank_rules.share_value

        share_request = ShareRequest.objects.create(
            partner=self.partner,
            bank=self.bank,
            quantity=requested_shares_quantity,
            amount=amount,
            approval_status=ApprovalStatus.pending
        )

        # Update partner detail
        # partner_detail = self.partner.partner_detail()
        # partner_detail.shares += share_request.quantity
        # partner_detail.save()

        # # Update bank
        # self.partner.bank.shares += share_request.quantity
        # self.partner.bank.cash_balance += share_request.amount

        self.partner.bank.save()

        return share_request
