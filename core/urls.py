from django.urls import path
# Home
from .views import IndexView
# Funcionalidades do sistema
from .views import TarefasView, CadastrarTarefaView, AtualizarTarefaView, DeletarTarefaView, TarefasConcluidasView, TarefaConcluirView, TarefasAndamentoView

app_name = 'tasks'
urlpatterns = [
    # Url Home
    path('', IndexView.as_view(), name='index'),
    # Urls funcionalidades do sistema
    path('tarefas/', TarefasView.as_view(), name='tarefas'),
    path('tarefas/concluidas', TarefasConcluidasView.as_view(), name='tarefas_concluidas'),
    path('tarefas/andamento', TarefasAndamentoView.as_view(), name='tarefas_andamento'),
    path('tarefas/add/', CadastrarTarefaView.as_view(), name='add'),
    path('tarefas/<int:pk>/atualizar', AtualizarTarefaView.as_view(), name='tarefa_atl'),
    path('tarefas/<int:pk>/deletar', DeletarTarefaView.as_view(), name='tarefa_del'),
    path('tarefas/<int:pk>/concluir', TarefaConcluirView.as_view(), name='tarefa_concluir'),
]

