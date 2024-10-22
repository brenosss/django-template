from django.test import TestCase
from orders.models import Order
from orders.services import OrderService


class OrderServiceTest(TestCase):
    def setUp(self):
        self.order1 = Order.objects.create(cart_id=1, price=100.0)
        self.order2 = Order.objects.create(cart_id=2, price=200.0)

    def test_get_all_orders(self):
        orders = OrderService.get_all_orders()
        self.assertEqual(len(orders), 2)
        self.assertEqual(orders[0]["cart_id"], self.order1.cart_id)
        self.assertEqual(orders[0]["price"], self.order1.price)
        self.assertEqual(orders[1]["cart_id"], self.order2.cart_id)
        self.assertEqual(orders[1]["price"], self.order2.price)

    def test_create_order(self):
        cart_id = 3
        price = 300.0
        order = OrderService.create_order(cart_id, price)
        self.assertIsNotNone(order.id)
        self.assertEqual(order.cart_id, cart_id)
        self.assertEqual(order.price, price)
