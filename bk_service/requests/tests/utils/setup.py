from bk_service.requests.models import *

# import pdb
# pdb.set_trace()


def create_share_request(partner, quantity=1, amount=10000):
    shareRequest = ShareRequest.objects.create(partner=partner, bank=partner.bank, quantity=1, amount=10000)
    return shareRequest


def create_credit_request(partner, amount=100000, installments=1):
    credit_request = CreditRequest.objects.create(
        partner=partner, bank=partner.bank, amount=amount, installments=installments)
    return credit_request
