""" Meeting Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.earning_shares import EarningShare
# Utils
from bk_service.banks.tests.utils.setup import create_earning_share


class EarningShareTestCase(TestCase):
    """ EarningShare test class """

    def test_earning_share_success(self):
        earning_share_created = create_earning_share()
        earning_share = EarningShare.objects.get(id=earning_share_created.id)

        self.assertEqual(earning_share.meeting, earning_share_created.meeting)
        self.assertEqual(earning_share.share, earning_share_created.share)
        self.assertEqual(earning_share.earning_by_share, 10)
        self.assertEqual(earning_share.total_earning_by_share, 100)
        self.assertEqual(earning_share.is_paid, False)
