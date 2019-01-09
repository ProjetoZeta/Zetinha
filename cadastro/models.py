from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings
from .validators import cpf, cnpj, lattes_url


class Usuario(AbstractUser):
    no_completo = models.CharField('Nome completo', max_length=64, unique=True)
    ic_bolsista = models.BooleanField('Bolsista', default=True)
    email = models.EmailField('Email', unique=True)
    username = models.CharField('Nome de Usuário', max_length=64, unique=True)

    class Meta:
        verbose_name = "Usuário"

class Responsavel(models.Model):
    nome = models.CharField('Nome', max_length=32)
    email = models.EmailField('Email', unique=True)
    cpf = models.CharField('CPF', max_length=14, unique=True, validators=[cpf])
    data_nascimento = models.DateField('Data de Nascimento')
    rg = models.CharField('RG', max_length=16)
    orgao_expedidor = models.CharField('Órgão Expedidor', max_length=32)
    telefone = models.CharField('Telefone', max_length=32, blank=True)
    celular = models.CharField('Celular', max_length=32, blank=True)
    matricula = models.CharField('Matrícula', max_length=32, unique=True, blank=True)
    ic_ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name_plural = "Responsáveis"
        verbose_name = "Responsável"

    def __str__(self):
        return self.nome



class Bolsista(models.Model):

    VINCULO_UNB = (
        ('1', 'Professor'),
        ('2', 'Pesquisador'),
        ('3', 'Técnico'),
        ('4', 'Estudante'),
        ('5', 'Nenhum')
    )

    OUTROS_VINCULOS = (
        ('1', 'Pesquisador ICT'),
        ('2', 'Profissionais extensão TEC/PI/TT'),
        ('3', 'Prof. ensino fundamental e médio da rede pública'),
        ('4', 'Nenhum')
    )

    VINCULO_OUTRA_IES = (
        ('1', 'Professor'),
        ('2', 'Estudante'),
        ('3', 'Nenhum')
    )   

    TIPO_CONTA = (
        ('1', 'Conta-poupança'),
        ('2', 'Conta-corrente')
    )

    COD_BANCO = (
        ('001', '001 - BANCO DO BRASIL S/A'),
        ('002', '002 - BANCO CENTRAL DO BRASIL'),
        ('003', '003 - BANCO DA AMAZONIA S.A'),
        ('004', '004 - BANCO DO NORDESTE DO BRASIL S.A'),
        ('070', '070 - BANCO DE BRASILIA S.A'),
        ('104', '104 - CAIXA ECONOMICA FEDERAL'),
        ('237', '237 - BANCO BRADESCO S.A'),
        ('275', '275 - BANCO REAL S.A'),
        ('341', '341 - BANCO ITAU S.A'),
        ('409', '409 - UNIBANCO - UNIAO DOS BANCOS BRASILEIROS'),
        ('422', '422 - BANCO SAFRA S.A'),
        ('477', '477 - CITIBANK N.A'),
        ('502', '502 - BANCO SANTANDER S.A')

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

    vinculo_unb = models.CharField('Vínculo UnB', max_length=1, choices=VINCULO_UNB, default='4')
    vinculo_outros = models.CharField('Outros Vínculos', max_length=1, choices=OUTROS_VINCULOS, default='4')
    vinculo_ies = models.CharField('Vínculo outras IES', max_length=1, choices=VINCULO_OUTRA_IES, default='3')

    no_bolsista = models.CharField('Nome', max_length=32)
    email = models.EmailField('Email', unique=True)
    cpf = models.CharField('CPF', max_length=14, unique=True, validators=[cpf])
    dt_nascimento = models.DateField('Data de Nascimento')
    rg = models.CharField('RG', max_length=32)
    orgao_expedidor = models.CharField('Órgão Expedidor', max_length=32)
    telefone = models.CharField('Telefone', max_length=32, blank=True)
    celular = models.CharField('Celular', max_length=32, blank=True)
    matricula = models.CharField('Matrícula', max_length=32, unique=True, blank=True)
    ic_ativo = models.BooleanField('Ativo', default=True)

    pis_nit = models.CharField('PIS ou NIT', max_length=32, blank=True)
    link_lattes = models.CharField('Lattes', max_length=128, unique=True, validators=[lattes_url])

    endereco = models.CharField('Endereço', max_length=128)
    cidade = models.CharField('Cidade', max_length=32)
    cep = models.CharField('CEP', max_length=32)
    uf = models.CharField('UF', max_length=2, choices=UFS, default='DF')

    banco = models.CharField('Banco', max_length=128, choices=COD_BANCO, default='001')
    agencia = models.CharField('Agência', max_length=32)
    tipo_conta = models.CharField('Tipo de Conta', max_length=1, choices=TIPO_CONTA, default='2')
    conta = models.CharField('Conta', max_length=32)

    email_unb = models.EmailField('Email UnB', blank=True)
    telefone_local = models.CharField('Telefone Local', max_length=32, blank=True)

    class Meta:
        verbose_name_plural = "Bolsistas"
        verbose_name = "Bolsista"

    def __str__(self):
        return self.no_bolsista

class Entidade(models.Model):

    ESFERA_ADMINISTRATIVA = (
        ('1', 'Público Federal'),
        ('2', 'Público Estadual'),
        ('3', 'Público Municipal'),
        ('4', 'Privado com fins lucrativos'),
        ('5', 'Privado sem fins lucrativos'),
    )

    nome = models.CharField('Nome Órgão/Entidade', max_length=128)
    email = models.CharField('Email', max_length=64)
    cnpj = models.CharField('CNPJ', max_length=64,validators=[cnpj], unique=True)
    endereco = models.CharField('Endereço', max_length=256, unique=True)
    cidade = models.CharField('Cidade', max_length=64)
    cep = models.CharField('CEP', max_length=16)
    uf = models.CharField('UF', max_length=2, choices=Bolsista.UFS, default='DF')
    telefone = models.CharField('Telefone', max_length=16)
    esfera_administrativa = models.CharField('Esfera', choices=ESFERA_ADMINISTRATIVA, default='1', max_length=1)
    ic_ativo = models.BooleanField('Ativo', default=True)

    banco = models.CharField('Banco', max_length=128, choices=Bolsista.COD_BANCO, default='001', blank=True)
    agencia = models.CharField('Agência', max_length=32, blank=True)
    tipo_conta = models.CharField('Tipo de Conta', max_length=1, choices=Bolsista.TIPO_CONTA, default='2', blank=True)
    conta = models.CharField('Conta', max_length=32, blank=True)
    praca_pagamento = models.CharField('Praça de Pagamento', max_length=128, blank=True)

    def __str__(self):
        return "{}".format(self.nome)


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

class EmprestimoEquipamento(models.Model):
    TIPOS = (
        ('1', 'Computador'),
        ('2', 'Projetor'),
        ('2', 'Microcontrolador'),
        ('4', 'Equipamento de Rede'),
        ('5', 'Outro'),
    )
    bolsista = models.ForeignKey('Bolsista', on_delete=models.CASCADE)
    tipo_equipamento = models.CharField('Tipo de Equipamento', max_length=1, choices=TIPOS, default='1')
    descricao_equipamento = models.CharField('Descrição do Equipamento', max_length=512)
    nu_serie = models.CharField('Número de Série', max_length=64)
    nu_patrimonio = models.CharField('Número de Patrimônio', max_length=64)
    dt_emprestimo = models.DateTimeField('Momento do Registro', default=datetime.now, blank=True)
    foto = models.FileField()

    @property
    def filename(self):
        return self.foto.name.replace(settings.MEDIA_URL, '')

    def __str__(self):
        return dict(EmprestimoEquipamento.TIPOS).get(self.tipo_equipamento)

class Projeto(models.Model):
    nome = models.CharField('Nome do Projeto', max_length=256)
    sigla = models.CharField('Sigla', max_length=256, unique=True)

    inicio_vigencia = models.DateField('Início da Vigência', null=True, blank=True)
    termino_vigencia = models.DateField('Término da Vigência', null=True, blank=True)

    duracao = models.CharField('Duração', max_length=256, null=True, blank=True)
    identificacao_objeto = models.CharField('Identificação do Objeto', max_length=12288, null=True, blank=True)
    justificativa_proposta = models.CharField('Justificativa da Proposta', max_length=12288, null=True, blank=True)
    referencias_bibliograficas = models.CharField('Referências Bibliográficas', max_length=12288, null=True, blank=True)
    
    metodologia = models.CharField('Metodologia', max_length=12288, null=True, blank=True)
    gestao_transferencia_tecnologia = models.CharField('Gestão de Projeto e Transferência de Tecnologia', max_length=12288, null=True, blank=True)

    entidade_concedente = models.ForeignKey('Entidade', on_delete=models.CASCADE, related_name='entidadeconcedente', null=True, blank=True)
    entidade_proponente = models.ForeignKey('Entidade', on_delete=models.CASCADE ,related_name='entidadeproponente', null=True, blank=True)

    responsavel_concedente = models.ForeignKey('Responsavel', on_delete=models.CASCADE, related_name='rconcedente', null=True, blank=True)
    responsavel_proponente = models.ForeignKey('Responsavel', on_delete=models.CASCADE, related_name='rproponente', null=True, blank=True)

    responsavel_tecnico_concedente = models.ForeignKey('Responsavel', on_delete=models.CASCADE, related_name='rtconcedente', null=True, blank=True)
    responsavel_tecnico_proponente = models.ForeignKey('Responsavel', on_delete=models.CASCADE, related_name='rtproponente', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Projetos"
        verbose_name = "Projeto"
    def __str__(self):
        return "{} - {}".format(self.sigla, self.nome)


class Participante(models.Model):
    bolsista = models.ForeignKey('Bolsista', on_delete=models.CASCADE, verbose_name="Bolsista")
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, verbose_name="Projeto")
    funcao = models.ForeignKey('Emprego', on_delete=models.CASCADE, verbose_name="Função")
    ic_ativo = models.BooleanField('Ativo', default=True)

    CATEGORIA = (
        ('1', 'Bolsa de aux. ao estudante'),
        ('2', 'Bolsa de aux. ao pesquisador '),
    )

    MODALIDADE = (
        ('01', 'Pesquisador Senior'),
        ('02', 'Pesquisador'),
        ('03', 'Pesquisa, Desenvol. E Inovação(PDI)'),
        ('04', 'Apoio Técnico à Pesquisa, Desenv. E Inovação'),
        ('05', 'Apoio Operacional à Pesquisa, Desenv. E Inovação(PDI)'),
        ('06', 'Pós-Doutorado'),
        ('07', 'Doutorado'),
        ('08', 'Mestrado'),
        ('09', 'Graduação'),
        ('10', 'Nível Médio'),
        ('11', 'Extensão')
    )

    NIVEL = (
        ('1', 'A'),
        ('2', 'B'),
        ('2', 'C'),
        ('4', 'D')
    )

    categoria = models.CharField('Categoria', max_length=1, choices=CATEGORIA, default='1')
    modalidade = models.CharField('Modalidade', max_length=2, choices=MODALIDADE, default='09')
    nivel = models.CharField('Nível', max_length=1, choices=NIVEL, default='1')

    inicio_vigencia = models.DateField('Início da Vigência')
    termino_vigencia = models.DateField('Término da Vigência')
    periodo_total = models.IntegerField('Período Total')
    horas_semanais = models.IntegerField('Horas semanais')
    valor_mensal = models.DecimalField('Valor mensal', max_digits=10, decimal_places=2)
    valor_total = models.DecimalField('Valor total', max_digits=10, decimal_places=2)

    def __str__(self):
        return "{}".format(self.bolsista.no_bolsista)

class Meta(models.Model):
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, verbose_name="Projeto")
    titulo = models.CharField('Título', max_length=100)
    descricao = models.CharField('Descrição', max_length=1024)
    ic_ativo = models.BooleanField('Ativo', default=True)
    posicao = models.IntegerField('Índice', null=True, blank=True)

    def __str__(self):
        return "{}".format(self.titulo)

