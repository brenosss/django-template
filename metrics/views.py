from django.http import JsonResponse

from metrics.models import Metric


def index(request):
    if request.method == "GET":
        metrics = Metric.objects.all()
        return JsonResponse(
            {
                "metrics": [
                    {
                        "description": metric.description,
                        "count": metric.count,
                    }
                    for metric in metrics
                ]
            }
        )
