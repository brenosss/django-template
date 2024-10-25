from django.db import models


class Order(models.Model):
    cart_uuid = models.CharField(max_length=36)
    price = models.DecimalField(max_digits=10, decimal_places=2)
