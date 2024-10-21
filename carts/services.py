from django.db import transaction

from carts.models import Cart
from outbox.services import OutboxService


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
            OutboxService.create_published(
                destination="/topic/orders.new",
                body={"cart_id": cart.id, "price": str(cart.total_amount)},
            )
        return cart
