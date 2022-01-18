""" Locations serializers """

# Django

# Django REST Framework
from rest_framework import serializers

# Models
from bk_service.locations.models import Country, State, City


class CityModelSerializer(serializers.ModelSerializer):
    """ City model serializers """
    class Meta:
        model = City
        fields = ('id', 'name',)


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
