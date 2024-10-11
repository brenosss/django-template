from django.urls import path

from . import views

urlpatterns = [
    path("", views.create_cart, name="create_cart"),
    path("/<int:cart_id>/close", views.close_cart, name="close_cart"),
]
