
# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
# Models
from bk_service.banks.models import Partner, PartnerDetail
# Enums
from bk_service.utils.enums.banks import PartnerType
# Serializer
from bk_service.banks.serializers.partner_admin import PartnersAdminSerializer
# Errors
from bk_service.utils.constants_errors import build_error_message
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import PARTNER_IS_NOT_ADMIN


class PartnerAdminApiView(APIView):
    def post(self, request, *args, **kwargs):
        partner = request.user.get_partner()
        bank = partner.bank
        data = request.data
        if partner.role != PartnerType.admin:
            raise CustomException(error=PARTNER_IS_NOT_ADMIN)
        serializer = PartnersAdminSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = dict(serializer.validated_data)

        # import pdb
        # pdb.set_trace()
        PartnersAdminSerializer.update_admin(
            partner_id=validated_data['id'],
            role=validated_data['role'],
            bank=bank)

        return Response('ok')
