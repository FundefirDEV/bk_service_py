#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils commons
from bk_service.users.tests.utils.commons import *
from bk_service.locations.tests.utils.setup import create_locations
from bk_service.utils.tests.requests import get_with_token, post_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *

# Utils
from bk_service.utils.enums.banks import PartnerType
from bk_service.utils.tests.test_security import security_test_get


URL = '/banks/partners/'


class PartnersAPITestCase(APITestCase):
    """ GET Partners test class """

    def setUp(self):
        security_test_get(self=self, URL=URL)
        self.partner = create_partner()
        self.guest = invite_partner(bank=self.partner.bank)

    def test_partners_success(self):
        """ Partners success """

        response = [
            {'id': self.partner.id,
             'phone': self.partner.phone_number,
             'phone_region_code': self.partner.phone_region_code,
             'first_name': self.partner.user.first_name,
             'last_name': self.partner.user.last_name,
             'name':  f'{ self.partner.user.first_name} {self.partner.user.last_name}',
             'is_active': True, 'role': PartnerType.partner,
             },
            {'id': self.guest.id,
             'phone': self.guest.phone_number,
             'phone_region_code': self.partner.phone_region_code,
             'name':  self.guest.name,
             'is_active': False,
             'role': PartnerType.guest
             }
        ]

        request = get_with_token(URL=URL, user=self.partner.user)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, response)
