#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APIClient


def security_test_get(self, URL):
    """ Verify GET Request response 401"""
    client = APIClient()
    request = client.get(URL, format='json')
    body = request.data
    self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
    self.assertEqual(body,
                     {'detail': ErrorDetail(
                         string='Authentication credentials were not provided.', code='not_authenticated')}
                     )


def security_test_post(self, URL):
    """ Verify POST Request response 401"""
    client = APIClient()
    request = client.post(URL, format='json')
    body = request.data
    self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
    self.assertEqual(body,
                     {'detail': ErrorDetail(
                         string='Authentication credentials were not provided.', code='not_authenticated')}
                     )
