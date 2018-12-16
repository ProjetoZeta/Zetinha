import factory
from cadastro.models import Emprego, Responsavel, Usuario
from cadastro.utils.models import choice_keys_list

faker = factory.faker.Faker._get_faker(locale='pt_BR')

class EmpregoFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Emprego
	nome = factory.lazy_attribute(lambda x: faker.job()) 
	tipo = factory.Iterator(choice_keys_list(Emprego.TIPOS))

class UsuarioFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Usuario

	no_completo = factory.lazy_attribute(lambda x: faker.name_female())
	ic_ativo = True
	ic_bolsista = factory.Iterator([True, False])
	email = factory.lazy_attribute(lambda x: faker.safe_email())
	username = factory.lazy_attribute(lambda x: faker.user_name())

class ResponsavelFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Responsavel

	nome = factory.lazy_attribute(lambda x: faker.name_female())
	email = factory.lazy_attribute(lambda x: faker.safe_email())
	cpf = factory.lazy_attribute(lambda x: faker.cpf())
	data_nascimento = factory.lazy_attribute(lambda x: faker.date_of_birth())
	rg = factory.lazy_attribute(lambda x: faker.ssn())
	orgao_expedidor = factory.lazy_attribute(lambda x: faker.currency_code())
	telefone = '(00) 0000-0000'
	celular = '(00) 9 0000-0000'
	matricula = factory.lazy_attribute(lambda x: faker.ssn())
	ic_ativo = True

	