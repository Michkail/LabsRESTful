import uuid
# from cassandra.cqlengine import columns
# from django_cassandra_engine.models import DjangoCassandraModel
# from cassandra.cqlengine.models import Model as PythonCassandraModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Please fill the Email form')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    photo_profile = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='photo_profile/')
    is_client = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        if self.first_name and isinstance(self.first_name, str):
            self.first_name = self.first_name.strip().title()

        if self.last_name and isinstance(self.last_name, str):
            self.last_name = self.last_name.strip().title()

        super(User, self).save(*args, **kwargs)

#
#
# class Address(DjangoCassandraModel, PythonCassandraModel):
#     address_id = columns.UUID(primary_key=True, default=uuid.uuid4)
#     street = columns.Text(max_length=255)
#     city = columns.Text(max_length=255)
#     state = columns.Text(max_length=255)
#     zip_code = columns.Text(max_length=10)
#
#
# class Company(DjangoCassandraModel, PythonCassandraModel):
#     company_id = columns.UUID(primary_key=True, default=uuid.uuid4)
#     name = columns.Text(max_length=255)
#     address_id = columns.UUID(required=False)
#
#
# class User(DjangoCassandraModel, PythonCassandraModel):
#     user_id = columns.UUID(primary_key=True, default=uuid.uuid4)
#     username = columns.Text(max_length=20, required=True)
#     first_name = columns.Text(max_length=30)
#     last_name = columns.Text(max_length=30)
#     address = columns.Map(columns.Text, columns.Text, required=False)
#     company_id = columns.UUID(required=False)
#     password = columns.Text()
#     is_staff = columns.Boolean(required=False, default=False)
#     is_superuser = columns.Boolean(required=False, default=False)
#     is_active = columns.Boolean(required=False, default=False)
#     last_login = columns.DateTime()
#     date_updated = columns.DateTime()
#     date_joined = columns.Date()
#
#     def __str__(self):
#         return self.username
