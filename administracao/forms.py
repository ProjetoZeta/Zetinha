from django import forms
from common.forms import BaseForm
from core.models import Cargo, Entidade, Funcao, Responsavel, Usuario, Bolsista
from django.conf import settings

class UsuarioForm(BaseForm):
    preview = ['email', 'no_completo', 'ic_ativo', 'ic_bolsista']
    class Meta:
        model = Usuario
        fields = ['email', 'no_completo', 'ic_ativo', 'ic_bolsista']

class CargoForm(BaseForm):
    preview = [f.name for f in Cargo._meta.get_fields()]
    class Meta:
        model = Cargo
        fields = [f.name for f in Cargo._meta.get_fields()]

class FuncaoForm(BaseForm):
    preview = [f.name for f in Funcao._meta.get_fields()]
    class Meta:
        model = Funcao
        fields = [f.name for f in Funcao._meta.get_fields()]

class EntidadeForm(BaseForm):
    preview = ['no_entidade', 'ic_ativo', 'cnpj', 'nu_municipio']
    class Meta:
        model = Entidade
        fields = [f.name for f in Entidade._meta.get_fields()]

class ResponsavelForm(BaseForm):
    preview = [f.name for f in Responsavel._meta.get_fields()]
    class Meta:
        model = Responsavel
        fields = [f.name for f in Responsavel._meta.get_fields()]

class BolsistaForm(BaseForm):
    DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')
    dt_nascimento = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    preview = ['no_bolsista', 'email', 'cpf', 'telefone', 'ic_ativo']
    class Meta:
        model = Bolsista
        fields = [f.name for f in Bolsista._meta.get_fields()]

