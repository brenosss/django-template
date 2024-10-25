from carts.domain.query.get_cart import GetCart, GetCartHandler
from carts.domain.command.checkout_cart import (
    CheckoutCartCommand,
    CheckoutCartCommandHandler,
)
from carts.domain.query.get_all_carts import GetAllCarts, GetAllCartsHandler
from carts.domain.command.create_cart import CreateCartCommand, CreateCartCommandHandler


class App:
    command_handlers = {
        CreateCartCommand: CreateCartCommandHandler,
        CheckoutCartCommand: CheckoutCartCommandHandler,
    }

    query_handlers = {GetAllCarts: GetAllCartsHandler, GetCart: GetCartHandler}

    def execute_command(self, command):
        handler = self.command_handlers[type(command)]
        return handler(command)

    def execute_query(self, query):
        handler = self.query_handlers[type(query)]
        return handler(query)


app = App()
