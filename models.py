from django.db import models

class Property(models.Model):
    location = models.CharField(max_length=50)
    price = models.IntegerField()
    area = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    stories = models.IntegerField()
    mainroad = models.BooleanField()
    guestroom = models.BooleanField()
    basement = models.BooleanField()
    hotwaterheating = models.BooleanField()
    airconditioning = models.BooleanField()
    parking = models.CharField(max_length=10)
    prefarea = models.BooleanField()
    furnishingstatus = models.CharField(max_length=10)
    predicted_price = models.FloatField(blank=True, null=True)