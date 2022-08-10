from django.db import models

# Create your models here.
class Review(models.Model):
    user_id = models.IntegerField(default=0)
    store_id = models.IntegerField(default=0)
    create_date = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    star_rating = models.IntegerField(default=0)