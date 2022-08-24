from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=400, default="")
    phone = models.CharField(max_length=200, default="", blank=True)
    category = models.CharField(max_length=200, default="", blank=True)
    signature = models.CharField(max_length=200, default="", blank=True)

    opening_hours = models.CharField(max_length=1000, default="", blank=True)
    break_time = models.CharField(max_length=1000, default="", blank=True)
    last_order = models.CharField(max_length=1000, default="", blank=True)
    day_off = models.CharField(max_length=1000, default="", blank=True)

    parking = models.CharField(max_length=100, default="", blank=True)

    taste = models.FloatField(default=0.5)
    atmosphere = models.FloatField(default=0.5)
    service = models.FloatField(default=0.5)
    price = models.FloatField(default=0.5)

    #star_rating = models.FloatField(default=0)

    img_url = models.CharField(max_length=1000, default="", blank=True)
    like = models.CharField(max_length=1000, default="", blank=True)