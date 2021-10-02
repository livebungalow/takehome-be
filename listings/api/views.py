from api.models import Home, ZillowData, Address
from api.serializers import HomeSerializer, AddressSerializer, ZillowDataSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from url_filter.filtersets import ModelFilterSet


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class HomeFilterSet(ModelFilterSet):
    class Meta(object):
        model = Home
        fields = '__all__'


class AddressFilterset(ModelFilterSet):
    class Meta(object):
        model = Address
        fields = '__all__'


class ZillowDataFilterset(ModelFilterSet):
    class Meta(object):
        model = ZillowData
        fields = '__all__'


class HomeList(generics.ListAPIView):
    """
    allows for complex query. For example:
    api/homes/?id__range=5,10
    api/homes/?price__range=0,500000
    """
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    pagination_class = StandardResultsSetPagination
    filterset_fields = '__all__'

    def get_queryset(self):
        queryset = super(HomeList, self).get_queryset()
        return HomeFilterSet(data=self.request.GET, queryset=queryset).filter()


class AddressList(generics.ListAPIView):
    """
    allows for complex query. For example:
    api/addresses/?zipcode=91302
    api/addresses/?id__range=5,10
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    pagination_class = StandardResultsSetPagination
    filterset_fields = '__all__'

    def get_queryset(self):
        queryset = super(AddressList, self).get_queryset()
        return AddressFilterset(data=self.request.GET, queryset=queryset).filter()


class ZillowDataList(generics.ListAPIView):
    """
    allows for complex query. For example:
    api/homes/?rent_estimate__range=0,500000
    """
    queryset = ZillowData.objects.all()
    serializer_class = ZillowDataSerializer
    pagination_class = StandardResultsSetPagination
    filterset_fields = '__all__'

    def get_queryset(self):
        queryset = super(ZillowDataList, self).get_queryset()
        return ZillowDataFilterset(data=self.request.GET, queryset=queryset).filter()
