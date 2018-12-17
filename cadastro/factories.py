import factory
from .models import Emprego, Responsavel, Usuario, Entidade, Bolsista, Projeto, Responsabilidade
from .utils.models import choice_keys_list

faker = factory.faker.Faker._get_faker(locale='pt_BR')

class EmpregoFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Emprego
	nome = factory.LazyAttribute(lambda x: faker.job()) 
	tipo = factory.Iterator(choice_keys_list(Emprego.TIPOS))

class UsuarioFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Usuario

	no_completo = factory.LazyAttribute(lambda x: faker.name_female())
	ic_ativo = True
	ic_bolsista = factory.Iterator([True, False])
	email = factory.LazyAttribute(lambda x: faker.safe_email())
	username = factory.LazyAttribute(lambda x: faker.user_name())

class ResponsavelFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Responsavel

	nome = factory.LazyAttribute(lambda x: faker.name_female())
	email = factory.LazyAttribute(lambda x: faker.safe_email())
	cpf = factory.LazyAttribute(lambda x: faker.cpf())
	data_nascimento = factory.LazyAttribute(lambda x: faker.date_of_birth())
	rg = factory.LazyAttribute(lambda x: faker.ssn())
	orgao_expedidor = factory.LazyAttribute(lambda x: faker.currency_code())
	telefone = '(00) 0000-0000'
	celular = '(00) 9 0000-0000'
	matricula = factory.LazyAttribute(lambda x: faker.ssn())
	ic_ativo = True

class EntidadeFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Entidade

	nome = factory.LazyAttribute(lambda x: faker.company())
	email = factory.LazyAttribute(lambda x: faker.safe_email())
	cnpj = factory.LazyAttribute(lambda x: faker.cnpj())
	endereco = factory.LazyAttribute(lambda x: faker.address())
	cidade = factory.LazyAttribute(lambda x: faker.city())
	cep = factory.LazyAttribute(lambda x: faker.ean8())
	uf = factory.Iterator(choice_keys_list(Bolsista.UFS))
	telefone = '(00) 0000-0000'
	esfera_administrativa = factory.Iterator(choice_keys_list(Entidade.ESFERA_ADMINISTRATIVA))
	ic_ativo = True

	banco = factory.Iterator(choice_keys_list(Bolsista.COD_BANCO))
	agencia = factory.LazyAttribute(lambda x: faker.ean8())
	tipo_conta = factory.Iterator(choice_keys_list(Bolsista.TIPO_CONTA))
	conta = factory.LazyAttribute(lambda x: faker.ean8())
	praca_pagamento = factory.LazyAttribute(lambda x: faker.catch_phrase_attribute())

class BolsistaFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Bolsista

	tipo_vinculo = factory.Iterator(choice_keys_list(Bolsista.TIPOS_VINCULOS))

	no_bolsista = factory.LazyAttribute(lambda x: faker.name_male())
	email = factory.LazyAttribute(lambda x: faker.safe_email())
	cpf = factory.LazyAttribute(lambda x: faker.cpf())	
	dt_nascimento = factory.LazyAttribute(lambda x: faker.date_of_birth())
	rg = factory.LazyAttribute(lambda x: faker.ssn())
	orgao_expedidor = factory.LazyAttribute(lambda x: faker.currency_code())
	telefone = '(00) 0000-0000'
	celular = '(00) 9 0000-0000'
	matricula = factory.LazyAttribute(lambda x: faker.ssn())
	ic_ativo = True

	pis_nit = factory.LazyAttribute(lambda x: faker.ean(length=13))
	link_lattes = factory.LazyAttribute(lambda x: 'http://lattes.cnpq.br/{}'.format(faker.ean(length=13)))

	endereco = factory.LazyAttribute(lambda x: faker.address())
	cidade = factory.LazyAttribute(lambda x: faker.city())
	cep = factory.LazyAttribute(lambda x: faker.ean8())
	uf = factory.Iterator(choice_keys_list(Bolsista.UFS))

	banco = factory.Iterator(choice_keys_list(Bolsista.COD_BANCO))
	agencia = factory.LazyAttribute(lambda x: faker.ean8())
	tipo_conta = factory.Iterator(choice_keys_list(Bolsista.TIPO_CONTA))
	conta = factory.LazyAttribute(lambda x: faker.ean8())

	email_unb = factory.LazyAttribute(lambda x: faker.safe_email())
	telefone_local = '(00) 0000-0000'

class ProjetoFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Projeto

	nome = factory.LazyAttribute(lambda x: faker.sentence(nb_words=6))
	sigla = factory.Sequence(lambda n: '{}{}'.format(faker.word(), n))

	periodo_execucao = 'De tal data até outra data'
	duracao = 'Alguns meses'
	identificacao_objeto = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=1000))
	justificativa_proposta = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=1000))
	referencias_bibliograficas = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=1000))
	
	metodologia = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=1000))
	gestao_transferencia_tecnologia = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=1000))

	entidade_concedente = factory.Iterator(Entidade.objects.all())
	entidade_proponente = factory.Iterator(Entidade.objects.all())

	responsavel_concedente = factory.Iterator(Responsavel.objects.all())
	responsavel_proponente = factory.Iterator(Responsavel.objects.all())

	responsavel_tecnico_concedente = factory.Iterator(Responsavel.objects.all())
	responsavel_tecnico_proponente = factory.Iterator(Responsavel.objects.all())


class ResponsabilidadeFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Responsabilidade

	entidade = factory.Iterator(Entidade.objects.all())
	responsavel = factory.Iterator(Responsavel.objects.all())
	cargo = factory.Iterator(Emprego.objects.filter(tipo=Emprego.CARGO))
	ic_ativo = True

