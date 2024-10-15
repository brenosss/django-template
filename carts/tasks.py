from celery import shared_task
from jaiminho.relayer import EventRelayer

@shared_task
def outbox_event_relay():
    EventRelayer().relay()
    print("Events relayed successfully!")
    