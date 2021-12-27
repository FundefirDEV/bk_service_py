from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


def get_with_token(URL, user):

    client = APIClient()
    refresh = RefreshToken.for_user(user)

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client.get(path=URL, format='json')


def post_with_token(URL, user, body):

    client = APIClient()
    refresh = RefreshToken.for_user(user)

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client.post(path=URL, data=body, format='json')
