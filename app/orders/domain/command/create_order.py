from datetime import datetime
from uuid import uuid4
from orders.domain.models import Order
from orders.domain.repositories import order_repository


class CreateOrderCommand:
    def __init__(self, cart_uuid: str, price: float):
        self.uuid = str(uuid4())
        self.cart_uuid = cart_uuid
        self.price = price


def CreateOrderCommandHandler(command: CreateOrderCommand) -> str:
    order = Order(
        uuid=command.uuid,
        cart_uuid=command.cart_uuid,
        price=command.price,
        created_at=datetime.now(),
    )
    order_repository.save(order)
