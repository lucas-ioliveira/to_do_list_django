
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import ToDoList, WorkSpace
from .utils import get_tarefas_by_status

# Home
# Index
class IndexView(TemplateView):
    template_name = 'index.html'

@login_required
def work_space_view(request):
    work_space = WorkSpace.objects.filter(usuario=request.user).order_by('data_criacao')
    context = {
        'work_space': work_space
    }
    return render(request, 'work_space.html', context)

@login_required
def create_work_space_view(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        work_space = WorkSpace.objects.create(titulo=titulo, usuario=request.user)
        work_space.save()
        return redirect('tasks:work-space')
    return render(request, 'work_space.html')

@login_required
def tarefas_list_view(request, work_space):
    if request.method == 'POST':
        
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

        return render(request, 'tarefa.html', context)
    return render(request, 'tarefa.html')

@login_required
def tarefas_cadastrar_view(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        status = request.POST.get('status')
        work_space_nome = request.POST.get('espaco_trabalho')
        work_space_id = WorkSpace.objects.filter(titulo=work_space_nome).first()

        tarefa = ToDoList.objects.create(titulo=titulo, descricao=descricao, status=status, 
                                         work_space=work_space_id, 
                                         usuario=request.user)
        tarefa.save()
        messages.success(request, 'Tarefa criada com sucesso!')
        return redirect('tasks:work-space')
    return render(request, 'tarefa.html')

@login_required
def tarefas_concluidas_view(request):
    if request.method == 'POST':
        tarefas = get_tarefas_by_status(request.user, 'Concluido', work_space=request.POST.get('work_space')).order_by('-data_criacao')
        return render(request, 'tarefas_concluidas.html', {'tarefas': tarefas})
    return render(request, 'tarefa.html')

@login_required
def tarefas_andamento_view(request):
    if request.method == 'POST':
        tarefas = get_tarefas_by_status(request.user, 'Andamento', work_space=request.POST.get('work_space')).order_by('-data_criacao')
        return render(request, 'tarefas_andamento.html', {'tarefas': tarefas})
    return render(request, 'tarefa.html')

@login_required
def tarefas_pausadas_view(request):
    if request.method == 'POST':
        tarefas = get_tarefas_by_status(request.user, 'Pausado', work_space=request.POST.get('work_space')).order_by('-data_criacao')
        return render(request, 'tarefas_pausadas.html', {'tarefas': tarefas})
    return render(request, 'tarefa.html')
    
@login_required
def tarefas_concluir_view(request, pk):
    if request.method == 'POST':
        tarefa = get_object_or_404(ToDoList, pk=pk)
        tarefa.status = 'Concluido' 
        tarefa.save()
        messages.success(request, 'Tarefa concluida com sucesso!')
        return redirect('tasks:work-space')
    return render(request, 'tarefa.html')
@login_required
def tarefas_editar_view(request, pk):
    if request.method == 'POST':
        tarefa = get_object_or_404(ToDoList, pk=pk)
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.status = request.POST.get('status')
        tarefa.save()
        messages.success(request, 'Tarefa editada com sucesso!')
        return redirect('tasks:work-space')
    return render(request, 'tarefa.html')

@login_required
def tarefas_clonar_view(request, pk):
    if request.method == 'POST':
        tarefa = get_object_or_404(ToDoList, pk=pk)
        tarefa.pk = None  
        tarefa.status = 'À fazer'  
        tarefa.data_criacao = datetime.now().date()
        tarefa.save()  
        messages.success(request, 'Tarefa clonada com sucesso!')
        return redirect('tasks:work-space')
    return render(request, 'tarefa.html')

@login_required
def tarefas_deletar_view(request, pk):
    if request.method == 'POST':
        import ipdb; ipdb.set_trace()
        tarefa = get_object_or_404(ToDoList, pk=pk)
        tarefa.ativo = False
        tarefa.save()
        messages.success(request, 'Tarefa deletada com sucesso!')
        return redirect('tasks:work-space')
    return render(request, 'tarefa.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)
