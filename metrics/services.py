from metrics.models import Metric


class MetricService:
    @staticmethod
    def get_all_metrics():
        metrics = Metric.objects.all().values()
        return metrics

    @staticmethod
    def create_metric(description):
        metric, _ = Metric.objects.get_or_create(description=description)
        metric.count += 1
        metric.save()
        return metric
