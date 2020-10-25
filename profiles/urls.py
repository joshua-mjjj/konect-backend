from rest_framework import routers
from .api import ProfileViewSet
from .views import Overview

router = routers.DefaultRouter()
router.register('serviceprovider/profiles', ProfileViewSet, 'profiles')
urlpatterns = router.urls