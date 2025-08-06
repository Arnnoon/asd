from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from .models import User


class CustomLoginView(LoginView):
    """
    CustomLoginView: for user login
    """
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        return reverse('home')


class CustomLogoutView(LogoutView):
    """
    CustomLogoutView: for user logout
    """
    def get_success_url(self):
        return reverse('home')


class RegisterView(CreateView):
    """
    RegisterView: for user registration
    """
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    
    def get_success_url(self):
        return reverse('login')