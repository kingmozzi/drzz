from django.db import models

# Create your models here.
class Course(models.Model):
    user_id = models.IntegerField(default=0)
    share_user = models.CharField(max_length=200, default="")
    start_day = models.CharField(max_length=200, default="")
    end_day = models.CharField(max_length=200, default="")
    content = models.CharField(max_length=1000, default="")