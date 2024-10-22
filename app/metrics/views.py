from django.http import JsonResponse
from django.views import View

from metrics.services import MetricService


class MetricsView(View):
    def get(self, _):
        metrics = MetricService.get_all_metrics()
        return JsonResponse({"metrics": list(metrics)})
