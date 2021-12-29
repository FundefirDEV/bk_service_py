""" Locations views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Serializers
from bk_service.locations.serializers import CountryModelSerializer

# Models
from bk_service.locations.models.countries import Country

import pdb


class LocationsAPIView(APIView):

    def get(self, request, *args, **kwargs):

        code = request.user.city.state.country.code
        countries = Country.objects.filter(is_active=True, code=code)
        serializer = CountryModelSerializer(countries, many=True)

        return Response(serializer.data)
