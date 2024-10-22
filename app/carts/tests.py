from django.test import TestCase
from unittest.mock import patch
from carts.models import Cart
from carts.services import CartService
from outbox.services import OutboxService


class CartServiceTest(TestCase):
    def setUp(self):
        self.cart1 = Cart.objects.create(total_amount=100)
        self.cart2 = Cart.objects.create(total_amount=200)

    def test_get_all_carts(self):
        carts = CartService.get_all_carts()
        self.assertEqual(len(carts), 2)
        self.assertEqual(carts[0]["total_amount"], 100)
        self.assertEqual(carts[1]["total_amount"], 200)

    def test_create_cart(self):
        cart = CartService.create_cart(total_amount=300)
        self.assertIsNotNone(cart.id)
        self.assertEqual(cart.total_amount, 300)

    def test_checkout_non_existent_cart(self):
        cart = CartService.checkout(999)
        self.assertFalse(cart)

    @patch.object(OutboxService, "create_published")
    def test_checkout(self, mock_create_published):
        cart = CartService.checkout(self.cart1.id)
        self.assertTrue(cart.closed)
        mock_create_published.assert_called_once_with(
            destination="/topic/orders.new",
            body={"cart_id": cart.id, "price": str(cart.total_amount)},
        )
