from django.db import transaction
from django_outbox_pattern.models import Published

from carts.models import Cart


class CartService:
    @staticmethod
    def create_cart(total_amount):
        cart = Cart.objects.create(total_amount=total_amount)
        return cart

    @staticmethod
    def checkout(cart_id):
        with transaction.atomic():
            cart = Cart.objects.get(id=cart_id)
            cart.closed = True
            cart.save()
            Published.objects.create(
                destination="/queue/create_order",
                body={"cart_id": cart.id, "price": str(cart.total_amount)},
                headers={'x-dead-letter-exchange': '', 'x-dead-letter-routing-key':'DLQ.create_order' },
            )
        return cart
