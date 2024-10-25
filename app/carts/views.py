import json

from django import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from carts.domain.query.get_all_carts import GetAllCarts
from carts.domain.query.get_cart import GetCart
from carts.domain.app import app
from carts.domain.command.create_cart import CreateCartCommand
from carts.domain.command.checkout_cart import CheckoutCartCommand


class CartForm(forms.Form):
    total_amount = forms.FloatField()


@method_decorator(csrf_exempt, name="dispatch")
class CartsView(View):
    def get(self, _):
        query = GetAllCarts()
        result = app.execute_query(query)
        return JsonResponse({"carts": [cart.to_dict() for cart in result]})

    def post(self, request):
        data = json.loads(request.body)
        form = CartForm(data)
        if not form.is_valid():
            return JsonResponse(
                {"error": form.errors},
                status=400,
            )

        command = CreateCartCommand(
            total_amount=form.cleaned_data["total_amount"],
        )
        app.execute_command(command)

        return JsonResponse(
            {"message": "Cart created successfully!", "cart_uuid": command.uuid},
            status=201,
        )


@method_decorator(csrf_exempt, name="dispatch")
class CheckoutView(View):
    def put(self, _, cart_uuid):
        query = GetCart(cart_uuid)
        result = app.execute_query(query)
        if not result:
            return JsonResponse(
                {"error": "Cart not found"},
                status=404,
            )

        command = CheckoutCartCommand(cart_uuid)
        app.execute_command(command)

        return JsonResponse(
            {"message": "Cart closed successfully!", "cart_uuid": command.cart_uuid},
            status=200,
        )
