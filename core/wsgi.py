"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from cassandra.cqlengine.management import sync_table
# from user.models import Address, Company, User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()

# print("Syncing model Address...")
# sync_table(Address)
# print("Address has been synced")
#
# print("Syncing model Company...")
# sync_table(Company)
# print("Address has been synced")
#
# print("Syncing model User...")
# sync_table(User)
# print("Address has been synced")