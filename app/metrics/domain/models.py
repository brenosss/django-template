from dataclasses import dataclass

from metrics.models import DjangoMetric


@dataclass
class Metric:
    uuid: str
    description: str
    count: int

    @staticmethod
    def from_django(django_metric: DjangoMetric):
        return Metric(
            uuid=django_metric.uuid,
            count=django_metric.count,
            description=django_metric.description,
        )

    def to_django(self):
        return DjangoMetric(
            uuid=self.uuid,
            count=self.count,
            description=self.description,
        )

    def to_dict(self):
        return {"uuid": self.uuid, "count": self.count, "description": self.description}
