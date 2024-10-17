from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car.title} ordered by {self.user.username}"
