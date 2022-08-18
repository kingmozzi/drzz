from django.db import models

# Create your models here.
class Review(models.Model):
    user_id = models.IntegerField(default=0)
    store_id = models.IntegerField(default=0)
    create_date = models.CharField(max_length=200, default="")
    content = models.CharField(max_length=1000, default="")
    star_rating = models.IntegerField(default=0)

    taste = models.FloatField(default=0.5)
    atmosphere = models.FloatField(default=0.5)
    service = models.FloatField(default=0.5)
    price = models.FloatField(default=0.5)