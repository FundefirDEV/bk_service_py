#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils commons
from bk_service.utils.tests.requests import get_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *

# Utils
from bk_service.utils.tests.test_security import security_test_get
from decimal import Decimal
from collections import OrderedDict


URL = '/banks/profile/'


class ProfileAPITestCase(APITestCase):
    """ GET Partners test class """

    def setUp(self):
        security_test_get(self=self, URL=URL)
        self.partner = create_partner()

    def test_profile_success(self):
        """ profile success """

        country = self.partner.user.city.state.country

        response = {
            'partner': OrderedDict(
                [('id', self.partner.id),
                 ('role', 'partner'),
                 ('phone_number', '31300000000'),
                 ('phone_region_code', '+1'),
                 ('bank', self.partner.bank.id),
                 ('user', OrderedDict(
                     [('id', self.partner.user.id),
                      ('email', 'user@mail.com'),
                      ('username', 'user@mail.com'),
                      ('gender', ''),
                      ('first_name', 'Brea'),
                      ('last_name', 'Brea'),
                      ('phone_number', '31300000000'),
                      ('city', OrderedDict(
                          [('id', self.partner.user.city.id), ('name', 'Bogota')])),
                      ('is_verified', False),
                      ('is_staff', False)]))]),
            'earnings': Decimal('0.0000'),
            'active_credit': Decimal('0.0000'),
            'shares': 0,
            'document_number': '',
            'profession': '',
            'scholarship': 'noData',
            'birth_date': None,
            'profit_obtained': Decimal('0.0000'),
            'country': {
                'id': country.id,
                'name': country.name,
                'code': country.code,
            }
        }

        request = get_with_token(URL=URL, user=self.partner.user)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, response)
