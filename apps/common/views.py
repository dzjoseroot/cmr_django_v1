from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

class HomeView(RedirectView):
    #template_name = 'common/login.html'
    url = 'login/'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('login')

class SignUpView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'common/register.html'

class SignInView(LoginView):
    template_name = 'common/login.html'

class ChangePasswordView(PasswordChangeView):
    template_name = 'common/change-password.html'
    success_url = reverse_lazy('login')

class PasswordForgotenView(PasswordResetView):
    template_name = 'common/password-reset/password_reset.html'
    subject_template_name = 'common/password-reset/password_reset_subject.txt'
    email_template_name = 'common/password-reset/password_reset_email.html'

class PasswordDoneView(PasswordResetDoneView):
    template_name = 'common/password-reset/password_reset_done.html'

class PasswordConfirmResetView(PasswordResetConfirmView):
    template_name = 'common/password-reset/password_reset_confirm.html'

class PasswordCompleteResetView(PasswordResetCompleteView):
    template_name = 'common/password-reset/password_reset_complete.html'
    
