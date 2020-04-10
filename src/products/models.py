from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=220)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank=True)
    salesman = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        super().save(*args,**kwargs)

    def __str__(self):
        return "Solled {} - {} items for {}".format(self.product.name, self.quantity, self.total_price)
