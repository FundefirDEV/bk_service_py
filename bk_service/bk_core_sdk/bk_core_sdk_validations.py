# Django
from django.db.models import Sum
from django.db.models.functions import Coalesce
# Errors
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import *

# Models
from bk_service.banks.models import (
    Meeting,
    BankRules,
    Share,
    Credit,
    ScheduleInstallment,
)

from bk_service.requests.models import *
# BkCore
from .bk_core import BkCore
# Utils
from bk_service.utils.enums import ApprovalStatus, PaymentStatus


class BkCoreSDKValidations():

    def __init__(self, partner):
        self.partner = partner
        self.bank = partner.bank

    # quantity = requested shares
    def maximun_number_of_shares(self, requested_shares_quantity, bank_rules):

        if requested_shares_quantity <= 0:
            raise CustomException(error=QUANTITY_INVALID)

        count_metting = len(Meeting.objects.filter(bank=self.bank))

        if count_metting > 0:

            maximum_shares_percentage = bank_rules.maximum_shares_percentage_per_partner
            total_shares = self.bank.shares
            partner_share_quantity = self.partner.partner_detail().shares

            total_shares_quantity = requested_shares_quantity

            bk_core = BkCore()

            maximun_number_of_shares = bk_core.maximun_number_of_shares(
                total_shares,
                maximum_shares_percentage,
            )

            if total_shares_quantity > maximun_number_of_shares:
                raise CustomException(error=MAXIMUN_NUMBER_OF_SHARES)

    def validate_share_requests(self, share_requests_id):

        try:
            share_request = ShareRequest.objects.get(
                pk=share_requests_id,
                approval_status=ApprovalStatus.pending
            )
            return share_request
        except:
            raise CustomException(error=ID_REQUESTS_INVALID)

    def validate_credit_requests(self, credit_requests_id):

        try:
            credit_request = CreditRequest.objects.get(
                pk=credit_requests_id,
                approval_status=ApprovalStatus.pending
            )
            if(credit_request.amount > self.bank.cash_balance):
                raise CustomException(error=CASH_BALANCE_EXCCEDED)

            return credit_request
        except:
            raise CustomException(error=ID_REQUESTS_INVALID)

    def validate_payment_schedule_requests(self, payment_schedule_request_id):

        try:
            payment_schedule_request = PaymentScheduleRequest.objects.get(
                pk=payment_schedule_request_id,
                approval_status=ApprovalStatus.pending
            )
            return payment_schedule_request
        except:
            raise CustomException(error=ID_REQUESTS_INVALID)

    def credit_request_validations(self, requested_amount, quantity, payment_type):
        bk_core = BkCore()
        partner = self.partner
        bank = self.bank
        bank_rules = bank.get_bank_rules()

        # requested_quantity needs to be positive
        if requested_amount <= 0:
            raise CustomException(error=AMOUNT_INVALID)

        if quantity <= 0 or quantity == None:
            raise CustomException(error=QUANTITY_REQUIRED)

        if payment_type == None:
            raise CustomException(error=PAYMENT_TYPE_REQUIRED)

        if quantity > bank_rules.maximun_credit_installments:
            raise CustomException(error=MAX_CREDIT_INSTALLMENTS_EXCCEDED)

        # just one request per partner
        if CreditRequest.objects.filter(partner=partner, approval_status=ApprovalStatus.pending).exists():
            raise CustomException(error=PENDING_REQUEST)

        # request can't be greater than the cash balance
        if requested_amount > bank.cash_balance:
            raise CustomException(error=CASH_BALANCE_EXCCEDED)

        # request can't be greater than "maximun_credit_value"
        if requested_amount > bank_rules.maximun_credit_value:
            raise CustomException(error=MAX_CREDIT_EXCCEDED)

        total_shares_amount = self.partner_total_shares_amount(partner=partner)

        maximun_credit_amount = bk_core.calculate_partner_maximun_credit_request(
            total_shares_amount=total_shares_amount, credit_investment_relationship=bank_rules.credit_investment_relationship)

        # request depends of the numbers of shares and credit_investment_relationship"
        if requested_amount > maximun_credit_amount:
            raise CustomException(error=MAX_PARTNER_CREDIT_EXCCEDED)

    def partner_total_shares_amount(self, partner):
        total_shares_amount = Share.objects.filter(
            partner=partner, is_active=True).aggregate(sum=Sum('amount'))["sum"] or 0

        return total_shares_amount

    def payment_schedule_request_validations(self, amount, id_schedule_installment):

        if amount == None or float(amount) <= 0:
            raise CustomException(error=AMOUNT_INVALID)

        if id_schedule_installment == None:
            raise CustomException(error=ID_SCHEDULE_INSTALMENT_REQUIRED)

        # Pending request
        if PaymentScheduleRequest.objects.filter(
            partner=self.partner,
            approval_status=ApprovalStatus.pending
        ).exists():
            raise CustomException(error=PENDING_REQUEST)

        # schedule installment exists
        schedule_installment = ScheduleInstallment.objects.filter(
            pk=id_schedule_installment,
            credit__partner=self.partner,
            payment_status=PaymentStatus.pending,
        )

        if schedule_installment.exists() is not True:
            raise CustomException(error=ID_SCHEDULE_INSTALMENT_NOT_EXIST)

    def change_rules_validations(self):
        share_requests = ShareRequest.objects.filter(bank=self.bank, approval_status=ApprovalStatus.pending)
        credit_requests = CreditRequest.objects.filter(bank=self.bank, approval_status=ApprovalStatus.pending)
        payment_requests = PaymentScheduleRequest.objects.filter(bank=self.bank, approval_status=ApprovalStatus.pending)
        if len(share_requests) > 0 or len(credit_requests) > 0 or len(payment_requests) > 0:
            raise CustomException(error=CHANGE_RULES_PENDING_REQUEST)
