from django.db import models


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
        ('Bloqueado', 'Bloqueado'),
        ('Finalizado', 'Finalizado')
    )
    nome = models.CharField(verbose_name='Nome', max_length=255)
    descricao = models.TextField(verbose_name='Descrição')
    status = models.CharField(verbose_name='Status', max_length=15, 
                              choices=STATUS_CHOICES)    
    
    def __str__(self) -> str:
        return self.nome

