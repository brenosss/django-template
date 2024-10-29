from django.db import transaction
from django_outbox_pattern.payloads import Payload

from metrics.domain.app import app
from metrics.domain.command.create_metric import CreateMetricCommand
from metrics.domain.command.increment_metric import IncrementMetricCommand
from metrics.domain.query.get_metric_by_description import GetMetricByDescription

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
        query = GetMetricByDescription(description)
        result = app.execute_query(query)
        if not result:
            command = CreateMetricCommand(description)
        else:
            command = IncrementMetricCommand(description)
        app.execute_command(command)
        OutboxService.create_received(payload)
