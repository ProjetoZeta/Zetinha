from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings
from common.validators import cpf, lattes_url

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

class Bolsista(models.Model):
    TIPOS_VINCULOS = (
        ('1', 'Servidor Público - Professor'),
        ('2', 'Servidor Público ou Empregado Público'),
        ('3', 'Colaborador sem vínculo com o serviço')
    )

    TIPO_CONTA = (
        ('1', 'Conta-salário'),
        ('2', 'Conta-poupança'),
        ('3', 'Conta-corrente')
    )

    UFS = (
        ('AC', 'AC - Acre'),
        ('AL', 'AL - Alagoas'),
        ('AP', 'AP - Amapá'),
        ('AM', 'AM - Amazonas'),
        ('BA', 'BA - Bahia'),
        ('CE', 'CE - Ceará'),
        ('DF', 'DF - Distrito Federal'),
        ('ES', 'ES - Espírito Santo'),
        ('GO', 'GO - Goiás'),
        ('MA', 'MA - Maranhão'),
        ('MT', 'MT - Mato Grosso'),
        ('MS', 'MS - Mato Grosso do Sul'),
        ('MG', 'MG - Minas Gerais'),
        ('PA', 'PA - Pará'),
        ('PB', 'PB - Paraíba'),
        ('PR', 'PR - Paraná'),
        ('PE', 'PE - Pernambuco'),
        ('PI', 'PI - Piauí'),
        ('RJ', 'RJ - Rio de Janeiro'),
        ('RN', 'RN - Rio Grande do Norte'),
        ('RS', 'RS - Rio Grande do Sul'),
        ('RO', 'RO - Rondônia'),
        ('RR', 'RR - Roraima'),
        ('SC', 'SC - Santa Catarina'),
        ('SP', 'SP - São Paulo'),
        ('SE', 'SE - Sergipe'),
        ('TO', 'TO - Tocantins')
    )

    tipo_vinculo = models.CharField('Tipo de Vínculo', max_length=1, choices=TIPOS_VINCULOS, default='1')

    no_bolsista = models.CharField('Nome', max_length=32, unique=True)
    email = models.EmailField('Email', unique=True)
    cpf = models.CharField('Nome', max_length=11, unique=True, validators=[cpf])
    dt_nascimento = models.DateField('Data de Nascimento')
    rg = models.CharField('RG', max_length=32, unique=True)
    orgao_expedidor = models.CharField('Órgão Expedidor', max_length=32)
    telefone = models.CharField('Telefone', max_length=32, blank=True)
    celular = models.CharField('Celular', max_length=32, blank=True)
    matricula = models.CharField('Matrícula', max_length=32, unique=True, blank=True)
    ic_ativo = models.BooleanField('Ativo')

    pis_nit = models.CharField('PIS ou NIT', max_length=32)
    link_lattes = models.CharField('Lattes', max_length=128, unique=True, validators=[lattes_url])

    endereco = models.CharField('Endereço', max_length=32)
    cidade = models.CharField('Cidade', max_length=32)
    cep = models.CharField('CEP', max_length=32, unique=True)
    uf = models.CharField('UF', max_length=2, choices=UFS, default='1')

    banco = models.CharField('Banco', max_length=32)
    agencia = models.CharField('Agência', max_length=32)
    tipo_conta = models.CharField('Tipo de Conta', max_length=1, choices=TIPO_CONTA, default='1')
    conta = models.CharField('Conta', max_length=32)

    email_unb = models.EmailField('Email UnB', unique=True, blank=True)
    telefone_local = models.CharField('Telefone Local', max_length=32, blank=True)

    def __str__(self):
        return self.no_bolsista

class Documento(models.Model):
    TIPOS = (
        ('1', 'Fotografia'),
        ('2', 'Declaração'),
        ('3', 'Documento pessoal'),
        ('4', 'Certificado'),
    )
    bolsista = models.ForeignKey('Bolsista', on_delete=models.CASCADE)
    tipo_documento = models.CharField('Tipo de Documento', max_length=1, choices=TIPOS, default='3')
    no_documento = models.CharField('Descrição', max_length=512)
    dt_cadastro = models.DateTimeField('Momento do Upload', default=datetime.now, blank=True)
    arquivo = models.FileField()

    @property
    def filename(self):
        return self.arquivo.name.replace(settings.MEDIA_URL, '')

    def __str__(self):
        return self.tipo_documento

