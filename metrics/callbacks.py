# callbacks.py
from django.db import transaction
from django_outbox_pattern.payloads import Payload
from metrics.models import Metric
from outbox.services import OutboxService


def callback(payload: Payload):

    print(f"Creating metric for new order")
    with transaction.atomic():
        (metric, _) = Metric.objects.get_or_create(description="orders_created")
        metric.count += 1
        metric.save()
        OutboxService.create_received(payload)
        print("Metric created successfully!")
