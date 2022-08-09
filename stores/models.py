from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    schedule = models.CharField(max_length=1000)
    signiture = models.CharField(max_length=200)
    taste = models.FloatField(default=0.0)
    waiting = models.FloatField(default=0.0)
    service = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    feeling = models.FloatField(default=0.0)

    