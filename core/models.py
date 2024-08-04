from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    data_criacao = models.DateField(verbose_name='Data de criação', 
                                    auto_now_add=True)
    data_atualizacao = models.DateField(verbose_name='Data de atualização',
                                        auto_now=True)
    ativo = models.BooleanField(verbose_name='Ativo?', default=True)

    class Meta:
        abstract = True

class ToDoList(Base):
    STATUS_CHOICES = (
        ('Concluido', 'Concluido'),
        ('À fazer', 'À fazer'),
        ('Em andamento', 'Em andamento'),
        ('Pausado', 'Pausado'),
        ('Finalizado', 'Finalizado')
    )
    usuario = models.ForeignKey(User, verbose_name='usuario', on_delete=models.CASCADE)
    titulo = models.CharField(verbose_name='Titulo', max_length=255)
    descricao = models.TextField(verbose_name='Descrição')
    status = models.CharField(verbose_name='Status', max_length=15, 
                              choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Lista de Tarefa'
        verbose_name_plural = 'Lista de Tarefas'    
    
    def __str__(self):
        return f"{self.titulo}"
