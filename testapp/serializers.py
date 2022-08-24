from .models import Test
from rest_framework import serializers

class TestSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Test
        fields = ['id', 'title', 'rate']