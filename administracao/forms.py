from django import forms
from django.forms import ModelForm
from .models import Cargo, Entidade, Funcao

class UserForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()
    bolsista = forms.BooleanField()
    ativo = forms.BooleanField()

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = ['no_cargo', 'ic_ativo']

class FuncaoForm(ModelForm):
    class Meta:
        model = Funcao
        fields = ['no_funcao', 'ic_ativo']

class EntidadeForm(ModelForm):
    class Meta:
        model = Entidade
        fields = ['co_entidade', 'no_entidade', 'sg_entidade', 'ic_ativo', 'cnpj', 'telefone', 'cep', 'nu_municipio', 'co_esfera', 'de_endereco']
