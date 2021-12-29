""" Users URLs. """

# Django
from django.urls import path, include

# Views
from bk_service.locations.views import LocationsAPIView

# Django REST Framework
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'locationsyy', LocationsAPIView, basename='location')

# urlpatterns = [
#     # path(r'^locations/location/', LocationsAPIView.as_view(), name='location_view'),
#     path(r'', include(router.urls)),
# ]

urlpatterns = [
    path('locations/location/', LocationsAPIView.as_view(), name='location_view'),
]
