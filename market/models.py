from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=50)
    price_per_kg = models.DecimalField(max_digits=6, decimal_places=2)
    available_quantity = models.IntegerField()

    def __str__(self):
        return self.name
