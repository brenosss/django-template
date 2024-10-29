from uuid import uuid4

from carts.domain.repositories import cart_repository

from outbox.domain.command.create_published import CreatePublishedCommand
from outbox.domain.app import app


class CheckoutCartCommand:
    def __init__(self, cart_uuid: str):
        self.uuid = str(uuid4())
        self.cart_uuid = cart_uuid


def CheckoutCartCommandHandler(command: CheckoutCartCommand) -> str:
    cart = cart_repository.get(command.cart_uuid)
    cart.closed = True
    cart_repository.update(cart)

    command = CreatePublishedCommand(
        destination="/topic/orders.new",
        body={"cart_uuid": cart.uuid, "price": str(cart.total_amount)},
    )

    app.execute_command(command)

    return cart.uuid
