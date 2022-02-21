""" Partner Admin serializers """

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.banks.models.partners import Partner

# Utils Errors
from bk_service.utils.constants_errors import build_error_message
from bk_service.utils.constants_errors import *
from bk_service.utils.exceptions_errors import CustomException


class PartnersAdminSerializer(serializers.ModelSerializer):
    """ Partner Admin serializers """
    id = serializers.CharField(
        required=True
    )
    role = serializers.CharField(
        required=True
    )

    class Meta:
        model = Partner
        fields = ('id', 'role')

    def update_admin(partner_id, role, bank):
        partner = Partner.objects.get(pk=partner_id, bank=bank)
        partner.role = role
        partner.save()
