from uuid import uuid4

from metrics.domain.models import Metric
from metrics.domain.repositories import metric_repository


class CreateMetricCommand:
    def __init__(self, description: str):
        self.uuid = str(uuid4())
        self.description = description


def CreateMetricCommandHandler(command: CreateMetricCommand) -> str:
    metric = Metric(
        uuid=command.uuid,
        count=1,
        description=command.description,
    )
    metric_repository.save(metric)
