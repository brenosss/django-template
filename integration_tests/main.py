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
    assert response.json()["cart_uuid"] is not None


def test_get_all_carts():
    new_cart_uuid = _request("POST", "carts", {"total_amount": "5.50"}).json()[
        "cart_uuid"
    ]
    response = _request("GET", "carts")
    carts = response.json()["carts"]
    assert response.status_code == 200
    assert new_cart_uuid in [cart["uuid"] for cart in carts]


def test_checkout_cart_with_invalid_cart_uuid():
    response = _request("PUT", "carts/invalid/checkout")
    assert response.status_code == 404


def test_checkout_cart():
    cart_uuid_under_test = _request("POST", "carts", {"total_amount": "5.50"}).json()[
        "cart_uuid"
    ]

    response = _request("PUT", f"carts/{cart_uuid_under_test}/checkout")
    assert response.status_code == 200

    response = _request("GET", "carts")
    assert response.status_code == 200
    carts = response.json()["carts"]
    cart_under_test = next(
        cart for cart in carts if cart["uuid"] == cart_uuid_under_test
    )
    assert cart_under_test["closed"] == True

    time.sleep(5)

    response = _request("GET", "orders")
    assert response.status_code == 200
    orders = response.json()["orders"]
    assert cart_uuid_under_test in [order["cart_uuid"] for order in orders]

    response = _request("GET", "metrics")
    assert response.status_code == 200
    metrics = response.json()["metrics"]
    assert "orders_created" in [metric["description"] for metric in metrics]
    orders_created_metric = next(
        metric for metric in metrics if metric["description"] == "orders_created"
    )
    assert orders_created_metric["count"] == 1
