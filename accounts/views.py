from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from accounts.forms import CustomUserCreationForm

class RegistroUsuarioView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/cadastro.html' 
    success_url = reverse_lazy('login')
