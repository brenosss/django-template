from django.db import models


class DjangoOrder(models.Model):
    uuid = models.CharField(max_length=36, unique=True, primary_key=True)
    cart_uuid = models.CharField(max_length=36)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()
