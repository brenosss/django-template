from celery import shared_task

from django.core.management import call_command


@shared_task
def publish_outbox_messages():
    call_command(
        "publish"
    )  # Send message through STOMP protocol to the configured broker
