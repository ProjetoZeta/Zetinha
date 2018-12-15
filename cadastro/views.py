from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django import forms

from .models import Emprego as EmpregoModel, Responsabilidade as ResponsabilidadeModel, Responsavel as ResponsavelModel, Entidade as EntidadeModel, Usuario as UsuarioModel, Bolsista as BolsistaModel, Documento as DocumentoModel, EmprestimoEquipamento as EmprestimoEquipamentoModel, Projeto as ProjetoModel, Participante as ParticipanteModel, Meta as MetaModel, Atividade as AtividadeModel, Anexo as AnexoModel
from .forms import EntidadeForm, ResponsavelForm, UsuarioForm, BolsistaForm, DocumentoForm, ProjetoForm, EmprestimoEquipamentoForm, ParticipanteProjetoForm, ParticipanteBolsistaForm, MetaForm, AtividadeForm, AnexoForm, AtividadeSelect, AtividadeBolsistaSelect, ResponsabilidadeForm, EmpregoForm, AtividadeParticipantesForm
from django.views.generic import View

from django.http import HttpResponse

from templates.views import MainView, ModalListView, MainViewStaticAliases, ModalListViewStaticAliases, RelatedFormView

from django.contrib import messages

class Responsavel(MainView):

    form = ResponsavelForm
    template_name = 'cadastro/responsavel.html'

    success_redirect = 'responsavel-editar'
    delete_redirect = 'responsavel'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Manter Responsáveis',
        }

class ResponsavelList(MainViewStaticAliases):

    form = ResponsavelForm
    template_name = 'cadastro/crud-nomodal.html'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Responsáveis',
            'createurl': 'responsavel-criar',
        }

class Responsabilidade(ModalListView):

    url_triggers = ['^responsabilidade.*$']
    form = ResponsabilidadeForm

    success_redirect = 'entidade-editar'
    delete_redirect = 'entidade-editar'

class Entidade(MainView):

    children = [Responsabilidade]
    form = EntidadeForm

    success_redirect = 'entidade-editar'
    delete_redirect = 'entidade'
    template_name = 'cadastro/entidade.html'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Entidade',
            'createurl': 'responsavel-criar',
        }

class EntidadeList(MainViewStaticAliases):

    form = EntidadeForm
    template_name = 'cadastro/crud-nomodal.html'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Órgão/Instituição',
            'createurl': 'entidade-criar',
        }

class Usuario(ModalListViewStaticAliases):

    template_name = 'cadastro/crud-withmodal.html'

    form = UsuarioForm

    success_redirect = 'usuario'
    delete_redirect = 'usuario'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Manter Usuários',
        }

class Emprego(ModalListViewStaticAliases):

    template_name = 'cadastro/crud-withmodal.html'

    form = EmpregoForm

    success_redirect = 'emprego'
    delete_redirect = 'emprego'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Manter Funções/Cargos',
        }

class ProjetoList(MainViewStaticAliases):

    form = ProjetoForm
    template_name = 'cadastro/crud-nomodal.html'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Projetos',
            'createurl': 'projeto-criar',
        }

class ParticipanteProjeto(MainView):

    form = ParticipanteProjetoForm

    url_triggers = ['^participante-proj-.*$', 'participante-remover']

    formalias = 'formp'
    setalias = 'datap'
    pkalias = 'pkparticipante'

    success_redirect = 'participante-proj-editar'
    delete_redirect = 'participante-proj-criar'

class AnexoProjeto(ModalListView):

    form = AnexoForm

    url_triggers = ['^anexo-proj-.*$']

    formalias = 'formfp'
    setalias = 'attachments'

    success_redirect = 'anexo-proj-upload'
    delete_redirect = 'anexo-proj-upload'


class AtividadeProjeto(ModalListView):

    form = AtividadeForm

    url_triggers = ['^atividade-meta-proj-.*$']

    formalias = 'forma'
    setalias = 'atividades'

    success_redirect = 'meta-proj-editar'
    delete_redirect = 'meta-proj-editar'

