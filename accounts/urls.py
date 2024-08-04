from django.urls import path, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from accounts.views import RegistroUsuarioView

urlpatterns = [
    path('login/', LoginView.as_view(
        form_class=AuthenticationForm,
        template_name='login.html'
    ), name='login'),

    path('logout/', LogoutView.as_view(
        next_page=reverse_lazy('login')
    ), name='logout'),

    path('alterar-senha/', PasswordChangeView.as_view(
        form_class=PasswordChangeForm,
        template_name='alteracao_senha.html',
        success_url=reverse_lazy('login')
    ), name='alterar_senha'),

    path('cadastro/', RegistroUsuarioView.as_view(), name='registro'),
]
