"""Main URLs module."""

# Django
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

# Views
from .views import PingAPIView

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('ping', PingAPIView.as_view(),),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
