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

    def get_queryset(self):
        return ToDoList.objects.filter(usuario=self.request.user)


# Listar tarefas concluidas
class TarefasConcluidasView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = 'tarefas_concluidas.html'
    context_object_name = 'tarefas'

    def get_queryset(self):
        return ToDoList.objects.filter(usuario=self.request.user, status='Concluido')


# Concluir tarefa
class TarefaConcluirView(RedirectView):
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

