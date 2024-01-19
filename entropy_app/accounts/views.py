from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import UserForm, UserAuthenticatioForm

# Create your views here.
class CreateUser(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'accounts/signup.html'
    success_message = 'User created.'
    success_url = reverse_lazy('signup')

    def form_invalid(self, form):
        messages.info(self.request, form.errors)
        return super().form_invalid(form)

class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    form_class = UserAuthenticatioForm
    success_message = 'Login Successful.'
    
    def get_success_url(self) -> str:
        return reverse_lazy('signup')
