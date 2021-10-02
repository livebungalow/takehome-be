from rest_framework import serializers
from api.models import Home, Address, ZillowData


class BaseAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class BaseZillowDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZillowData
        fields = '__all__'


class HomeSerializer(serializers.ModelSerializer):
    address = BaseAddressSerializer()
    zillow_data = BaseZillowDataSerializer()

    class Meta:
        model = Home
        fields = '__all__'


class AddressSerializer(BaseAddressSerializer):
    home = serializers.SerializerMethodField()

    def get_home(self, address):
        # get id of foreignkey related home model object
        if address.home_set.all()[0].id:
            return {
                'id': address.home_set.all()[0].id
            }
        return {'id': None}


class ZillowDataSerializer(BaseZillowDataSerializer):
    home = serializers.SerializerMethodField()

    def get_home(self, address):
        # get id of one foreignkey related home model object
        if address.home_set.all():
            return {
                'id': address.home_set.all()[0].id
            }
        return {'id': None}


