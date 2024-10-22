import uuid
from datetime import timedelta

from django.db import models
from django.utils import timezone


def _one_more_day():
    return timezone.now() + timedelta(1)


class StatusChoice(models.IntegerChoices):
    FAILED = -1
    SCHEDULE = 1
    SUCCEEDED = 2


class Received(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
        help_text="Id not sequential using UUID Field",
    )
    msg_id = models.CharField(max_length=100, null=True)
    headers = models.JSONField(null=True)
    body = models.JSONField(null=True)
    added = models.DateTimeField(auto_now_add=True, db_index=True)
    expires_at = models.DateTimeField(default=_one_more_day)
    retry = models.PositiveIntegerField(default=0)
    status = models.IntegerField(
        choices=StatusChoice.choices, default=StatusChoice.SUCCEEDED
    )

    @property
    def destination(self):
        return self.headers.get("destination", "") if self.headers else ""

    class Meta:
        verbose_name = "custom_received"
        db_table = "custom_received"

    def __str__(self):
        return f"{self.destination} - {self.body}"
