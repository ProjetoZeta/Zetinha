from django import forms
from common.forms import BaseForm
from core.models import Cargo, Entidade, Funcao, Responsavel, Usuario

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
