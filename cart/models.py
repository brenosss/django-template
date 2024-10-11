from django.db import models


class Cart(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
