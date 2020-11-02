from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'common/login.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('login')

class SignUpView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'common/register.html'

class SignInView(LoginView):
    template_name = 'common/login.html'
