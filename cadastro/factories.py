import factory
from .models import Emprego, Responsavel, Usuario, Entidade, Bolsista, Projeto, Responsabilidade, Participante, Meta, Atividade
from .utils.models import choice_keys_list
import datetime

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

class ProjetoFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Projeto

	nome = factory.LazyAttribute(lambda x: faker.sentence(nb_words=6))
	sigla = factory.Sequence(lambda n: '{}{}'.format(faker.word(), n))

	inicio_vigencia = datetime.datetime(2018, 5, 17)
	termino_vigencia = datetime.datetime(2020, 5, 17)

	duracao = 'Alguns meses'
	identificacao_objeto = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=1000))
	justificativa_proposta = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=1000))
	referencias_bibliograficas = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=1000))
	
	metodologia = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=1000))
	gestao_transferencia_tecnologia = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=1000))

	entidade_concedente = factory.SubFactory(EntidadeFactory)
	entidade_proponente = factory.SubFactory(EntidadeFactory)

	responsavel_concedente = factory.SubFactory(ResponsavelFactory)
	responsavel_proponente = factory.SubFactory(ResponsavelFactory)

	responsavel_tecnico_concedente = factory.SubFactory(ResponsavelFactory)
	responsavel_tecnico_proponente = factory.SubFactory(ResponsavelFactory)


class ParticipanteFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Participante

	projeto = factory.Iterator(Projeto.objects.all())
	funcao = factory.Iterator(Emprego.objects.filter(tipo=Emprego.FUNCAO))
	ic_ativo = True

	categoria = factory.Iterator(choice_keys_list(Participante.CATEGORIA))
	modalidade = factory.Iterator(choice_keys_list(Participante.MODALIDADE))
	nivel = factory.Iterator(choice_keys_list(Participante.NIVEL))

	inicio_vigencia = datetime.datetime(2018, 5, 17)
	termino_vigencia = datetime.datetime(2020, 5, 17)
	periodo_total = 24
	horas_semanais = 10
	valor_mensal = 999.99
	valor_total = 999.99

class BolsistaFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Bolsista

	vinculo_unb = factory.Iterator(choice_keys_list(Bolsista.VINCULO_UNB))
	vinculo_outros = factory.Iterator(choice_keys_list(Bolsista.OUTROS_VINCULOS))
	vinculo_ies = factory.Iterator(choice_keys_list(Bolsista.VINCULO_OUTRA_IES))

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

	participante = factory.RelatedFactory(ParticipanteFactory, 'bolsista')


class ResponsabilidadeFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Responsabilidade

	entidade = factory.Iterator(Entidade.objects.all())
	responsavel = factory.Iterator(Responsavel.objects.all())
	cargo = factory.Iterator(Emprego.objects.filter(tipo=Emprego.CARGO))
	ic_ativo = True


class MetaFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Meta

	projeto = factory.Iterator(Projeto.objects.all())
	titulo = factory.LazyAttribute(lambda x: faker.sentence(nb_words=2))
	descricao = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=256))
	ic_ativo = True
	posicao = 1


class AtividadeFactory(factory.django.DjangoModelFactory):

	meta = factory.Iterator(Meta.objects.all())
	titulo = factory.LazyAttribute(lambda x: faker.sentence(nb_words=2))
	descricao = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=256))

	data_inicio = factory.LazyAttribute(lambda x: faker.date_between(start_date=datetime.datetime(2018, 5, 17), end_date=datetime.datetime(2020, 5, 17)))
	data_fim = factory.LazyAttribute(lambda x: faker.date_between(start_date=x.data_inicio, end_date=datetime.datetime(2020, 5, 17)))

	ic_ativo = True
	posicao = 1

	class Meta:
		model = Atividade
