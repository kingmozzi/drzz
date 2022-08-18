from .models import Review
from rest_framework import serializers

class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'user_id', 'store_id', 'create_date', 'content', 'star_rating', 'taste', 'service', 'atmosphere', 'price']