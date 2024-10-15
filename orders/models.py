from django.db import models


class Order(models.Model):
    cart_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
