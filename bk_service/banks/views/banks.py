""" Bank creation views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from bk_service.banks.serializers import BankModelSerializer, CreateBankSerializer
import pdb


class BankCreationAPIView(APIView):

    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = CreateBankSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        validated_data = dict(serializer.validated_data)
        partners = validated_data.pop('partners')

        bank_model_serializer = BankModelSerializer(
            data=validated_data
        )
        bank_model_serializer.is_valid(raise_exception=True)
        bank_model_validated_data = dict(bank_model_serializer.validated_data)

        bank = bank_model_serializer.create(
            name=bank_model_validated_data['name'],
            city=bank_model_validated_data['city'],
            partners=partners,
            user=request.user
        )

        return Response({"message": "Bank created"})
