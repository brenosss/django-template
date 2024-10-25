from uuid import uuid4
from outbox.services import OutboxService
from carts.domain.repositories import cart_repository


class CheckoutCartCommand:
    def __init__(self, cart_uuid: str):
        self.uuid = str(uuid4())
        self.cart_uuid = cart_uuid


def CheckoutCartCommandHandler(command: CheckoutCartCommand) -> str:
    cart = cart_repository.get(command.cart_uuid)
    cart.closed = True
    cart_repository.update(cart)
    OutboxService.create_published(
        destination="/topic/orders.new",
        body={"cart_uuid": cart.uuid, "price": str(cart.total_amount)},
    )
    return cart.uuid
