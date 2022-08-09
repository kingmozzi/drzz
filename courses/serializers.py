from .models import Course
from rest_framework import serializers, viewsets

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Course
        fields = ['id', 'user_id', 'shared_user', 'startday', 'endday', 'course_contents']