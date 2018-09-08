from django import forms
from common.forms import BaseForm, BaseFormControl
from core.models import Cargo, Entidade, Funcao, Responsavel, Usuario, Bolsista, Documento, Projeto, EmprestimoEquipamento, ProjetoDenominacao, ProjetoInteressados, ProjetoMetas, ProjetoAnexos, ProjetoBolsista
from django.conf import settings
from utils.models import get_fields, get_clean_fields

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


class ProjetoForm(BaseForm):
    preview = ['no_projeto', 'sg_projeto']
    class Meta:
        model = Projeto
        fields = get_fields(model)

class ProjetoFormEdit(BaseForm):
    preview = get_clean_fields(Projeto)
    fk_entidade_proponente = forms.ModelChoiceField(queryset=Entidade.objects.values_list('no_entidade',flat=True),
                                                    widget=forms.Select(attrs={'class':'form-control'}),
                                                    to_field_name="no_entidade")

    fk_entidade_concedente = forms.ModelChoiceField(queryset=Entidade.objects.values_list('no_entidade',flat=True),
                                                    widget=forms.Select(attrs={'class':'form-control'}),
                                                    to_field_name="no_entidade")

    fk_responsavel_proponente = forms.ModelChoiceField(queryset=Responsavel.objects.values_list('no_responsavel',flat=True),
                                                    widget=forms.Select(attrs={'class':'form-control'}),
                                                    to_field_name="no_responsavel")

    fk_responsavel_concedente = forms.ModelChoiceField(queryset=Responsavel.objects.values_list('no_responsavel',flat=True),
                                                    widget=forms.Select(attrs={'class':'form-control'}),
                                                    to_field_name="no_responsavel")

    fk_bolsita = forms.ModelChoiceField(queryset=Bolsista.objects.values_list('no_bolsista',flat=True),
                                                    widget=forms.Select(attrs={'class':'form-control'}),
                                                    to_field_name="no_bolsista")

    fk_funcao = forms.ModelChoiceField(queryset=Funcao.objects.values_list('no_funcao',flat=True),
                                                    widget=forms.Select(attrs={'class':'form-control'}),
                                                    to_field_name="no_funcao")

    class Meta:
        model = Projeto
        fields = get_fields(model)

class ProjetoDenominacaoForm(BaseFormControl):
    preview = get_clean_fields(ProjetoDenominacao)
    class Meta:
        model = ProjetoDenominacao
        fields = get_fields(model)

class ProjetoInteressadosForm(BaseFormControl):
    preview = get_clean_fields(ProjetoInteressados)
    class Meta:
        model = ProjetoInteressados
        fields = get_fields(model)

class ProjetoMetasForm(BaseFormControl):
    preview = get_clean_fields(ProjetoMetas)
    class Meta:
        model = ProjetoMetas
        fields = get_fields(model)

class ProjetoAnexosForm(BaseFormControl):
    preview = get_clean_fields(ProjetoAnexos)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = ProjetoAnexos
        fields = get_fields(model)

class ProjetoBolsistaForm(BaseFormControl):
    preview = get_clean_fields(ProjetoBolsista)
    class Meta:
        model = ProjetoBolsista
        fields = get_fields(model)
