from carts.models import Cart


class CartService:
    @staticmethod
    def create_cart(total_amount):
        cart = Cart.objects.create(total_amount=total_amount)
        return cart

    @staticmethod
    def checkout(cart_id):
        cart = Cart.objects.get(id=cart_id)
        cart.closed = True
        cart.save()
        return cart
