from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

from testenv.home.viewsets import FarmViewSet, PlotViewSet,UserViewSet
# , FarmerViewSet, ProjectManagerViewSet, RegionalManagerViewSet, SalesmanViewSet, TechSupportViewSet, UserViewSet

# Serializers define the API representation.


# ViewSets define the view behavior.

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)
# router.register(r'projectmanager', ProjectManagerViewSet)
# router.register(r'techsupport', TechSupportViewSet)
# router.register(r'regionalmanager', RegionalManagerViewSet)
# router.register(r'salesman', SalesmanViewSet)
# router.register(r'farmer', FarmerViewSet)
router.register(r'user', UserViewSet)
router.register(r'farm', FarmViewSet)
router.register(r'plot', PlotViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]