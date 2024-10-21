from django_outbox_pattern.models import Published
from django_outbox_pattern.payloads import Payload


class OutboxService:

    @staticmethod
    def create_published(destination, body):
        return Published.objects.create(
            destination=destination,
            body=body,
        )

    @staticmethod
    def create_received(payload: Payload):
        return payload.save()
