from carts.domain.repositories import cart_repository


class GetCart:
    def __init__(self, cart_uuid):
        self.cart_uuid = cart_uuid


def GetCartHandler(GetCart):
    cart = cart_repository.get(GetCart.cart_uuid)
    return cart
