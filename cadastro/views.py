from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django import forms

from .models import Emprego as EmpregoModel, Responsabilidade as ResponsabilidadeModel, Responsavel as ResponsavelModel, Entidade as EntidadeModel, Usuario as UsuarioModel, Bolsista as BolsistaModel, Documento as DocumentoModel, EmprestimoEquipamento as EmprestimoEquipamentoModel, Projeto as ProjetoModel, Participante as ParticipanteModel, Meta as MetaModel, Atividade as AtividadeModel, Anexo as AnexoModel
from .forms import EntidadeForm, ResponsavelForm, UsuarioForm, BolsistaForm, DocumentoForm, ProjetoForm, EmprestimoEquipamentoForm, ParticipanteProjetoForm, ParticipanteBolsistaForm, MetaForm, AtividadeForm, AnexoForm, AtividadeSelect, AtividadeBolsistaSelect, ResponsabilidadeForm
from django.views.generic import View

from django.http import HttpResponse

from .abstract_views import GenericView, FormView, MainView, ModalListView, MainViewStaticAliases, ModalListViewStaticAliases

class Responsavel(MainView):

    model = ResponsavelModel
    template_name = 'cadastro/responsavel.html'

    success_redirect = 'responsavel-editar'
    delete_redirect = 'responsavel'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Manter Responsáveis',
        }

class ResponsavelList(MainViewStaticAliases):

    model = ResponsavelModel
    template_name = 'cadastro/crud-nomodal.html'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Responsáveis',
            'createurl': 'responsavel-criar',
        }

class Responsabilidade(ModalListView):

    url_triggers = ['^responsabilidade.*$']
    model = ResponsabilidadeModel

    success_redirect = 'entidade-editar'
    delete_redirect = 'entidade-editar'

class Entidade(MainView):

    children = [Responsabilidade]
    model = EntidadeModel

    success_redirect = 'entidade-editar'
    delete_redirect = 'entidade'
    template_name = 'cadastro/entidade.html'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Entidade',
            'createurl': 'responsavel-criar',
        }

class EntidadeList(MainViewStaticAliases):

    model = EntidadeModel
    template_name = 'cadastro/crud-nomodal.html'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Órgão/Instituição',
            'createurl': 'entidade-criar',
        }

class Usuario(ModalListViewStaticAliases):

    template_name = 'cadastro/crud-withmodal.html'

    model = UsuarioModel

    success_redirect = 'usuario'
    delete_redirect = 'usuario'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Manter Usuários',
        }

class Emprego(ModalListViewStaticAliases):

    template_name = 'cadastro/crud-withmodal.html'

    model = EmpregoModel

    success_redirect = 'emprego'
    delete_redirect = 'emprego'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Manter Funções/Cargos',
        }

class ProjetoList(MainViewStaticAliases):

    model = ProjetoModel
    template_name = 'cadastro/crud-nomodal.html'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Projetos',
            'createurl': 'projeto-criar',
        }

class ParticipanteProjeto(MainView):

    model = ParticipanteModel
    form = ParticipanteProjetoForm

    url_triggers = ['^participante-proj-.*$', 'participante-remover']

    formalias = 'formp'
    setalias = 'datap'
    pkalias = 'pkparticipante'

    success_redirect = 'participante-proj-editar'
    delete_redirect = 'participante-proj-criar'

class AnexoProjeto(ModalListView):

    model = AnexoModel

    url_triggers = ['^anexo-proj-.*$']

    formalias = 'formfp'
    setalias = 'attachments'

    success_redirect = 'anexo-proj-upload'
    delete_redirect = 'anexo-proj-upload'


class AtividadeProjeto(ModalListView):

    model = AtividadeModel

    url_triggers = ['^atividade-meta-proj-.*$']

    formalias = 'forma'
    setalias = 'atividades'

    success_redirect = 'meta-proj-editar'
    delete_redirect = 'meta-proj-editar'


class MetaProjeto(MainView):

    model = MetaModel

    children = [AtividadeProjeto]

    url_triggers = ['^meta-proj-.*$']

    formalias = 'formm'
    setalias = 'metas'

    success_redirect = 'meta-proj-editar'
    delete_redirect = 'meta-proj-criar'

    template_name = 'cadastro/projeto.html'


class Projeto(MainViewStaticAliases):

    children = [ParticipanteProjeto, AnexoProjeto, MetaProjeto]

    model = ProjetoModel

    success_redirect = 'projeto-editar'
    delete_redirect = 'projeto'

    template_name = 'cadastro/projeto.html'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Manter Projeto'
        }

