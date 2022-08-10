from .models import Course
from rest_framework import serializers, viewsets

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Course
        fields = ['id', 'user_id', 'share_user', 'start_day', 'end_day', 'content']