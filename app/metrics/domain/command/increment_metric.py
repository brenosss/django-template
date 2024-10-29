from metrics.domain.repositories import metric_repository


class IncrementMetricCommand:
    def __init__(self, description: str):
        self.description = description


def IncrementMetricCommandHandler(command: IncrementMetricCommand) -> str:
    metric = metric_repository.get_by_description(command.description)
    metric.count += 1
    metric_repository.update(metric)
    return metric.uuid
