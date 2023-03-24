from django.urls import path, include
from .views import snippet_list, snippet_detail

urlpatterns = [
    path('', snippet_list),
    path('<int:pk>/', snippet_detail)
]
