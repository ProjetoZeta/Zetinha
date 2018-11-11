from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django import forms

from .models import Cargo as CargoModel, Entidade as EntidadeModel, Funcao as FuncaoModel, Usuario as  UsuarioModel, Bolsista as BolsistaModel, Documento as DocumentoModel, EmprestimoEquipamento as EmprestimoEquipamentoModel, Projeto as ProjetoModel, Participante as ParticipanteModel, Meta as MetaModel
from .forms import CargoForm, EntidadeForm, FuncaoForm, ResponsavelForm, UsuarioForm, BolsistaForm, DocumentoForm, ProjetoForm, EmprestimoEquipamentoForm, ParticipanteProjetoForm, ParticipanteBolsistaForm, MetaForm
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

    def post(self, request, **kwargs):

        pk = kwargs.get(self.pk_alias, None)

        bolsista = self.model.objects.get(pk=pk) if pk else None

        participantes = ParticipanteModel.objects.filter(bolsista=bolsista, ic_ativo=True) if pk else None

        last_participante = participantes.latest('id') if participantes else None

        formp = ParticipanteBolsistaForm(request.POST,instance=last_participante)
        form = self.form(request.POST, instance=(bolsista if bolsista else None))

        if form.is_valid():
            b = form.save()
            post = request.POST.copy() # to make it mutable
            post['bolsista'] = b.pk
            request.POST = post
            formp = ParticipanteBolsistaForm(request.POST,instance=last_participante)
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

class BolsistaList(GenericView):

    model = BolsistaModel
    template_name = 'cadastro/crud-bolsista.html'

    def template_keys(self, **kwargs):
        return {
            **super().template_keys(**kwargs),
            'content_title': 'Bolsistas',
            'data': self.model.objects.all(),
            'form': BolsistaForm()
        }


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

class ProjetoList(GenericView):

    model = ProjetoModel
    template_name = 'cadastro/crud-projeto.html'

    def template_keys(self, **kwargs):
        return {
            **super().template_keys(**kwargs),
            'content_title': 'Projetos',
            'data': self.model.objects.all(),
            'form': ProjetoForm()
        }


class Projeto(FormView):

    template_name = 'cadastro/projeto.html'

    def dispatch(self, request, **kwargs):

        self.delete_redirect = ('projeto',)
        
        return super().dispatch(request, **kwargs)

    def post(self, request, **kwargs):

        pk = kwargs.get(self.pk_alias, None)

        form = self.form(request.POST, instance=self.model.objects.get(pk=pk)) if pk else self.form(request.POST)
        v = form.is_valid()
        nprojeto = form.save() if v else None
        if nprojeto:
                return redirect(*('projeto-editar', nprojeto.pk,))
        else:
            return self.get(request=request, form=form, **kwargs)

    def template_keys(self, **kwargs):
        pk = kwargs.get('pk', None)
        return {
            **super().template_keys(**kwargs),
            'content_title': 'Manter Projeto',
            'formp': ParticipanteProjetoForm(initial={'projeto': ProjetoModel.objects.get(pk=pk)}) if pk else ParticipanteProjetoForm(),
            'pk': kwargs.get('pk', None),
            'formm': MetaForm(),
            'datap': ParticipanteModel.objects.filter(projeto=ProjetoModel.objects.get(pk=pk)) if pk else []
        }

class ParticipanteProjeto(FormView):

    def dispatch(self, request, **kwargs):

        self.delete_redirect = ('participante-proj-criar', kwargs.get('pk', None),)
        
        return super().dispatch(request, **kwargs)

    model = ParticipanteModel
    template_name = 'cadastro/projeto.html'
    pk_alias = 'pkparticipante'

    def post(self, request, **kwargs):

        pk = kwargs.get(self.pk_alias, None)
        projetopk = kwargs.get('pk', None)

        initial = {'projeto': ProjetoModel.objects.get(pk=projetopk)} if projetopk else ParticipanteProjetoForm()

        form = ParticipanteProjetoForm(request.POST, initial=initial, instance=self.model.objects.get(pk=pk)) if pk else ParticipanteProjetoForm(request.POST)

        v = form.is_valid()
        nparticipante = form.save() if v else None
        if nparticipante:
            return redirect(*('participante-proj-editar', nparticipante.projeto.pk, nparticipante.pk,))
        else:
            return self.get(request=request, formp=form, **kwargs)

    def template_keys(self, **kwargs):

        pk = kwargs.get('pk', None)
        pkparticipante = kwargs.get('pkparticipante', None)

        fp = kwargs.get('formp', None)
        formp = fp if fp else (ParticipanteProjetoForm(instance=self.model.objects.get(pk=pkparticipante)) if pkparticipante else ParticipanteProjetoForm())

        return {
            **super().template_keys(**kwargs),
            'content_title': 'Manter Projeto',
            'pk': pk,
            'pkparticipante': kwargs.get('pkparticipante', None),
            'formp': formp,
            'form': ProjetoForm(instance=ProjetoModel.objects.get(pk=pk)),
            'datap': ParticipanteModel.objects.filter(projeto=ProjetoModel.objects.get(pk=pk)) if pk else []
        }

