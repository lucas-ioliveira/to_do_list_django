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
# para funções de login e logout
from django.contrib.auth.views import LoginView, LogoutView

from django.shortcuts import get_object_or_404
from django.contrib import messages

# Formulário baseado no meu model para auyenticação e registro
from .forms import CustomUsuarioCreateForm
# model de usuário e das funções do sistema
from .models import ToDoList, CustomUsuario


# Home
# Index
class IndexView(TemplateView):
    template_name = 'index.html'


# Autenticação 

# Login
class LoginUsuarioView(LoginView):
    template_name = 'registration/login.html'


# Logout
class LogoutUsuarioView(LogoutView):
    template_name = 'tasks:index'


# Cadastrar usuário
class RegistroUsuarioView(SuccessMessageMixin, CreateView):
    template_name = 'registration/registro.html'
    model = CustomUsuario
    forms = CustomUsuarioCreateForm
    fields = ('email', 'password', 'first_name', 'last_name', 'fone')
    success_url = reverse_lazy('tasks:login')
    success_message = "Conta criada com sucesso! Faça login para acessar sua conta."

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


# Funcionalidades do sistema
# Listar

class TarefasView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = 'tarefa.html'
    queryset = ToDoList.objects.exclude(status='Concluido')
    context_object_name = 'tarefas'


# Listar tarefas concluidas
class TarefasConcluidasView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = 'tarefas_concluidas.html'
    queryset = ToDoList.objects.filter(status='Concluido')
    context_object_name = 'tarefas'


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
    fields = ['titulo', 'descricao', 'status',]
    success_url = reverse_lazy('tasks:tarefas')
    success_message = "A tarefa foi criada com sucesso!"



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


