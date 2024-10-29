from django.http import JsonResponse
from django.views import View

from metrics.domain.app import app
from metrics.domain.query.get_all_metrics import GetAllMetrics


class MetricsView(View):
    def get(self, _):
        query = GetAllMetrics()
        result = app.execute_query(query)
        return JsonResponse({"metrics": [metric.to_dict() for metric in result]})
