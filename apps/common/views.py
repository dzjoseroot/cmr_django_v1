from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib import messages
from django.contrib.auth.models import User
from apps.userprofile.models import Profile
from django.http import HttpResponseRedirect

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

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'common/profile.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'common/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(user_form=user_form,profile_form=profile_form)

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
