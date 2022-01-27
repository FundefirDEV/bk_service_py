# Django
from django.db.models import Sum

# Bk core SDK validations
from .bk_core_sdk_validations import BkCoreSDKValidations

# BkCore
from bk_service.bk_core_sdk.bk_core import BkCore

# Models
from bk_service.banks.models import *
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
        self.bk_core = BkCore()

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

    def reject_shares_request(self, share_requests_id,):

        # Validate share requests
        share_request = self.bk_core_validation.validate_share_requests(
            share_requests_id=share_requests_id
        )

        share_request.approval_status = ApprovalStatus.rejected
        share_request.save()

        return share_request

    def create_credit_request(self, amount, quantity, credit_use, credit_use_detail, payment_type):
        bank_rules = self.bank.get_bank_rules()

        if credit_use == None or credit_use_detail == None:
            raise CustomException(error=CREDIT_USE_REQUIRED)

        # Validate credit params
        self.bk_core_validation.credit_request_validations(
            requested_amount=int(amount),
            quantity=int(quantity),
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

    def approve_credit_request(self, credit_requests_id):

        # Validate credit requests
        credit_request = self.bk_core_validation.validate_credit_requests(
            credit_requests_id=credit_requests_id
        )

        credit_request.approval_status = ApprovalStatus.approved
        credit_request.save()

    def reject_credit_request(self, credit_requests_id):

        # Validate credit requests
        credit_request = self.bk_core_validation.validate_credit_requests(
            credit_requests_id=credit_requests_id
        )

        credit_request.approval_status = ApprovalStatus.rejected
        credit_request.save()

        return credit_request

    def create_payment_schedule_request(self, amount, id_schedule_installment):

        self.bk_core_validation.payment_schedule_request_validations(
            amount=amount,
            id_schedule_installment=id_schedule_installment,
        )

        payment_schedule_request = PaymentScheduleRequest.objects.create(
            partner=self.partner,
            bank=self.bank,
            schedule_installment_id=id_schedule_installment,
            amount=amount,
            approval_status=ApprovalStatus.pending
        )

        return payment_schedule_request

    def validate_credit_use(self, credit_use, credit_use_detail):
        if credit_use == None or credit_use_detail == None:
            raise CustomException(error=CREDIT_USE_REQUIRED)

    def create_meeting(self, preview=True):

        cash_balance = self.bank.cash_balance
        bank_rules = self.bank.get_bank_rules()

        credits = Credit.objects.filter(bank=self.bank, meeting=None)
        shares = Share.objects.filter(bank=self.bank, meeting=None)
        payments_schedule = PaymentSchedule.objects.filter(bank=self.bank, meeting=None)

        # Shares
        total_shares_quantity = shares.aggregate(Sum('quantity'))["quantity__sum"] or 0
        total_shares_amount = shares.aggregate(Sum('amount'))["amount__sum"] or 0.0

        # credits
        total_credits_quantity = len(credits)
        total_credits_amount = credits.aggregate(Sum('amount'))["amount__sum"] or 0.0

        # Calculate interests
        total_ordinary_interest = 0.0

        # TODO: pending delay interest
        total_delay_interest = 0.0

        credits_advance = credits.filter(payment_type=CreditPayType.advance)
        total_ordinary_interest_advance = credits_advance.aggregate(
            Sum('total_interest'))["total_interest__sum"] or 0.0

        total_ordinary_interest_installments = payments_schedule.aggregate(
            Sum('interest_paid'))["interest_paid__sum"] or 0.0

        total_ordinary_interest = float(total_ordinary_interest_advance) + float(total_ordinary_interest_installments)

        total_interest = total_ordinary_interest + total_delay_interest

        # Calculate capital
        total_capital = payments_schedule.aggregate(
            Sum('capital_paid'))["capital_paid__sum"] or 0.0

        # Expenditure fund
        expenditure_fund_percentage = float(bank_rules.expenditure_fund_percentage)
        expenditure_fund = self.bk_core.calculate_expenditure_fund(
            total_interest=total_interest,
            expenditure_fund_percentage=expenditure_fund_percentage
        )
        total_expenditure_fund = expenditure_fund + float(self.bank.expenditure_fund)

        # reserve_fund_of_bad_debt
        expenditure_fund_percentage = float(bank_rules.reserve_fund_of_bad_debt_percentage)

        reserve_fund_of_bad_debt = self.bk_core.calculate_reserve_fund_of_bad_debt(
            total_interest=total_interest,
            reserve_fund_of_bad_debt_percentage=expenditure_fund_percentage
        )
        total_reserve_fund_of_bad_debt = reserve_fund_of_bad_debt + float(self.bank.reserve_fund_of_bad_debt)

        # Earning
        total_earning = self.bk_core.calculate_total_earning(
            total_interest=total_interest,
            expenditure_fund=expenditure_fund,
            reserve_fund_of_bad_debt=reserve_fund_of_bad_debt
        )

        # Earning by share
        earning_by_share = self.bk_core.calculate_earning_by_share(
            total_earning=total_earning,
            bank_shares_quantity=self.bank.shares
        )

        meeting_data = {
            "cash_balance": cash_balance,
            "expenditure_fund": expenditure_fund,
            "reserve_fund_of_bad_debt": reserve_fund_of_bad_debt,
            "total_expenditure_fund": total_expenditure_fund,
            "total_reserve_fund_of_bad_debt": total_reserve_fund_of_bad_debt,
            "earning_by_share": earning_by_share,
            "total_shares_quantity": total_shares_quantity,
            "total_shares_amount": total_shares_amount,
            "total_delay_interest": total_delay_interest,
            "total_ordinary_interest": total_ordinary_interest,
            "total_credits_amount": total_credits_amount,
            "total_credits_quantity": total_credits_quantity,
            "total_capital": total_capital
        }

        if preview:
            meeting_data['resource'] = 'PREVIEW'
        else:
            meeting_data['bank'] = self.bank.id

        return meeting_data
