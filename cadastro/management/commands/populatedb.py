from django.core.management.base import BaseCommand, CommandError
import factory
from ._factories import EmpregoFactory

# see https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/#writing-custom-django-admin-commands

class Command(BaseCommand):
    help = 'Populates the bd with mock data'

    def handle(self, *args, **options):
        EmpregoFactory.create_batch(size=2)
        
        