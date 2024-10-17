# callbacks.py
from django.db import transaction
from django_outbox_pattern.payloads import Payload
from orders.models import Order

def callback(payload: Payload):

    print(f"Creating order for cart {payload.body['cart_id']} with price {payload.body['price']}")
    with transaction.atomic():
        Order.objects.create(
            cart_id=payload.body.get("cart_id"),
            price=payload.body.get("price"),
        )
        payload.save()
        print("Order created successfully!")
