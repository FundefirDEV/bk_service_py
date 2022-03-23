# Django

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.banks.models import Share

# Serializer
from bk_service.banks.serializers.schedule_installments import ScheduleInstallmentModelSerializer
from bk_service.banks.serializers.partners import PartnerModelSerializer


class SharesModelSerializer(serializers.ModelSerializer):
    """ Shares Model serializers """

    partner = PartnerModelSerializer(read_only=True)

    class Meta:
        model = Share
        fields = (
            'id',
            'partner',
            'is_active',
            'amount',
            'quantity',
            'share_request',
            'created_at',
        )
