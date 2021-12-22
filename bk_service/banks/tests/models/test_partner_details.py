""" Partner Details Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.partner_details import PartnerDetail
# Utils
from bk_service.banks.tests.utils.setup import create_partner_detail


class PartnerDetailTestCase(TestCase):
    """ Partner Detail test class """

    def test_partner_detail_success(self):
        partner_detail_created = create_partner_detail()
        partner_detail = PartnerDetail.objects.get(id=partner_detail_created.id)

        self.assertEqual(partner_detail.partner, partner_detail_created.partner)
        self.assertEqual(partner_detail.earnings, 0)
        self.assertEqual(partner_detail.active_credit, 0)
        self.assertEqual(partner_detail.shares, 0)
        self.assertEqual(partner_detail.document_number, '')
        self.assertEqual(partner_detail.profession, '')
        self.assertEqual(partner_detail.scholarship, 'noData')
