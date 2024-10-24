from django.test import TestCase
from unittest.mock import patch
from django_outbox_pattern.payloads import Payload
from outbox.services import OutboxService


class OutboxServiceTest(TestCase):
    def test_create_published(self):
        published = OutboxService.create_published("destination", "body")
        self.assertIsNotNone(published.id)
        self.assertEqual(published.destination, "destination")
        self.assertEqual(published.body, "body")

    @patch.object(Payload, "ack")
    def test_create_received(self, mock_payload_ack):
        payload = Payload(connection=None, body=None, headers=None)
        OutboxService.create_received(payload)
        mock_payload_ack.assert_called_once()
