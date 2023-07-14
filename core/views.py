from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ToDoList

# Index
class IndexView(TemplateView):
    template_name = 'index.html'

# Login
class LoginUsuarioView(TemplateView):
    template_name = 'login.html'

# Cadastrar usuário
class CadastrarUsuarioView(TemplateView):
    template_name = 'cadastrar_usuario.html'

# Listar
class TarefasView(ListView):
    model = ToDoList
    template_name = 'tarefa.html'
    queryset = ToDoList.objects.all()
    context_object_name = 'tarefas'

# Cadastrar tarefa
class CadastrarTarefaView(CreateView):
    model = ToDoList
    template_name = 'cadastrar_tarefa.html'
    fields = ['nome', 'descricao', 'status',]
    success_url = reverse_lazy('tasks:tarefas')

# Atualizar
class AtualizarTarefaView(UpdateView):
    model = ToDoList
    template_name = 'cadastrar_tarefa.html'
    fields = ['nome', 'descricao', 'status',]
    success_url = reverse_lazy('tasks:tarefas')

# Deletar
class DeletarTarefaView(DeleteView):
    model = ToDoList
    template_name = 'tarefa_del.html'
    success_url = reverse_lazy('tasks:tarefas')
