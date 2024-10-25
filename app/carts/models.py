from django.db import models


class DjangoCart(models.Model):
    uuid = models.CharField(max_length=36, unique=True, primary_key=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()
    closed = models.BooleanField()