class BolsistaList(MainViewStaticAliases):

    model = BolsistaModel
    template_name = 'cadastro/crud-nomodal.html'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Bolsistas',
            'createurl': 'bolsista-criar',
        }


class Bolsista(FormView):

    template_name = 'cadastro/bolsista.html'

    def post(self, request, **kwargs):

        pk = kwargs.get(self.pk_alias, None)

        bolsista = self.model.objects.get(pk=pk) if pk else None

        participantes = ParticipanteModel.objects.filter(bolsista=bolsista, ic_ativo=True) if pk else None

        last_participante = participantes.latest('id') if participantes else None

        formp = ParticipanteBolsistaForm(request.POST,instance=last_participante)
        form = self.form(request.POST, instance=(bolsista if bolsista else None))

        if form.is_valid():
            b = form.save()
            datap = formp.data.copy()
            datap['bolsista'] = b.pk
            formp.data = datap
            if formp.is_valid():
                formp.save()
                return redirect(*('bolsista-editar', b.pk,))
            else:
                print(formp.errors)
                return self.get(request=request, form=form, formp=formp, pk=b.pk)
        else:
            return self.get(request=request, form=form, formp=formp, **kwargs)

    def template_keys(self, **kwargs):

        pk = kwargs.get('pk', None)

        bolsista = BolsistaModel.objects.get(pk=pk) if pk else None

        documento_form = DocumentoForm(initial={'bolsista': bolsista}) if pk else DocumentoForm()
        documento_form.fields['bolsista'].widget = forms.HiddenInput() if pk else documento_form.fields['bolsista'].widget

        emprestimo_form = EmprestimoEquipamentoForm(initial={'bolsista': bolsista}) if pk else EmprestimoEquipamentoForm()
        emprestimo_form.fields['bolsista'].widget = forms.HiddenInput() if pk else documento_form.fields['bolsista'].widget

        participantes = ParticipanteModel.objects.filter(bolsista=bolsista, ic_ativo=True) if pk else None

        last_participante = participantes.latest('id') if participantes else None

        formp = kwargs.get('formp', None)

        if formp is None:
            formp = ParticipanteBolsistaForm(initial=({'bolsista': bolsista} if pk else None), instance=last_participante)

        return {
            **super().template_keys(**kwargs),
            'content_title': 'Cadastrar Bolsistas / Pequisadores',
            'formf': documento_form,
            'forme': emprestimo_form,
            'formp': formp,
            'documents': DocumentoModel.objects.filter(bolsista=bolsista if pk else None),
            'emprestimos': EmprestimoEquipamentoModel.objects.filter(bolsista=bolsista if pk else None),
            'pk': pk
        }

class BolsistaMedia(Bolsista):

    def post(self, request, **kwargs):
        bolsista = BolsistaModel.objects.get(pk=request.POST.get('bolsista', None))
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(*('bolsista-editar', bolsista.pk,))
        else:
            #form = BolsistaForm(instance=BolsistaModel.objects.get(pk=bolsista.pk)) if bolsista.pk else BolsistaForm()
            return self.get(request=request, form=form)

    def delete(self, request, **kwargs):
        item = self.model.objects.get(pk=kwargs.get('pkdelete', None))
        bolsista = item.bolsista
        if item:
            item.delete()
        return redirect(*('bolsista-editar', bolsista.pk,))


class BolsistaDocumento(BolsistaMedia):

    model = DocumentoModel

class BolsistaEmprestimoEquipamento(BolsistaMedia):

    model = EmprestimoEquipamentoModel

class Documento(GenericView):

    template_name = 'cadastro/file-viewer.html'

    def template_keys(self, **kwargs):
        return {
            **super().template_keys(**kwargs),
            'content_title': 'Preview de arquivo',
            'document': DocumentoModel.objects.get(pk=kwargs.get('pk', None))
        }

class EmprestimoEquipamento(GenericView):

    template_name = 'cadastro/emprestimo-viewer.html'

    def template_keys(self, **kwargs):
        return {
            **super().template_keys(**kwargs),
            'content_title': 'Empréstimo de Equipamento',
            'emprestimo': EmprestimoEquipamentoModel.objects.get(pk=kwargs.get('pk', None))
        }

def get_atividades(self, pk):
    form = AtividadeSelect(pkmeta=pk)
    return HttpResponse(form)

def get_atividade_bolsistas(self, pk):
    atividade = AtividadeModel.objects.get(pk=pk)
    form = AtividadeBolsistaSelect(pkprojeto=atividade.meta.projeto.pk, instance=AtividadeModel.objects.get(pk=pk))
    return HttpResponse(form)

        
        
