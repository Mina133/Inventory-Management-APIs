from rest_framework import serializers
from .models import Items, Categories

class itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

