from django.urls import path
from .views import wedding_index

urlpatterns = [
    path("", wedding_index, ""),
]
