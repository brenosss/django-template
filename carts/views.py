import json

from django import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from orders.services import craete_order

from carts.models import Cart
from carts.services import CartService


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ["total_amount"]


def is_json_valid(body):
    try:
        json.loads(body)
        return True
    except:
        return False


@csrf_exempt  # Disable CSRF for simplicity
def index(request):
    match request.method:
        case "POST":
            if not is_json_valid(request.body):
                return JsonResponse({"error": "Invalid JSON"}, status=400)
            form = CartForm(json.loads(request.body))
            if not form.is_valid():
                return JsonResponse({"error": form.errors}, status=400)
            cart = CartService.create_cart(form.cleaned_data["total_amount"])
            return JsonResponse(
                {"message": "Cart created successfully!", "cart_id": cart.id},
                status=201,
            )
        case "GET":
            all_carts = Cart.objects.all()
            return JsonResponse(
                {
                    "carts": [
                        {
                            "id": cart.id,
                            "total_amount": cart.total_amount,
                            "created_at": cart.created_at,
                            "closed": cart.closed,
                        }
                        for cart in all_carts
                    ]
                }
            )
        case _:
            return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt  # Disable CSRF for simplicity
def checkout(request, cart_id):
    if request.method != "PUT":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        cart = CartService.checkout(cart_id)
        craete_order(cart_id, price=cart.total_amount)

        return JsonResponse(
            {"message": "Cart closed successfully!", "cart_id": cart.id},
            status=200,
        )
    except Cart.DoesNotExist:
        return JsonResponse({"error": "Cart not found"}, status=404)
