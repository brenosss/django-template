import json
from django.core.management.base import BaseCommand
from django_outbox_pattern.models import Published

from djangotemplate.stomp import send_message_to_queue


class Command(BaseCommand):
    help = "Publish messages to queue"

    def handle(self, *args, **options):
        unpublisheds = Published.objects.filter(status=1)  # Unpublished messages
        for unpublished in unpublisheds:
            body_json = json.dumps(unpublished.body)
            send_message_to_queue(unpublished.destination, body_json)
            unpublished.status = 2  # Mark as published
            unpublished.save()
            self.stdout.write('Successfully added to queue "%s"' % unpublished.id)
