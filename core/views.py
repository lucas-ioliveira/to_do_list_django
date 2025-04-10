
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from datetime import datetime

from .models import ToDoList, WorkSpace
from .utils import get_tarefas_by_status


class IndexView(TemplateView):
    template_name = 'home/index.html'


@method_decorator(login_required, name='dispatch')
class WorkSpaceView(View):
    def get(self, request):
        work_space = WorkSpace.objects.filter(usuario=request.user, ativo=True).order_by('data_criacao')
        context = {
            'work_space': work_space
        }
        return render(request, 'work_space/work_space.html', context)

    def post(self, request):
        titulo = request.POST.get('titulo')
        work_space = WorkSpace.objects.create(titulo=titulo, usuario=request.user)
        work_space.save()
        messages.success(request, 'Espaco de trabalho criado com sucesso!')
        return redirect('tasks:work-space')


@method_decorator(login_required, name='dispatch')
class WorkSpaceEditarView(View):
    def post(self, request, pk):
        work_space = get_object_or_404(WorkSpace, pk=pk)
        work_space.titulo = request.POST.get('titulo')
        work_space.save()
        messages.success(request, 'Espaco de trabalho editado com sucesso!')
        return redirect('tasks:work-space')


@method_decorator(login_required, name='dispatch')
class WorkSpaceDeletarView(View):
    def post(self, request, pk):
        work_space = get_object_or_404(WorkSpace, pk=pk)
        work_space.ativo = False
        work_space.save()
        messages.success(request, 'Espaco de trabalho deletado com sucesso!')
        return redirect('tasks:work-space')


@method_decorator(login_required, name='dispatch')
class TarefasListView(View):
    def get(self, request, work_space):
        work_space_id = WorkSpace.objects.get(id=work_space)
        work_space_name = work_space_id.titulo
        status = ToDoList.STATUS_CHOICES
        tarefas = get_tarefas_by_status(request.user, 'À fazer', work_space=work_space).order_by('-data_criacao')
        context = {
            'tarefas': tarefas,
            'status': status,
            'work_space_name': work_space_name,
            'work_space_id': work_space,
            'tarefas_concluidas': get_tarefas_by_status(request.user, 'Concluido', work_space=work_space).count(),
            'tarefas_em_andamento': get_tarefas_by_status(request.user, 'Andamento', work_space=work_space).count(),
            'tarefas_a_fazer': get_tarefas_by_status(request.user, 'À fazer', work_space=work_space).count(),
            'tarefas_pausadas': get_tarefas_by_status(request.user, 'Pausado', work_space=work_space).count(),
        }

        return render(request, 'tasks/tarefa.html', context)


@method_decorator(login_required, name='dispatch')
class TarefaCreateView(View):
    def post(self, request):
        previous_page = request.META.get('HTTP_REFERER')
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        status = request.POST.get('status')
        work_space_nome = request.POST.get('espaco_trabalho')
        work_space_id = WorkSpace.objects.filter(titulo=work_space_nome).first()

        tarefa = ToDoList.objects.create(
            titulo=titulo, descricao=descricao, status=status,
            work_space=work_space_id, usuario=request.user
        )
        tarefa.save()
        messages.success(request, 'Tarefa criada com sucesso!')
        return redirect(previous_page)


@method_decorator(login_required, name='dispatch')
class TarefasConcluidasView(View):
    def get(self, request):
        tarefas = get_tarefas_by_status(request.user, 'Concluido', work_space=request.GET.get('work_space')).order_by('-data_criacao')
        return render(request, 'tasks/tarefas_concluidas.html', {'tarefas': tarefas})


@method_decorator(login_required, name='dispatch')
class TarefasAndamentoView(View):
    def get(self, request):
        tarefas = get_tarefas_by_status(request.user, 'Andamento', work_space=request.GET.get('work_space')).order_by('-data_criacao')
        return render(request, 'tasks/tarefas_andamento.html', {'tarefas': tarefas})


@method_decorator(login_required, name='dispatch')
class TarefasPausadasView(View):
    def get(self, request):
        tarefas = get_tarefas_by_status(request.user, 'Pausado', work_space=request.GET.get('work_space')).order_by('-data_criacao')
        return render(request, 'tasks/tarefas_pausadas.html', {'tarefas': tarefas})


@method_decorator(login_required, name='dispatch')
class TarefaConcluirView(View):
    def post(self, request, pk):
        previous_page = request.META.get('HTTP_REFERER')
        tarefa = get_object_or_404(ToDoList, pk=pk)
        tarefa.status = 'Concluido'
        tarefa.save()
        messages.success(request, 'Tarefa concluida com sucesso!')
        return redirect(previous_page)


@method_decorator(login_required, name='dispatch')
class TarefaEditarView(View):
    def post(self, request, pk):
        previous_page = request.META.get('HTTP_REFERER')
        tarefa = get_object_or_404(ToDoList, pk=pk)
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.status = request.POST.get('status')
        tarefa.save()
        messages.success(request, 'Tarefa editada com sucesso!')
        return redirect(previous_page)


@method_decorator(login_required, name='dispatch')
class TarefaClonarView(View):
    def post(self, request, pk):
        previous_page = request.META.get('HTTP_REFERER')
        tarefa = get_object_or_404(ToDoList, pk=pk)
        tarefa.pk = None
        tarefa.status = 'À fazer'
        tarefa.data_criacao = datetime.now().date()
        tarefa.save()
        messages.success(request, 'Tarefa clonada com sucesso!')
        return redirect(previous_page)


@method_decorator(login_required, name='dispatch')
class TarefaDeletarView(View):
    def post(self, request, pk):
        previous_page = request.META.get('HTTP_REFERER')
        tarefa = get_object_or_404(ToDoList, pk=pk)
        tarefa.ativo = False
        tarefa.save()
        messages.success(request, 'Tarefa deletada com sucesso!')
        return redirect(previous_page)


def custom_404(request, exception):
    return render(request, '404.html', status=404)
