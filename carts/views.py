import json

from django import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from carts.models import Cart
from carts.services import CartService


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ["total_amount"]


@method_decorator(csrf_exempt, name="dispatch")
class CartsView(View):
    def get(self, _):
        carts = CartService.get_all_carts()
        return JsonResponse({"carts": list(carts)})

    def post(self, request):
        data = json.loads(request.body)
        form = CartForm(data)
        if not form.is_valid():
            return JsonResponse(
                {"error": form.errors},
                status=400,
            )
        cart = CartService.create_cart(total_amount=form.cleaned_data["total_amount"])
        return JsonResponse(
            {"message": "Cart created successfully!", "cart_id": cart.id},
            status=201,
        )


@method_decorator(csrf_exempt, name="dispatch")
class CheckoutView(View):
    def put(self, _, cart_id):
        cart = CartService.checkout(cart_id)
        if not cart:
            return JsonResponse(
                {"error": "Cart not found"},
                status=404,
            )
        return JsonResponse(
            {"message": "Cart closed successfully!", "cart_id": cart.id},
            status=200,
        )
