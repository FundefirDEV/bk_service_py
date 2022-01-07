""" Locations serializers """

# Django

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.locations.models import Country, State, City

from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import *


# class LocationSerializer(serializers.Serializer):
#     countries = CountryModelSerializer(many=True)
#     states = StateModelSerializer(many=True)
#     cities = CityModelSerializer(many=True)


class CityModelSerializer(serializers.ModelSerializer):
    """ City model serializers """
    class Meta:
        model = City
        fields = ('name',)


class StateModelSerializer(serializers.ModelSerializer):
    """ State model serializers """

    cities = CityModelSerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = ('name', 'cities')


class CountryModelSerializer(serializers.ModelSerializer):
    """ Country model serializers """

    states = StateModelSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('name', 'code', 'states', )
