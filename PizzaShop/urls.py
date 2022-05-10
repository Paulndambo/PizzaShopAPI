from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("auth/", include("accounts.urls")),
    path("orders/", include("orders.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path('admin/', admin.site.urls),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)