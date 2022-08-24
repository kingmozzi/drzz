from django.db import models

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=1000, default="")
    rate = models.FloatField(default=0)