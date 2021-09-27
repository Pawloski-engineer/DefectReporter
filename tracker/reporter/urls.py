from django.urls import path, include
# from . import views
from rest_framework import routers
from .views import locations_list, location_detail
# from .views import defects_list, defect_detail


# router = routers.DefaultRouter()
# router.register(r'defects-detail', views.DefectViewSet)
# router.register(r'location-detail', views.LocationViewSet)
# router.register(r'user-detail', views.UserViewSet)
# router.register(r'group-detail', views.GroupViewSet)

# app_name = 'reporter'
urlpatterns = [
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('locationslist/', locations_list),
    path('location/<int:pk>/', location_detail),
    # path('defectslist/', defects_list),
    # path('defect/<int:pk>/', defect_detail),

]

