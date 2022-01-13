""" Location test !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils commons
from bk_service.locations.tests.utils.setup import create_locations
from bk_service.utils.tests.requests import get_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *

# Models
from bk_service.locations.models import *

# test-utils
from bk_service.utils.tests.test_security import security_test_get

import json

# import pdb

URL = '/locations/location/'


class BankSuccessAPITestCase(APITestCase):
    """ Locations success test class """

    def setUp(self):
        security_test_get(self=self, URL=f'{URL}CO')

        city = create_locations(city_name='Distrito Capital')
        self.user = create_user(city)
        self.city_id = city.id

    def test_get_locations_success(self):
        """ Locations success """

        country_body = {
            "name": "Colombia",
            "code": "CO",
            "states": [
                {
                    "name": "Bogota",
                    "cities": [
                        {
                            "id": self.city_id,
                            "name": "Distrito Capital",
                        },
                    ]
                },
            ],
        },

        request = get_with_token(URL=f'{URL}CO', user=self.user,)

        body = json.dumps(request.data)
        status_code = request.status_code

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, json.dumps(country_body[0]))
