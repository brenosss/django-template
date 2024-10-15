from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from orders.models import Order


def list_orders():
    all_orders = Order.objects.all()
    return JsonResponse(
        {
            "orders": [
                {
                    "id": order.id,
                    "price": order.price,
                    "cart_id": order.cart_id,
                }
                for order in all_orders
            ]
        }
    )


@csrf_exempt  # Disable CSRF for simplicity
def index(request):
    match request.method:
        case "GET":
            return list_orders()
        case _:
            return JsonResponse({"error": "Invalid request method"}, status=405)
