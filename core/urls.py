from django.urls import path
# Home
from .views import IndexView
# Funcionalidades do sistema
from .views import TarefasView, CadastrarTarefaView, AtualizarTarefaView, DeletarTarefaView
from .views import LoginUsuarioView, LogoutUsuarioView, RegistroUsuarioView

app_name = 'tasks'
urlpatterns = [
    # Url Home
    path('', IndexView.as_view(), name='index'),
    # Urls funcionalidades do sistema
    path('tarefas/', TarefasView.as_view(), name='tarefas'),
    path('tarefas/add/', CadastrarTarefaView.as_view(), name='add'),
    path('tarefas/atualizar/<int:pk>', AtualizarTarefaView.as_view(), 
         name='tarefa_atl'),
    path('tarefas/deletar/<int:pk>', DeletarTarefaView.as_view(), 
         name='tarefa_del'),
     # Urls de autenticação
     path('accouts/login', LoginUsuarioView.as_view(), name='login'),
     path('logout/', LogoutUsuarioView.as_view(), name='logout'),
     path('accounts/registro', RegistroUsuarioView.as_view(), name='registro' )
]