class AtividadeParticipantes(MainView):

    form = AtividadeParticipantesForm

    url_triggers = ['^vinculo-atividade-m-proj$']

    formalias = 'formv'
    setalias = 'atividadespormeta'

    success_redirect = 'vinculo-atividade-m-proj'

    def template_keys(self, *args, **kwargs):

        atividade = AtividadeModel.objects.get(pk=kwargs.get(self.pkalias)) if kwargs.get(self.pkalias) else None
        participantes = ParticipanteModel.objects.filter(projeto=atividade.meta.projeto if atividade else None).exclude(ic_ativo=False)

        return {
            'content_title': 'Manter Projeto',
            'participantes': participantes
        }


class MetaProjeto(MainView):

    form = MetaForm

    children = [AtividadeProjeto, AtividadeParticipantes]

    url_triggers = ['^meta-proj-.*$']

    formalias = 'formm'
    setalias = 'metas'

    success_redirect = 'meta-proj-editar'
    delete_redirect = 'meta-proj-criar'

    template_name = 'cadastro/projeto.html'

class Projeto(MainViewStaticAliases):

    children = [ParticipanteProjeto, AnexoProjeto, MetaProjeto]

    form = ProjetoForm

    success_redirect = 'projeto-editar'
    delete_redirect = 'projeto'

    template_name = 'cadastro/projeto.html'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Manter Projeto'
        }

class BolsistaList(MainViewStaticAliases):

    form = BolsistaForm
    template_name = 'cadastro/crud-nomodal.html'

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Bolsistas',
            'createurl': 'bolsista-criar',
        }

class Documento(ModalListView):

    form = DocumentoForm

    url_triggers = ['^.*arquivo-bolsista$']

    formalias = 'formf'
    setalias = 'documents'

    success_redirect = 'bolsista-editar'
    delete_redirect = 'bolsista-editar'

class EmprestimoEquipamento(ModalListView):

    form = EmprestimoEquipamentoForm

    url_triggers = ['^.*equipamento-bolsista$']

    formalias = 'forme'
    setalias = 'emprestimos'

    success_redirect = 'bolsista-editar'
    delete_redirect = 'bolsista-editar'


class ParticipanteBolsista(RelatedFormView):

    form = ParticipanteBolsistaForm

    formalias = 'formp'

class Bolsista(MainViewStaticAliases):

    children = [Documento, EmprestimoEquipamento]

    related = [ParticipanteBolsista]

    form = BolsistaForm

    template_name = 'cadastro/bolsista.html'

    success_redirect = 'bolsista-editar'
    delete_redirect = 'bolsista'

    def template_keys(self, *args, **kwargs):
        
        return {
            'content_title': 'Cadastrar Bolsistas / Pequisadores',
        }

class Documento(MainViewStaticAliases):

    template_name = 'cadastro/file-viewer.html'

    form = DocumentoForm

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Preview de arquivo',
            'document': self.model.objects.get(pk=kwargs.get('pk', None))
        }

class EmprestimoEquipamento(MainViewStaticAliases):

    template_name = 'cadastro/emprestimo-viewer.html'

    form = EmprestimoEquipamentoForm

    def template_keys(self, *args, **kwargs):
        return {
            'content_title': 'Empréstimo de Equipamento',
            'emprestimo': self.model.objects.get(pk=kwargs.get('pk', None))
        }

def get_atividades(self, pk):
    form = AtividadeSelect(pkmeta=pk)
    return HttpResponse(form)

def get_atividade_bolsistas(self, pk):
    atividade = AtividadeModel.objects.get(pk=pk)
    form = AtividadeBolsistaSelect(pkprojeto=atividade.meta.projeto.pk, instance=AtividadeModel.objects.get(pk=pk))
    return JsonResponse({'form': str(form.as_raw_html()), 'action': {'projeto': atividade.meta.projeto.pk, 'meta': atividade.meta.pk, 'atividade': atividade.pk}})
        
        
