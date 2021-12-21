""" Shares Request Test. """

#  Django
from django.test import TestCase
from bk_service.requests.models.share_requests import ShareRequest
# Utils
from bk_service.banks.tests.utils.setup import createPartner


class SharesRequestTestCase(TestCase):
    """ Shares Request test class """

    def setUp(self):
        partner = createPartner()
        # import pdb
        # pdb.set_trace()
        ShareRequest.objects.create(partner=partner, bank=partner.bank, quantity=1, amount=10000)

    def test_State_success(self):
        """ Shares Request success """
        shareRequest = ShareRequest.objects.get(pk=1)
        self.assertEqual(shareRequest.amount, 10000)
        self.assertEqual(shareRequest.quantity, 1)
