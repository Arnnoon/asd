from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class UserLoginView(LoginView):
    """
    UserLoginView: for logging in users
    """
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('blogs:home')


class UserRegisterView(CreateView):
    """
    UserRegisterView: for registering users
        - use template 'accounts/register.html'
        - use form for creating users
    """
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('user_accounts:login')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('user_accounts:login')
