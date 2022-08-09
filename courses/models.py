from django.db import models

# Create your models here.
class Course(models.Model):
    user_id = models.IntegerField(default=0)
    shared_user = models.CharField(max_length=200, default="")
    startday = models.CharField(max_length=200)
    endday = models.CharField(max_length=200)
    course_contents = models.CharField(max_length=1000)