from orders.domain.repositories import order_repository


class GetAllOrders:
    pass


def GetAllOrdersHandler(GetAllOrders):
    orders = order_repository.get_all()
    return orders
