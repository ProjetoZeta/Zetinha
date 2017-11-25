from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse

class Usuario(AbstractUser):
    no_completo = models.CharField('Nome completo', max_length=64, unique=True)
    ic_ativo = models.BooleanField('Ativo', default=True)
    ic_bolsista = models.BooleanField('Bolsista', default=True)
    email = models.EmailField('Email', unique=True)
    class Meta:
        verbose_name = "usuário"

class Entidade(models.Model):
    co_entidade = models.CharField('Código', max_length=32, unique=True)
    no_entidade = models.CharField('Nome', max_length=32, unique=True)
    sg_entidade = models.CharField('Sigla', max_length=32, unique=True)
    ic_ativo = models.BooleanField('Ativo')
    cnpj = models.IntegerField('CNPJ', unique=True)
    telefone = models.IntegerField('Telefone')
    cep = models.IntegerField('CEP')
    nu_municipio = models.IntegerField('Número do municipio')
    co_esfera = models.CharField('Esfera', max_length=32, unique=True)
    de_endereco = models.CharField('Endereço', max_length=128, unique=True)

class Cargo(models.Model):
    no_cargo = models.CharField('Nome', max_length=6, unique=True)
    ic_ativo = models.BooleanField('Ativo')

class Funcao(models.Model):
    no_funcao = models.CharField('Nome', max_length=6, unique=True)
    ic_ativo = models.BooleanField('Ativo')
    class Meta:
        verbose_name_plural = "funções"
        verbose_name = "função"

class Responsavel(models.Model):
    no_responsavel = models.CharField('Nome', max_length=32, unique=True)
    cpf = models.IntegerField('CPF')
    telefone = models.IntegerField('Telefone')
    co_matricula = models.CharField('Matrícula', max_length=32, unique=True)
    ic_ativo = models.BooleanField('Ativo')

    class Meta:
        verbose_name_plural = "responsáveis"
        verbose_name = "responsável"
