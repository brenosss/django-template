import json

from django.test import TestCase, Client
from django.urls import reverse

from carts.models import Cart
from carts.services import CartService


class CartViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_cart_success(self):
        response = self.client.post(
            reverse("carts"),
            data=json.dumps({"total_amount": 100}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("cart_id", response.json())

    def test_create_cart_invalid_method(self):
        response = self.client.put(reverse("carts"))
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {"error": "Invalid request method"})

    def test_create_cart_missing_total_amount(self):
        response = self.client.post(
            reverse("carts"), data=json.dumps({}), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), {"error": {"total_amount": ["This field is required."]}}
        )

    def test_create_cart_invalid_json(self):
        response = self.client.post(
            reverse("carts"), data="invalid json", content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Invalid JSON"})

    def test_checkout_success(self):
        cart = Cart.objects.create(total_amount=100)
        response = self.client.put(
            reverse("checkout", args=[cart.id]), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"message": "Cart closed successfully!", "cart_id": cart.id},
        )
        cart.refresh_from_db()
        self.assertTrue(cart.closed)

    def test_checkout_invalid_method(self):
        cart = Cart.objects.create(total_amount=100)
        response = self.client.get(reverse("checkout", args=[cart.id]))
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {"error": "Invalid request method"})

    def test_checkout_not_found(self):
        response = self.client.put(
            reverse("checkout", args=[999]), content_type="application/json"
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "Cart not found"})

    def test_list_carts_success(self):
        Cart.objects.create(total_amount=100)
        response = self.client.get(reverse("carts"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("carts", response.json())


class CartServiceTestCase(TestCase):
    def test_create_cart(self):
        cart = CartService.create_cart(100)
        self.assertEqual(cart.total_amount, 100)
        self.assertFalse(cart.closed)
        self.assertIsNotNone(cart.created_at)

    def test_checkout(self):
        cart = Cart.objects.create(total_amount=100)
        cart = CartService.checkout(cart.id)
        self.assertTrue(cart.closed)
