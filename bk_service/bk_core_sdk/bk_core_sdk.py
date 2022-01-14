# Bk core SDK validations
from .bk_core_sdk_validations import BkCoreSDKValidations

# Models
from bk_service.banks.models import BankRules, Share
from bk_service.requests.models import *

from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import *

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

        bank_rules = self.bank.get_bank_rules()

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

        return share_request

    def approve_shares_request(self, share_requests_id,):

        # Validate share requests
        share_request = self.bk_core_validation.validate_share_requests(
            share_requests_id=share_requests_id
        )

        share_request.approval_status = ApprovalStatus.approved
        share_request.save()

        share = Share.objects.create(
            bank=self.bank,
            partner=self.partner,
            share_request=share_request,
            quantity=share_request.quantity,
            amount=share_request.amount,
        )

        # Update partner detail
        partner_detail = self.partner.partner_detail()
        partner_detail.shares += share.quantity
        partner_detail.save()

        # Update bank
        self.partner.bank.shares += share.quantity
        self.partner.bank.cash_balance += share.amount
        self.partner.bank.save()

        return share

    def reject_shares_request(self, share_requests_id,):

        # Validate share requests
        share_request = self.bk_core_validation.validate_share_requests(
            share_requests_id=share_requests_id
        )

        share_request.approval_status = ApprovalStatus.rejected
        share_request.save()

        return share_request

    def create_credit_request(self, amount, quantity, credit_use, credit_use_detail, payment_type):

        # TODO FIX WITH METHOD
        bank_rules = BankRules.objects.get(bank=self.bank, is_active=True)

        self.validate_credit_use(credit_use=credit_use, credit_use_detail=credit_use_detail)

        # Validate credit amount
        self.bk_core_validation.credit_request_validations(
            partner=self.partner,
            requested_amount=requested_credit_amount,
            bank_rules=bank_rules,
            quantity=quantity,
            payment_type=payment_type
        )

        credit_request = CreditRequest.objects.create(
            partner=self.partner,
            bank=self.bank,
            installments=quantity,
            amount=amount,
            credit_use=credit_use,
            credit_use_detail=credit_use_detail,
            payment_type=payment_type,
            approval_status=ApprovalStatus.pending
        )

        return credit_request

    def validate_credit_use(credit_use, credit_use_detail):
        if credit_use == None or credit_use_detail == None:
            raise CustomException(error=CREDIT_USE_REQUIRED)
