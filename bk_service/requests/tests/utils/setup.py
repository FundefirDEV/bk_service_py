
# Models
from bk_service.requests.models import *

# Utils
from bk_service.utils.enums.requests import (
    ApprovalStatus,
    CreditPayType,
    CreditUse,
    CreditUseDetail
)

# # import pdb
# pdb.set_trace()


def create_share_request(partner, quantity=1, amount=10000, approval_status=ApprovalStatus.pending):
    shareRequest = ShareRequest.objects.create(
        partner=partner,
        bank=partner.bank,
        quantity=quantity,
        amount=amount,
        approval_status=approval_status,
    )
    return shareRequest


def create_credit_request(
        partner,
        amount=100000,
        installments=1,
        payment_type=CreditPayType.installments,
        approval_status=ApprovalStatus.pending,
        credit_use=CreditUse.consumption,
        credit_use_detail=CreditUseDetail.Education,
):
    credit_request = CreditRequest.objects.create(
        partner=partner,
        bank=partner.bank,
        amount=amount,
        installments=installments,
        approval_status=approval_status,
        credit_use=credit_use,
        credit_use_detail=credit_use_detail,
        payment_type=payment_type
    )
    return credit_request


def create_payment_schedule_request(credit, schedule_installment):
    payment_schedule_request = PaymentScheduleRequest.objects.create(
        schedule_installment=schedule_installment,
        partner=credit.partner,
        bank=credit.bank,
        amount=10000,
        approval_status=ApprovalStatus.pending,
    )
    return payment_schedule_request
