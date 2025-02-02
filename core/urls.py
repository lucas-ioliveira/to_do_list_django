from django.urls import path
# Home
from .views import IndexView
# Funcionalidades do sistema
from .views import (
    work_space_view, create_work_space_view, tarefas_list_view, tarefas_cadastrar_view, tarefas_concluidas_view,
    tarefas_andamento_view, tarefas_pausadas_view, tarefas_concluir_view, tarefas_editar_view, tarefas_clonar_view,
    tarefas_deletar_view
)

app_name = 'tasks'
router_path = 'tarefas'

urlpatterns = [
    # Url Home
    path('', IndexView.as_view(), name='index'),
    # Urls funcionalidades do sistema
    path(f'{router_path}/espaco-trabalho/', work_space_view, name='work-space'),
    path(f'{router_path}/espaco-trabalho/cadastrar', create_work_space_view, name='work-space-cadastar'), 
    path(f'{router_path}/<int:work_space>/', tarefas_list_view, name='tarefas-list'),
    path(f'{router_path}/cadastrar/', tarefas_cadastrar_view, name='tarefas-cadastrar'),
    path(f'{router_path}/concluidas/', tarefas_concluidas_view, name='tarefas-concluidas'),
    path(f'{router_path}/andamentos', tarefas_andamento_view, name='tarefas_andamento'),
    path(f'{router_path}/pausadas', tarefas_pausadas_view, name='tarefas_pausadas'),
    path(f'{router_path}/concluir/<int:pk>/', tarefas_concluir_view, name='tarefa_concluir'),
    path(f'{router_path}/editar/<int:pk>/', tarefas_editar_view, name='tarefa_editar'),
    path(f'{router_path}/clonar/<int:pk>/', tarefas_clonar_view, name='tarefa_clonar'),
    path(f'{router_path}/deletar/<int:pk>/', tarefas_deletar_view, name='tarefa_deletar'),
]

