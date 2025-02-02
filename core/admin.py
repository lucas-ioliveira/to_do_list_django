from django.contrib import admin
from .models import ToDoList, WorkSpace

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'titulo', 'descricao', 'status', 'data_criacao',
                    'data_atualizacao', 'ativo', 'work_space')


@admin.register(WorkSpace)
class WorkSpaceAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'titulo', 'data_criacao',
                    'data_atualizacao', 'ativo')