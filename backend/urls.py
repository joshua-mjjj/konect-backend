from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('konnect/backend/api/', include('api.urls')),
    path('konnect/backend/api/authentication/', include('accounts.urls')),
    path('konnect/backend/api/', include('profiles.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
