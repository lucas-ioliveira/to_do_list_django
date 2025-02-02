from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    data_criacao = models.DateTimeField(verbose_name='Data de criação', 
                                    auto_now_add=True)
    data_atualizacao = models.DateTimeField(verbose_name='Data de atualização',
                                        auto_now=True)
    ativo = models.BooleanField(verbose_name='Ativo?', default=True)

    class Meta:
        abstract = True

class WorkSpace(Base):
    usuario = models.ForeignKey(User, verbose_name='usuario', on_delete=models.CASCADE)
    titulo = models.CharField(verbose_name='Titulo', max_length=255)

    class Meta:
        verbose_name = 'Espaço de trabalho'
        verbose_name_plural = 'Espaços de trabalhos'
    
    def __str__(self):
        return f"{self.titulo}"


class ToDoList(Base):
    STATUS_CHOICES = (
        ('Concluido', 'Concluido'),
        ('À fazer', 'À fazer'),
        ('Andamento', 'Andamento'),
        ('Pausado', 'Pausado')
    )
    usuario = models.ForeignKey(User, verbose_name='usuario', on_delete=models.CASCADE)
    titulo = models.CharField(verbose_name='Titulo', max_length=255)
    descricao = models.TextField(verbose_name='Descrição')
    status = models.CharField(verbose_name='Status', max_length=15, 
                              choices=STATUS_CHOICES)
    work_space = models.ForeignKey(WorkSpace, verbose_name='Espaço de trabalho', 
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Lista de Tarefa'
        verbose_name_plural = 'Listas de Tarefas'    
    
    def __str__(self):
        return f"{self.titulo}"
