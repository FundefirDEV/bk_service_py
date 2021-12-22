""" Partner serializers """

# Django

# Django REST Framework
from rest_framework import serializers
# from rest_framework.validators import UniqueValidator

# Models
from bk_service.banks.models import Partner


class PartnerModelSerializer(serializers.ModelSerializer):
    """ Partner model serializers """
    class Meta:
        model = Partner
        fields = ('id', 'role', 'phone_number', 'phone_region_code', 'bank',
                  'user',)
