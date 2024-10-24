from django_outbox_pattern.models import Published
from django_outbox_pattern.payloads import Payload


class OutboxService:
    @staticmethod
    def create_published(destination, body):
        published = Published.objects.create(
            destination=destination,
            body=body,
        )
        return published

    @staticmethod
    def create_received(payload: Payload):
        payload.ack()
        payload.saved = True
