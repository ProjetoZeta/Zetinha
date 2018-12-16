import factory
from cadastro.models import Emprego

faker = factory.faker.Faker._get_faker(locale='pt_BR')

class EmpregoFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Emprego
	nome = factory.lazy_attribute(lambda x: faker.job()) 
	tipo = factory.Iterator([Emprego.FUNCAO, Emprego.CARGO])