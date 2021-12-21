from bk_service.requests.models.share_requests import ShareRequest

# import pdb
# pdb.set_trace()


def create_share_request(partner, quantity=1, amount=10000):
    shareRequest = ShareRequest.objects.create(partner=partner, bank=partner.bank, quantity=1, amount=10000)
    return shareRequest
