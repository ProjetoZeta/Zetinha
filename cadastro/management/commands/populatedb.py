from django.core.management.base import BaseCommand, CommandError
import factory
from cadastro.factories import EmpregoFactory, ResponsavelFactory, UsuarioFactory, EntidadeFactory

# see https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/#writing-custom-django-admin-commands

class Command(BaseCommand):
	help = 'Populates the bd with mock data'

	def handle(self, *args, **options):
		EmpregoFactory.create_batch(size=15)
		ResponsavelFactory.create_batch(size=15)
		UsuarioFactory.create_batch(size=15)
		EntidadeFactory.create_batch(size=15)
		
		