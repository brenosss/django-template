from django.urls import path

from metrics import views

urlpatterns = [
    path("", views.index, name="metrics"),
]
