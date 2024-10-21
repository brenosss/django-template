from django.db import transaction

from carts.models import Cart
from outbox.services import OutboxService


class CartService:
    @staticmethod
    def get_all_carts():
        carts = Cart.objects.all().values()
        return carts

    @staticmethod
    def create_cart(total_amount):
        cart = Cart.objects.create(total_amount=total_amount)
        return cart

    @staticmethod
    def checkout(cart_id):
        with transaction.atomic():
            cart = Cart.objects.filter(id=cart_id).first()
            if not cart:
                return False  # We can raise a custom exception here later
            cart.closed = True
            cart.save()
            OutboxService.create_published(
                destination="/topic/orders.new",
                body={"cart_id": cart.id, "price": str(cart.total_amount)},
            )
        return cart
