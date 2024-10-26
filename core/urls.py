from django.urls import path
# Home
from .views import IndexView
# Funcionalidades do sistema
from .views import (
    TarefasView, CadastrarTarefaView, AtualizarTarefaView, DeletarTarefaView,
    TarefasConcluidasView, TarefaConcluirView, TarefasAndamentoView, 
    ClonarTarefaView, TarefasPausadasView
)

app_name = 'tasks'
router_path = 'tarefas'

urlpatterns = [
    # Url Home
    path('', IndexView.as_view(), name='index'),
    # Urls funcionalidades do sistema
    path(f'{router_path}/', TarefasView.as_view(), name='tarefas'),
    path(f'{router_path}/concluidas', TarefasConcluidasView.as_view(), name='tarefas_concluidas'),
    path(f'{router_path}/andamentos', TarefasAndamentoView.as_view(), name='tarefas_andamento'),
    path(f'{router_path}/pausadas', TarefasPausadasView.as_view(), name='tarefas_pausadas'),
    path(f'{router_path}/add/', CadastrarTarefaView.as_view(), name='tarefa_add'),
    path(f'{router_path}/<int:pk>/atualizar', AtualizarTarefaView.as_view(), name='tarefa_atl'),
    path(f'{router_path}/<int:pk>/deletar', DeletarTarefaView.as_view(), name='tarefa_del'),
    path(f'{router_path}/<int:pk>/concluir', TarefaConcluirView.as_view(), name='tarefa_concluir'),
    path(f'{router_path}/<int:pk>/clonar', ClonarTarefaView.as_view(), name='tarefa_clonar'),
]

