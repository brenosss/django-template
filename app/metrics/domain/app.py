from metrics.domain.command.create_metric import (
    CreateMetricCommand,
    CreateMetricCommandHandler,
)
from metrics.domain.command.increment_metric import (
    IncrementMetricCommand,
    IncrementMetricCommandHandler,
)
from metrics.domain.query.get_all_metrics import GetAllMetrics, GetAllMetricsHandler
from metrics.domain.query.get_metric_by_description import (
    GetMetricByDescription,
    GetMetricByDescriptionHandler,
)


class App:
    command_handlers = {
        CreateMetricCommand: CreateMetricCommandHandler,
        IncrementMetricCommand: IncrementMetricCommandHandler,
    }

    query_handlers = {
        GetAllMetrics: GetAllMetricsHandler,
        GetMetricByDescription: GetMetricByDescriptionHandler,
    }

    def execute_command(self, command):
        handler = self.command_handlers[type(command)]
        return handler(command)

    def execute_query(self, query):
        handler = self.query_handlers[type(query)]
        return handler(query)


app = App()
