from .models import ToDoList
from datetime import datetime, timedelta


def get_tarefas_by_status(user, status, days=30):
    data_limite = datetime.now() - timedelta(days=days)
    return ToDoList.objects.filter(usuario=user, status=status, data_criacao__gte=data_limite)
