from .models import Store
from rest_framework import serializers

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'phone', 'category', 'schedule', 'signature', 'taste', 'service', 'waiting', 'price']
