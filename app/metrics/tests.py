from django.test import TestCase
from metrics.models import Metric
from metrics.services import MetricService


class MetricServiceTest(TestCase):
    def setUp(self):
        Metric.objects.create(description="Test Metric 1", count=1)
        Metric.objects.create(description="Test Metric 2", count=2)

    def test_get_all_metrics(self):
        metrics = MetricService.get_all_metrics()
        self.assertEqual(len(metrics), 2)
        self.assertEqual(metrics[0]["description"], "Test Metric 1")
        self.assertEqual(metrics[1]["description"], "Test Metric 2")

    def test_create_first_metric(self):
        description = "New Metric"
        metric = MetricService.create_metric(description)
        self.assertEqual(metric.description, description)
        self.assertEqual(metric.count, 1)

    def test_create_existing_metric(self):
        description = "Test Metric 1"
        metric = MetricService.create_metric(description)
        self.assertEqual(metric.description, description)
        self.assertEqual(metric.count, 2)
