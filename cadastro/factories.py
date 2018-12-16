import factory
from faker import Faker
fake = Faker('pt_BR')

from .models import Emprego

class EmpregoFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Emprego
	nome = fake.job()
	tipo = factory.Iterator([Emprego.FUNCAO, Emprego.CARGO])