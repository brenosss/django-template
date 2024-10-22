import unittest
import requests


def fetch_data_from_api(endpoint):
    base_url = "http://web:8000"
    response = requests.get(f"{base_url}/{endpoint}")
    response.raise_for_status()  # Raise an exception for 4xx/5xx errors
    return response.json()


class TestAPICalls(unittest.TestCase):

    def test_successful_request(self):
        endpoint = "carts"

        result = fetch_data_from_api(endpoint)
        self.assertIsInstance(result["carts"], list)


if __name__ == "__main__":
    unittest.main()
