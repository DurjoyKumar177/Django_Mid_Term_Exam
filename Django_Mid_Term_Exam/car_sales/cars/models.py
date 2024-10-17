from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User

#Create your models here.

class Car(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='cars/media/uploads/', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