class Atividade(models.Model):
    meta = models.ForeignKey('Meta', on_delete=models.CASCADE, verbose_name="Meta")
    titulo = models.CharField('Título', max_length=100)
    descricao = models.CharField('Descrição', max_length=1024)
    data_inicio = models.DateField('Data de Início')
    data_fim = models.DateField('Data de Fim')
    ic_ativo = models.BooleanField('Ativo', default=True)
    participantes = models.ManyToManyField(Participante)
    posicao = models.IntegerField('Índice', null=True, blank=True)

    def __str__(self):
        return "{}".format(self.titulo)


class Anexo(models.Model):
    
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE)
    arquivo = models.FileField()

    @property
    def filename(self):
        return self.arquivo.name.replace(settings.MEDIA_URL, '')

    def __str__(self):
        return self.arquivo.name.replace(settings.MEDIA_URL, '')

class Emprego(models.Model):
    FUNCAO = '1'
    CARGO = '2'
    TIPOS = (
        (FUNCAO, 'Função'),
        (CARGO, 'Cargo')
    )
    nome = models.CharField('Nome', max_length=100)
    tipo = models.CharField('Tipo', choices=TIPOS, max_length=1)

    class Meta:
        verbose_name_plural = "Funções ou Cargos"
        verbose_name = "Função ou Cargo"

    def __str__(self):
        return self.nome

class Responsabilidade(models.Model):
    entidade = models.ForeignKey('Entidade', on_delete=models.CASCADE, verbose_name="Entidade", null=True)
    responsavel = models.ForeignKey('Responsavel', on_delete=models.CASCADE, verbose_name="Responsável", null=True)
    cargo = models.ForeignKey('Emprego', on_delete=models.CASCADE, verbose_name="Cargo", null=True)
    ic_ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return "{} como {}".format(self.responsavel, self.cargo)



