from django.db import transaction
from django_outbox_pattern.payloads import Payload

from metrics.services import MetricService
from outbox.services import OutboxService


def callback(payload: Payload):

    print(f"Creating metric for new order")
    with transaction.atomic():
        MetricService.create_metric(description=payload.body.get("description"))
        OutboxService.create_received(payload)
        print("Metric created successfully!")
