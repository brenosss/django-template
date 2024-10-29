from django.http import JsonResponse
from django.views import View

from orders.domain.query.get_all_orders import GetAllOrders
from orders.domain.app import app


class OrdersView(View):
    def get(self, _):
        query = GetAllOrders()
        result = app.execute_query(query)
        return JsonResponse({"orders": [order.to_dict() for order in result]})
