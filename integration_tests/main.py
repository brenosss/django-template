import time
import requests


BASE_URL = "http://web:8000"


def _request(method, endpoint, data=None):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.request(method, url, json=data)
    return response


def test_create_cart_with_invalid_total_amount():
    response = _request("POST", "carts", {"total_amount": "invalid"})
    assert response.status_code == 400


def test_create_cart():
    response = _request("POST", "carts", {"total_amount": "5.50"})
    assert response.status_code == 201
    assert response.json()["cart_id"] == 1


def test_get_all_carts():
    response = _request("GET", "carts")
    carts = response.json()["carts"]
    assert response.status_code == 200
    assert carts[0]["id"] == 1
    assert carts[0]["total_amount"] == "5.50"


def test_checkout_cart():
    response = _request("PUT", "carts/1/checkout")
    assert response.status_code == 200

    time.sleep(5)

    response = _request("GET", "carts")
    assert response.json()["carts"][0]["closed"] == True

    response = _request("GET", "orders")
    assert response.status_code == 200
    assert response.json()["orders"][0]["cart_id"] == 1

    response = _request("GET", "metrics")
    assert response.status_code == 200
    assert response.json()["metrics"][0]["description"] == "orders_created"
    assert response.json()["metrics"][0]["count"] == 1
