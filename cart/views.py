import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from jaiminho.send import save_to_outbox

from .models import Cart


@csrf_exempt  # Disable CSRF for simplicity
def create_cart(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        data = json.loads(request.body)

        total_amount = data.get("total_amount")
        if not total_amount:
            return JsonResponse({"error": "total_amount is required."}, status=400)

        cart = Cart.objects.create(
            total_amount=total_amount,
        )

        return JsonResponse(
            {"message": "Cart created successfully!", "cart_id": cart.id},
            status=201,
        )
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)


@save_to_outbox
def add_checkout_to_queue(cart_id):
    pass


@csrf_exempt  # Disable CSRF for simplicity
def checkout(request, cart_id):
    if request.method != "PUT":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        cart = Cart.objects.get(id=cart_id)
        cart.closed = True
        cart.save()

        add_checkout_to_queue(cart_id)

        return JsonResponse(
            {"message": "Cart closed successfully!", "cart_id": cart.id},
            status=200,
        )
    except Cart.DoesNotExist:
        return JsonResponse({"error": "Cart not found"}, status=404)
