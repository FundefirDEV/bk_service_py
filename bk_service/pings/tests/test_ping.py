""" Users URLs. """

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase


class PingAPITestCase(APITestCase):
    """ ping test class """

    def test_ping_success(self):
        """ ping success """

        url = '/ping/'
        request = self.client.get(path=url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
