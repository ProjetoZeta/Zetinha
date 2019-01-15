from django import forms
from django.forms import Form
from cadastro.models import Projeto, Participante

from cadastro.forms import NewModelForm

class ParticipantesSelect(Form):
    def __init__(self, pkprojeto, **kwargs):
        super().__init__(**kwargs)
        projeto = Projeto.objects.get(pk=pkprojeto)
        self.fields['participantes'].queryset = Participante.objects.filter(projeto=projeto, ic_ativo=True)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['id'] = 'id_atividade_select'

    participantes = forms.ModelChoiceField(queryset=Participante.objects.all(), empty_label='Selecione um bolsista')

