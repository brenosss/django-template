from abc import ABC, abstractmethod
from typing import Optional

from metrics.domain.models import Metric
from metrics.models import DjangoMetric


class MetricRepository(ABC):
    @abstractmethod
    def save(self, metric: Metric) -> None:
        pass

    @abstractmethod
    def get_by_description(self, description: str) -> Optional[Metric]:
        pass

    @abstractmethod
    def get_all(self) -> Metric:
        pass

    @abstractmethod
    def update(self, metric: Metric) -> None:
        pass


class DjangoMetricRepository(MetricRepository):
    def save(self, metric: Metric) -> None:
        metric.to_django().save()

    def get_by_description(self, description: str) -> Optional[Metric]:
        try:
            django_metric = DjangoMetric.objects.get(description=description)
        except DjangoMetric.DoesNotExist:
            return None
        return Metric.from_django(django_metric)

    def get_all(self) -> list[Metric]:
        django_metrics = DjangoMetric.objects.all()
        return [Metric.from_django(django_metric) for django_metric in django_metrics]

    def update(self, metric: Metric) -> None:
        django_metric = metric.to_django()
        django_metric.save()


metric_repository = DjangoMetricRepository()
