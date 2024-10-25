from datetime import datetime
from uuid import uuid4
from carts.domain.models import Cart
from carts.domain.repositories import cart_repository


class CreateCartCommand:
    def __init__(self, total_amount: float):
        self.uuid = str(uuid4())
        self.total_amount = total_amount


def CreateCartCommandHandler(command: CreateCartCommand) -> str:
    cart = Cart(
        uuid=command.uuid,
        closed=False,
        created_at=datetime.now(),
        total_amount=command.total_amount,
    )
    cart_repository.save(cart)
