from django.db import models

class Entidade(models.Model):
    nu_entidade = models.IntegerField()
    co_entidade = models.CharField(max_length=32, unique=True)
    no_entidade = models.CharField(max_length=32, unique=True)
    sg_entidade = models.CharField(max_length=32, unique=True)
    ic_ativo = models.BooleanField()
    cnpj = models.IntegerField(unique=True)
    telefone = models.IntegerField()
    cep = models.IntegerField()
    nu_municipio = models.IntegerField()
    co_esfera = models.CharField(max_length=32, unique=True)
    de_endereco = models.CharField(max_length=128, unique=True)

class Cargo(models.Model):
    nu_cargo = models.IntegerField()
    no_cargo = models.CharField(max_length=32, unique=True)
    ic_ativo = models.BooleanField()

class Responsavel(models.Model):
    nu_responsavel = models.IntegerField()
    no_responsavel = models.CharField(max_length=32, unique=True)
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    co_matricula = models.CharField(max_length=32, unique=True)
    ic_ativo = models.BooleanField()

    class Meta:
        verbose_name_plural = "responsaveis"
