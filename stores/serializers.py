from .models import Store
from rest_framework import serializers

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Store
        fields = ['name', 'address', 'phone', 'category', 'schedule', 'signiture', 'taste', 'feeling', 'service', 'waiting', 'price']
