# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models import EarningShare

# Serializers
from bk_service.banks.serializers import EarningShareModelSerializer


class EarningShareModelAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        earningShares = EarningShare.objects.filter(share__partner=partner)
        serializer = EarningShareModelSerializer(earningShares, many=True)

        return Response(serializer.data)
