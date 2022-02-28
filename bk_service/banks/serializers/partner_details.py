""" Partner Details serializers """

# Django

# Django REST Framework
from rest_framework import serializers

# Models
from bk_service.banks.models.partner_details import PartnerDetail

# Serializers
from bk_service.banks.serializers import PartnerModelSerializer

# Utils


class PartnerDetailModelSerializer(serializers.ModelSerializer):
    """ Partner detail model serializers """

    partner = PartnerModelSerializer(read_only=True)

    class Meta:
        model = PartnerDetail
        fields = (
            'partner',
            'earnings',
            'profit_obtained',
            'active_credit',
            'shares',
            'document_number',
            'profession',
            'scholarship',
            'birth_date',
        )
