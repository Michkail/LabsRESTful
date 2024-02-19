from django.urls import path
from .views import UserListAPIView, UserDetailAPIView, CreateUserAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('<uuid:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('create/', CreateUserAPIView.as_view(), name='create-user'),
]
