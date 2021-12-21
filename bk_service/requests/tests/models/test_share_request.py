""" Shares Request Test. """

#  Django
from django.test import TestCase
from bk_service.requests.models.share_requests import ShareRequest

# Utils
from bk_service.banks.tests.utils.setup import create_partner


class SharesRequestTestCase(TestCase):
    """ Shares Request test class """

    def test_share_request_success(self):
        """ Shares Request success """
        partner = create_partner()
        ShareRequest.objects.create(partner=partner, bank=partner.bank, quantity=1, amount=10000)
        shareRequest = ShareRequest.objects.get(partner=partner)
        self.assertEqual(shareRequest.amount, 10000)
        self.assertEqual(shareRequest.quantity, 1)
