from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.Overview),
    path('mwesigwa', views.get_api),
    path('backend/konnect/clients/', include('api.urls_users')),
    path('backend/konnect/servers/', include('api.urls_servers')),

    path('backend/konnect/auth', obtain_auth_token),

]
