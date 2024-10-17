from django_outbox_pattern.models import Published

from django.db import transaction

from orders.models import Order


class OrderService:
    @staticmethod
    def create_order(cart_id, price):
        print(f"Creating order for cart {cart_id} with price {price}")
        with transaction.atomic():
            Order.objects.create(cart_id=cart_id, price=price)
