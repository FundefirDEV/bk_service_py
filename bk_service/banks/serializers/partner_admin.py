""" Partner Admin serializers """

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.banks.models.partners import Partner

# Enum
from bk_service.utils.enums.banks import PartnerType

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
        partners_admins = Partner.objects.filter(bank=bank, role=PartnerType.admin, is_active=True)
        valid_partners_admins = partners_admins.exclude(pk=partner_id)
        # import pdb
        # pdb.set_trace()
        if len(valid_partners_admins) == 0:
            raise CustomException(error=AT_LEAST_ONE_ADMIN)
        partner = get_object_or_404(Partner, pk=partner_id, bank=bank)
        partner.role = role
        partner.save()

    # def validate_admin_body(data, bank):
    #     # import pdb
    #     # pdb.set_trace()
    #     if admin == False:
    #         ids = [p['id'] for p in data if 'id' in data]
    #         partners = Partner.objects.filter(
    #             bank=bank,
    #             is_active=True,
    #         )
