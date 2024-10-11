from django.test import TestCase, Client
from django.urls import reverse
from .models import Cart
import json


class CartViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_cart_success(self):
        response = self.client.post(
            reverse("create_cart"),
            data=json.dumps({"total_amount": 100}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("cart_id", response.json())

    def test_create_cart_invalid_method(self):
        response = self.client.get(reverse("create_cart"))
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {"error": "Invalid request method"})

    def test_create_cart_missing_total_amount(self):
        response = self.client.post(
            reverse("create_cart"), data=json.dumps({}), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "total_amount is required."})

    def test_create_cart_invalid_json(self):
        response = self.client.post(
            reverse("create_cart"), data="invalid json", content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Invalid JSON"})

    def test_close_cart_success(self):
        cart = Cart.objects.create(total_amount=100)
        response = self.client.put(
            reverse("close_cart", args=[cart.id]), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"message": "Cart closed successfully!", "cart_id": cart.id},
        )
        cart.refresh_from_db()
        self.assertTrue(cart.closed)

    def test_close_cart_invalid_method(self):
        cart = Cart.objects.create(total_amount=100)
        response = self.client.get(reverse("close_cart", args=[cart.id]))
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {"error": "Invalid request method"})

    def test_close_cart_not_found(self):
        response = self.client.put(
            reverse("close_cart", args=[999]), content_type="application/json"
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "Cart not found"})
