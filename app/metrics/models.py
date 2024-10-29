from django.db import models


class DjangoMetric(models.Model):
    uuid = models.CharField(max_length=36, unique=True, primary_key=True)
    description = models.CharField(max_length=255, unique=True, null=False)
    count = models.IntegerField()
