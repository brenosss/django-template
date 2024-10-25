from carts.domain.repositories import cart_repository


class GetAllCarts:
    pass


def GetAllCartsHandler(GetAllCarts):
    carts = cart_repository.get_all()
    return carts
