# Django

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.banks.models import Credit

# Serializer
from bk_service.banks.serializers.schedule_installments import ScheduleInstallmentModelSerializer
from bk_service.banks.serializers.partners import PartnerModelSerializer


class CreditsModelSerializer(serializers.ModelSerializer):
    """ Credits Model serializers """

    schedule_installments = ScheduleInstallmentModelSerializer(many=True, read_only=True)
    partner = PartnerModelSerializer(read_only=True)

    class Meta:
        model = Credit
        fields = (
            'id',
            'created_at',
            'partner',
            'credit_request',
            'installments',
            'amount',
            'credit_use_detail',
            'credit_use',
            'payment_type',
            'schedule_installments',
            'total_interest'
        )
