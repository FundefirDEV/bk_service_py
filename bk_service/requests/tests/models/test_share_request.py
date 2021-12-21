""" Shares Request Test. """

#  Django
from django.test import TestCase
from bk_service.requests.models.share_requests import ShareRequest

# Utils
from bk_service.banks.tests.utils.setup import createPartner
from bk_service.requests.tests.utils.setup import createShareRequest


class SharesRequestTestCase(TestCase):
    """ Shares Request test class """

    def setUp(self):
        partner = createPartner()
        xxx = createShareRequest(partner)
        import pdb
        pdb.set_trace()

    def test_State_success(self):
        """ Shares Request success """
        shareRequest = ShareRequest.objects.get(id=1)
        self.assertEqual(shareRequest.amount, 10000)
        self.assertEqual(shareRequest.quantity, 1)
