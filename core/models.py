from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 


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
    titulo = models.CharField(verbose_name='Titulo', max_length=255)
    descricao = models.TextField(verbose_name='Descrição')
    status = models.CharField(verbose_name='Status', max_length=15, 
                              choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Lista de Tarefa'
        verbose_name_plural = 'Lista de Tarefas'    
    
    def __str__(self) -> str:
        return self.titulo


# Gerenciador
class UsuarioManage(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
        
        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    username = models.CharField('Username', max_length=255, default='user_defult_value')
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self) -> str:
        return self.email
    
    objects = UsuarioManage()