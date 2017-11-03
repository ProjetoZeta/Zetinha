from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from .models import Cargo, Entidade, Funcao, Responsavel, Usuario

class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'no_completo', 'ic_ativo', 'ic_bolsista']

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = [f.name for f in Cargo._meta.get_fields()]

class FuncaoForm(ModelForm):
    class Meta:
        model = Funcao
        fields = [f.name for f in Funcao._meta.get_fields()]

class EntidadeForm(ModelForm):
    class Meta:
        model = Entidade
        fields = [f.name for f in Entidade._meta.get_fields()]

class ResponsavelForm(ModelForm):
    class Meta:
        model = Responsavel
        fields = [f.name for f in Responsavel._meta.get_fields()]
