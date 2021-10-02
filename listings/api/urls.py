from django.urls import include, path
from api import views
from rest_framework.routers import SimpleRouter

from . import views

# TODO: Create your routers and urls here
router = SimpleRouter()

urlpatterns = [
    path('homes/', views.HomeList.as_view()),
    path('addresses/', views.AddressList.as_view()),
    path('zillowdata/', views.ZillowDataList.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
