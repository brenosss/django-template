from django.db import transaction
from django_outbox_pattern.payloads import Payload

from orders.services import OrderService
from outbox.services import OutboxService


def callback(payload: Payload):
    print(
        f"Creating order for cart {payload.body['cart_uuid']} with price {payload.body['price']}"
    )
    with transaction.atomic():
        OrderService.create_order(
            cart_uuid=payload.body.get("cart_uuid"),
            price=payload.body.get("price"),
        )
        OutboxService.create_received(payload)
        print("Order created successfully!")
