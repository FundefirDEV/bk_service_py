""" Meetings serializers """

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.banks.models import Meeting


class MeetingsModelSerializer(serializers.ModelSerializer):
    """ Meeting Model serializers """

    class Meta:
        model = Meeting
        fields = (
            'bank',
            'total_shares_amount',
            'total_credits_amount',
            'total_shares_quantity',
            'total_credits_quantity',
            'total_ordinary_interest',
            'total_capital',
            'earning_by_share',
            'total_delay_interest',
            'expenditure_fund',
            'reserve_fund_of_bad_debt'
        )

    def create(self, validated_data):

        meeting = Meeting.objects.create(**validated_data)

        return meeting
