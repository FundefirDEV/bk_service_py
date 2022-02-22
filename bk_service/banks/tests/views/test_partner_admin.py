#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils commons
from bk_service.users.tests.utils.commons import *
from bk_service.utils.tests.requests import post_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *

# Enums
from bk_service.utils.enums.banks import PartnerType
# Models
from bk_service.banks.models.partners import Partner
# Utils
from bk_service.utils.enums.banks import PartnerType
from bk_service.utils.tests.test_security import security_test_post


URL = '/banks/partner-admin/'


class PartnersAPITestCase(APITestCase):
    """ GET Partners test class """

    def setUp(self):
        security_test_post(self=self, URL=URL)
        self.partner_admin = create_partner(role=PartnerType.admin)
        self.partner_1 = create_partner(
            role=PartnerType.partner,
            bank=self.partner_admin.bank,
            email='test1@mail.com',
            phone_number='31313131313')

    def test_partners_success(self):
        """ Partners-admin success """

        body = {
            'id': self.partner_1.id,
            'role': PartnerType.admin
        }

        request = post_with_token(URL=URL, user=self.partner_admin.user, body=body)
        body = request.data
        partner1 = Partner.objects.get(pk=self.partner_1.id)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(partner1.role, PartnerType.admin)

    def test_partners_fails_no_admin(self):
        """ Partners-admin success """

        body = {
            'id': self.partner_admin.id,
            'role': PartnerType.partner
        }

        request = post_with_token(URL=URL, user=self.partner_admin.user, body=body)
        body = request.data
        partner_admin = Partner.objects.get(pk=self.partner_admin.id)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=AT_LEAST_ONE_ADMIN)})
        self.assertEqual(partner_admin.role, PartnerType.admin)
