from django.db import models


class Car(models.Model):
    url = models.URLField()
    title = models.CharField(
        max_length=255
    )
    price_usd = models.IntegerField()
    odometer = models.IntegerField()
    username = models.CharField(
        max_length=255
    )
    phone_number = models.CharField(
        max_length=255
    )
    image_url = models.URLField(null=True)
    images_count = models.IntegerField()
    car_number = models.CharField(
        max_length=255, null=True
    )
    car_vin = models.CharField(
        max_length=255, null=True
    )
    datetime_found = models.DateTimeField(
        auto_now_add=True
    )
