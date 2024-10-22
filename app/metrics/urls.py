from django.urls import path

from metrics import views

urlpatterns = [
    path("", views.MetricsView.as_view(), name="metrics"),
]
