from django import forms
from django.forms import ModelForm
from .models import Cargo, Entidade, Funcao, Responsavel

class UserForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()
    bolsista = forms.BooleanField()
    ativo = forms.BooleanField()

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
