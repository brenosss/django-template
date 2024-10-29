from metrics.domain.repositories import metric_repository


class GetMetricByDescription:
    def __init__(self, description: str):
        self.description = description


def GetMetricByDescriptionHandler(GetMetricByDescription):
    metric = metric_repository.get_by_description(GetMetricByDescription.description)
    return metric
