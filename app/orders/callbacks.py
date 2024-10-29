from django.db import transaction
from django_outbox_pattern.payloads import Payload

from orders.domain.command.create_order import CreateOrderCommand
from orders.domain.app import app


def callback(payload: Payload):
    print(
        f"Creating order for cart {payload.body['cart_uuid']} with price {payload.body['price']}"
    )
    with transaction.atomic():
        command = CreateOrderCommand(
            cart_uuid=payload.body.get("cart_uuid"),
            price=payload.body.get("price"),
        )
        app.execute_command(command)
        payload.ack()
        payload.saved = True
        print("Order created successfully!")
