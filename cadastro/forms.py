from django import forms
from common.forms import BaseForm, BaseFormControl
from .models import Cargo, Entidade, Funcao, Responsavel, Usuario, Bolsista, Documento, EmprestimoEquipamento, Projeto
from django.conf import settings
from utils.models import get_fields, get_clean_fields

from django.contrib.auth.forms import UserChangeForm

class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario

class UsuarioForm(BaseForm):
    preview = ['email', 'no_completo', 'ic_ativo', 'ic_bolsista']
    class Meta:
        model = Usuario
        fields = ['email', 'no_completo', 'ic_ativo', 'ic_bolsista']

class CargoForm(BaseForm):
    preview = get_clean_fields(Cargo)
    class Meta:
        model = Cargo
        fields = get_fields(model)

class FuncaoForm(BaseForm):
    preview = ['no_funcao','ic_ativo']
    class Meta:
        model = Funcao
        fields = get_fields(model)

class EntidadeForm(BaseForm):
    preview = ['no_entidade', 'ic_ativo', 'cnpj', 'nu_municipio']
    class Meta:
        model = Entidade
        fields = get_fields(model)

class ResponsavelForm(BaseForm):
    preview = ['no_responsavel', 'ic_ativo', 'co_matricula']
    class Meta:
        model = Responsavel
        fields = get_fields(model)

class BolsistaForm(BaseFormControl):

    preview = ['no_bolsista', 'email', 'cpf', 'celular', 'ic_ativo']

    def is_valid(self):

        #parent built-in is_valid() method
        valid = super(BolsistaForm, self).is_valid()

        if self.cleaned_data['tipo_conta'] == '1' and self.cleaned_data['banco'] != '104':
            self._errors['poupanca_sem_caixa'] = '{} disponível somente para o banco {}'.format(dict(Bolsista.TIPO_CONTA).get('1'), dict(Bolsista.COD_BANCO).get('104'))
            return False

        return valid

    class Meta:
        model = Bolsista
        fields = get_fields(model)

class DocumentoForm(BaseForm):
    preview = get_clean_fields(Documento)
    class Meta:
        model = Documento
        fields = ['bolsista', 'tipo_documento', 'no_documento', 'arquivo']

class EmprestimoEquipamentoForm(BaseForm):
    preview = get_clean_fields(EmprestimoEquipamento)
    class Meta:
        model = EmprestimoEquipamento
        fields = get_fields(model, ignore=['dt_emprestimo'])

class ProjetoForm(BaseFormControl):
    preview = ['nome', 'sigla']
    #file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Projeto
        fields = ['nome', 'sigla']
