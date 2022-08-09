from .models import User
from rest_framework import serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'date_of_birth', 'age', 'sex', 'taste', 'feeling', 'service', 'waiting', 'price', 'mucket']