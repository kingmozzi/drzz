from .models import User
from rest_framework import serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'email', 'birth', 'age', 'sex', 'taste', 'service', 'atmosphere', 'price', 'mucket', 'friend']