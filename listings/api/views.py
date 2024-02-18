from rest_framework import (
    mixins,
    viewsets
)

from api import models, serializers

# Create your views here.
class HomeViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    
    serializer_class = serializers.HomeSerializer
    queryset = models.Home.objects.all()


class SaleDataViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    
    serializer_class = serializers.SaleDataSerializer
    queryset = models.SaleData.objects.all()


class RentDataViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    
    serializer_class = serializers.RentDataSerializer
    queryset = models.RentData.objects.all()