from django.contrib import admin
from .models import ToDoList 

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'titulo', 'descricao', 'status', 'data_criacao',
                    'data_atualizacao', 'ativo')
