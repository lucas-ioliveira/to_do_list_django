# Para menssagens do django
from django.contrib.messages.views import SuccessMessageMixin
# Para as funcionalidades do sistema
from django.views.generic import TemplateView, ListView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Para redirecionar o usuario
from django.urls import reverse_lazy
# Para autenticação e registro do usuário
# Para o usuário acessar a página somente se estiver logado
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404
from django.contrib import messages

# model de usuário e das funções do sistema
from .models import ToDoList

from .utils import get_tarefas_by_status

from datetime import datetime

# Home
# Index
class IndexView(TemplateView):
    template_name = 'index.html'


# Funcionalidades do sistema
# Listar

class TarefasView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = 'tarefa.html'
    context_object_name = 'tarefas'
    paginate_by = 6

    def get_queryset(self):
        return ToDoList.objects.filter(usuario=self.request.user, status='À fazer').order_by('-data_criacao')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        usuario = self.request.user
        context['total_tarefas'] = ToDoList.objects.filter(usuario=usuario).count()
        context['tarefas_concluidas'] = ToDoList.objects.filter(usuario=usuario, status='Concluido').count()
        context['tarefas_em_andamento'] = ToDoList.objects.filter(usuario=usuario, status='Andamento').count()
        context['tarefas_a_fazer'] = ToDoList.objects.filter(usuario=usuario, status='À fazer').count()
        context['tarefas_pausadas'] = ToDoList.objects.filter(usuario=usuario, status='Pausado').count()

        return context
    

# Listar tarefas concluidas
class TarefasConcluidasView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = 'tarefas_concluidas.html'
    context_object_name = 'tarefas'
    paginate_by = 6

    def get_queryset(self):
        return get_tarefas_by_status(self.request.user, 'Concluido').order_by('-data_criacao')


# Listar tarefas andamento
class TarefasAndamentoView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = 'tarefas_andamento.html'
    context_object_name = 'tarefas'
    paginate_by = 6

    def get_queryset(self):
        return get_tarefas_by_status(self.request.user, 'Andamento').order_by('-data_criacao')


class TarefasPausadasView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = 'tarefas_pausadas.html'
    context_object_name = 'tarefas'
    paginate_by = 6

    def get_queryset(self):
        return get_tarefas_by_status(self.request.user, 'Pausado').order_by('-data_criacao')


# Concluir tarefa
class TarefaConcluirView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        tarefa = get_object_or_404(ToDoList, pk=self.kwargs['pk'])
        tarefa.status = 'Concluido' 
        tarefa.save()
        messages.success(self.request, 'Tarefa concluída com sucesso!')
        return reverse_lazy('tasks:tarefas')
        

# Cadastrar tarefa
class CadastrarTarefaView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ToDoList
    template_name = 'cadastrar_tarefa.html'  
    fields = ['titulo', 'descricao', 'status']  
    success_url = reverse_lazy('tasks:tarefas')  

    def form_valid(self, form):
        form.instance.usuario = self.request.user  
        return super().form_valid(form)


# Atualizar
class AtualizarTarefaView(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    model = ToDoList
    template_name = 'cadastrar_tarefa.html'
    fields = ['titulo', 'descricao', 'status',]
    success_url = reverse_lazy('tasks:tarefas')
    success_message = "A tarefa foi atualizada com sucesso!"



# Deletar
class DeletarTarefaView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ToDoList
    template_name = 'tarefa_del.html'
    success_url = reverse_lazy('tasks:tarefas')
    success_message = "A tarefa foi deletada com sucesso!"

    def get_queryset(self):
        return ToDoList.objects.filter(usuario=self.request.user)


class ClonarTarefaView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        tarefa = get_object_or_404(ToDoList, pk=self.kwargs['pk'])
        tarefa.pk = None  
        tarefa.status = 'À fazer'  
        tarefa.data_criacao = datetime.now().date()
        tarefa.save()  
        messages.success(self.request, 'Tarefa clonada com sucesso!')
        return reverse_lazy('tasks:tarefas')

