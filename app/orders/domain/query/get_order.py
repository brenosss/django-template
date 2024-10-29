from orders.domain.repositories import order_repository


class GetOrder:
    def __init__(self, order_uuid):
        self.order_uuid = order_uuid


def GetOrderHandler(GetOrder):
    order = order_repository.get(GetOrder.order_uuid)
    return order
