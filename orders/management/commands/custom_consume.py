from django.core.management.base import BaseCommand

from djangotemplate.stomp import handle_message


class Command(BaseCommand):
    help = "Consume messages from queue"

    def handle(self, *args, **options):
        handle_message("checkout", self.stdout.write)