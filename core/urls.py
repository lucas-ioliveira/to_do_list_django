from django.urls import path
from .views import IndexView, LoginUsuarioView, CadastrarUsuarioView, TarefasView
from .views import CadastrarTarefaView, AtualizarTarefaView, DeletarTarefaView

app_name = 'tasks'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginUsuarioView.as_view(), name='login'),
    path('cadastrar/', CadastrarUsuarioView.as_view(), name='cadastrar'),
    path('tarefas/', TarefasView.as_view(), name='tarefas'),
    path('tarefas/add/', CadastrarTarefaView.as_view(), name='add'),
    path('tarefas/atualizar/<int:pk>', AtualizarTarefaView.as_view(), 
         name='tarefa_atl'),
    path('tarefas/deletar/<int:pk>', DeletarTarefaView.as_view(), 
         name='tarefa_del')
]
