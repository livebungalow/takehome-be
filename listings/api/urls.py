from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'homes', views.HomeViewSet)
router.register(r'sales', views.SaleDataViewSet)
router.register(r'rents', views.RentDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
