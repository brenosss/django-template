from django.db import models


class Metric(models.Model):
    description = models.CharField(max_length=255, unique=True, null=False)
    count = models.IntegerField(default=0)
