from django.urls import path

from carts import views

urlpatterns = [
    path("", views.index, name="carts"),
    path("/<int:cart_id>/checkout", views.checkout, name="checkout"),
]
