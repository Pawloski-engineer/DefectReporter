from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'defects-detail', views.DefectViewSet)
router.register(r'location-detail', views.LocationViewSet)
router.register(r'user-detail', views.UserViewSet)
router.register(r'group-detail', views.GroupViewSet)

app_name = 'reporter'
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
