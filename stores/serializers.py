from .models import Store
from rest_framework import serializers

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'phone', 'category', 'signature', 'parking', 'taste', 'service', 'atmosphere', 'price', 'img_url', 'like', 'opening_hours', 'break_time', 'last_order', 'day_off']
