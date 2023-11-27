import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine.models import Model as PythonCassandraModel


class Address(DjangoCassandraModel, PythonCassandraModel):
    address_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    street = columns.Text(max_length=255)
    city = columns.Text(max_length=255)
    state = columns.Text(max_length=255)
    zip_code = columns.Text(max_length=10)


class Company(DjangoCassandraModel, PythonCassandraModel):
    company_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    name = columns.Text(max_length=255)
    address_id = columns.UUID(required=False)


class User(DjangoCassandraModel, PythonCassandraModel):
    user_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    username = columns.Text(max_length=20, required=True)
    first_name = columns.Text(max_length=30)
    last_name = columns.Text(max_length=30)
    address = columns.Map(columns.Text, columns.Text, required=False)
    company_id = columns.UUID(required=False)
    password = columns.Text()

    def __str__(self):
        return self.username
