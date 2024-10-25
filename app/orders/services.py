from orders.models import Order


class OrderService:
    @staticmethod
    def get_all_orders():
        orders = Order.objects.all().values()
        return orders

    @staticmethod
    def create_order(cart_uuid, price):
        order = Order.objects.create(cart_uuid=cart_uuid, price=price)
        return order
