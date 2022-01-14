""" Locations views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Serializers
from bk_service.locations.serializers import CountryModelSerializer

# Models
from bk_service.locations.models.countries import Country

# import pdb


class LocationsAPIView(APIView):

    def get(self, request, *args, **kwargs):

        code = kwargs['code']
        countries = Country.objects.get(is_active=True, code=code)
        serializer = CountryModelSerializer(countries,)

        return Response(serializer.data)
