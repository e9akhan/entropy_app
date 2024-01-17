from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from accounts.forms import UserForm

# Create your views here.
class CreateUser(CreateView):
    model = User
    form_class = UserForm
    template_name = 'accounts/signup.html'
