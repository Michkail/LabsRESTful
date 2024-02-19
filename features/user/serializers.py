from rest_framework import serializers
from .models import User


class UsersSerializer(serializers.ModelSerializer):
    user_id = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['password', 'last_login']


# class UserSerializer(serializers.Serializer):
#     user_id = serializers.UUIDField()
#     username = serializers.CharField(max_length=20)
#     first_name = serializers.CharField(max_length=30, required=False)
#     last_name = serializers.CharField(max_length=30, required=False)
#     password = serializers.CharField()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'last_name', 'password', 'is_superuser', 'is_staff']
