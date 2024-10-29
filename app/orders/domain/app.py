from orders.domain.command.create_order import (
    CreateOrderCommand,
    CreateOrderCommandHandler,
)
from orders.domain.query.get_all_orders import GetAllOrders, GetAllOrdersHandler


class App:
    command_handlers = {
        CreateOrderCommand: CreateOrderCommandHandler,
    }

    query_handlers = {GetAllOrders: GetAllOrdersHandler}

    def execute_command(self, command):
        handler = self.command_handlers[type(command)]
        return handler(command)

    def execute_query(self, query):
        handler = self.query_handlers[type(query)]
        return handler(query)


app = App()
