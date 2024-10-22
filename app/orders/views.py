from django.http import JsonResponse
from django.views import View

from orders.services import OrderService


class OrdersView(View):
    def get(self, _):
        orders = OrderService.get_all_orders()
        return JsonResponse({"orders": list(orders)})
