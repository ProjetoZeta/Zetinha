from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django import forms

from .models import Cargo as CargoModel, Entidade as EntidadeModel, Funcao as FuncaoModel, Usuario as  UsuarioModel, Bolsista as BolsistaModel, Documento as DocumentoModel, EmprestimoEquipamento as EmprestimoEquipamentoModel, Projeto as ProjetoModel
from .forms import CargoForm, EntidadeForm, FuncaoForm, ResponsavelForm, UsuarioForm, BolsistaForm, DocumentoForm, ProjetoForm, EmprestimoEquipamentoForm
from django.views.generic import View

from django.http import HttpResponse

from .abstract_views import GenericView, FormView

class Cargo(FormView):
    template_name = 'cadastro/crud-withmodal.html'

class Funcao(FormView):
    template_name = 'cadastro/crud-withmodal.html'

class Entidade(FormView):
    template_name = 'cadastro/crud-withmodal.html'

class Responsavel(FormView):
    template_name = 'cadastro/crud-withmodal.html'

class Usuario(FormView):
    template_name = 'cadastro/crud-withmodal.html'

class Projeto(FormView):

    template_name = 'cadastro/projeto.html'

class ProjetoList(GenericView):
    
    model = ProjetoModel
    template_name = 'cadastro/crud-projeto.html'


class Bolsista(FormView):

    template_name = 'cadastro/bolsista.html'

    def get(self, request, **kwargs):

        pk = kwargs.get('pk', None)

        documento_form = DocumentoForm(initial={'bolsista': BolsistaModel.objects.get(pk=pk)}) if pk else DocumentoForm()
        documento_form.fields['bolsista'].widget = forms.HiddenInput() if pk else documento_form.fields['bolsista'].widget

        emprestimo_form = EmprestimoEquipamentoForm(initial={'bolsista': BolsistaModel.objects.get(pk=pk)}) if pk else EmprestimoEquipamentoForm()
        emprestimo_form.fields['bolsista'].widget = forms.HiddenInput() if pk else documento_form.fields['bolsista'].widget

        self.template_keys = {
            'content_title': 'Cadastrar Bolsistas / Pequisadores',
            'formf': documento_form,
            'forme': emprestimo_form,
            'documents': DocumentoModel.objects.filter(bolsista=BolsistaModel.objects.get(pk=pk) if pk else None),
            'emprestimos': EmprestimoEquipamentoModel.objects.filter(bolsista=BolsistaModel.objects.get(pk=pk) if pk else None),
            'projects': BolsistaModel.objects.get(pk=pk).projeto_atual if pk else None,
            'pk': pk
        }

        return super().get(request, **kwargs)

class BolsistaList(GenericView):

    def get(self, request, **kwargs):

        self.template_keys = {
            **self.template_keys,
            'content_title': 'Bolsistas',
            'data': self.model.objects.all(),
            'form': BolsistaForm()
        }

        return super().get(request, **kwargs)     

    model = BolsistaModel
    template_name = 'cadastro/crud-bolsista.html'


class BolsistaMedia(Bolsista):

    def post(self, request, **kwargs):
        bolsista = BolsistaModel.objects.get(pk=request.POST.get('bolsista', None))
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bolsista-editar', pk=bolsista.pk)
        else:
            #form = BolsistaForm(instance=BolsistaModel.objects.get(pk=bolsista.pk)) if bolsista.pk else BolsistaForm()
            return self.get(request=request, form=form)

class BolsistaDocumento(BolsistaMedia):

    model = DocumentoModel

class BolsistaEmprestimoEquipamento(BolsistaMedia):

    model = EmprestimoEquipamentoModel

class Documento(GenericView):

    template_name = 'cadastro/file-viewer.html'

    def get(self, request, **kwargs):

        self.template_keys = {
            **self.template_keys,
            'content_title': 'Preview de arquivo',
            'document': DocumentoModel.objects.get(pk=kwargs.get('pk', None))
        }

        return super().get(request, **kwargs)

class EmprestimoEquipamento(GenericView):

    template_name = 'cadastro/emprestimo-viewer.html'

    def get(self, request, **kwargs):

        self.template_keys = {
            **self.template_keys,
            'content_title': 'Empréstimo de Equipamento',
            'emprestimo': EmprestimoEquipamentoModel.objects.get(pk=kwargs.get('pk', None))
        }
        
        return super().get(request, **kwargs)

def projeto_handle(request, pk=None, pkdelete=None):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=ProjetoModel.objects.get(pk=pk)) if pk else ProjetoForm(request.POST)
        if form.is_valid() and form.save():
            return redirect('projeto')

    elif request.method == 'GET':
        form = ProjetoForm(instance=ProjetoModel.objects.get(pk=pk)) if pk else ProjetoForm()

    return fetch_projeto(request, form, pk)


def fetch_projeto(request, form,  pk):
    return render(request,'cadastro/projeto.html', {
                'content_title': 'Manter Projeto',
                'form': form,
                'pk': pk
                })

def projeto(request, pk=None, pkdelete=None):
    if pkdelete:
        item = ProjetoModel.objects.get(pk=pkdelete)
        if item:
            item.delete()
        return redirect('projeto')
    return render(request, 'cadastro/crud-projeto.html', {
        'data': ProjetoModel.objects.all(),
        'form': ProjetoForm(),
        'content_title': 'Projeto'
    })
