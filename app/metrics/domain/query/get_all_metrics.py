from metrics.domain.repositories import metric_repository


class GetAllMetrics:
    pass


def GetAllMetricsHandler(GetAllMetrics):
    metrics = metric_repository.get_all()
    return metrics
