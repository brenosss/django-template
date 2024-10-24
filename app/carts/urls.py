from django.urls import path

from carts import views

urlpatterns = [
    path("", views.CartsView.as_view(), name="carts"),
    path("/<int:cart_id>/checkout", views.CheckoutView.as_view(), name="checkout"),
]