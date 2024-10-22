from django.db import transaction
from django_outbox_pattern.payloads import Payload

from metrics.services import MetricService
from outbox.services import OutboxService


def callback(payload: Payload):
    print(f"Creating metric for new order")

    destination_descriptions = {
        "/topic/orders.new": "orders_created",
    }

    with transaction.atomic():
        destination = payload.headers.get("destination")
        description = destination_descriptions.get(destination)
        if description == None:
            print("No metric to create for this payload")
            return
        MetricService.create_metric(description=description)
        OutboxService.create_received(payload)
        print("Metric created successfully!")
