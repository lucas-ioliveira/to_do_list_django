from django.urls import path
# Home
from .views import IndexView
# Funcionalidades do sistema
from .views import (
    WorkSpaceView, WorkSpaceEditarView, WorkSpaceDeletarView, TarefasListView, TarefaCreateView, TarefasConcluidasView, 
    TarefasAndamentoView, TarefasPausadasView, TarefaConcluirView, TarefaEditarView, TarefaClonarView, TarefaDeletarView
)

app_name = 'tasks'
router_path = 'tarefas'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path(f'{router_path}/espaco-trabalho/', WorkSpaceView.as_view(), name='work-space'),
    path(f'{router_path}/espaco-trabalho/editar/<int:pk>/', WorkSpaceEditarView.as_view(), name='work-space-editar'),
    path(f'{router_path}/espaco-trabalho/deletar/<int:pk>/', WorkSpaceDeletarView.as_view(), name='work-space-deletar'),
    path(f'{router_path}/<int:work_space>/', TarefasListView.as_view(), name='tarefas-list'),
    path(f'{router_path}/cadastrar/', TarefaCreateView.as_view(), name='tarefas-cadastrar'),
    path(f'{router_path}/concluidas/', TarefasConcluidasView.as_view(), name='tarefas-concluidas'),
    path(f'{router_path}/andamentos', TarefasAndamentoView.as_view(), name='tarefas_andamento'),
    path(f'{router_path}/pausadas', TarefasPausadasView.as_view(), name='tarefas_pausadas'),
    path(f'{router_path}/concluir/<int:pk>/', TarefaConcluirView.as_view(), name='tarefa_concluir'),
    path(f'{router_path}/editar/<int:pk>/', TarefaEditarView.as_view(), name='tarefa_editar'),
    path(f'{router_path}/clonar/<int:pk>/', TarefaClonarView.as_view(), name='tarefa_clonar'),
    path(f'{router_path}/deletar/<int:pk>/', TarefaDeletarView.as_view(), name='tarefa_deletar'),
]

