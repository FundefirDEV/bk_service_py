""" Earning shares serializers """

# Django

# Django REST Framework
from rest_framework import serializers

# Models
from bk_service.banks.models.earning_shares import EarningShare


class EarningShareModelSerializer(serializers.ModelSerializer):
    """ earning share model serializers """

    class Meta:
        model = EarningShare
        fields = (
            'share',
            'meeting',
            'earning_by_share',
            'total_earning_by_share',
            'is_paid',
            'created_at',
        )
