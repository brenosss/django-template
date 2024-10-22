from django.urls import path

from orders import views

urlpatterns = [
    path("", views.OrdersView.as_view(), name="orders"),
]
