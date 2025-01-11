from rest_framework import serializers
from .models import Items, Categories, Store

class itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

