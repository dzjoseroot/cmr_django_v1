from django.urls import path
from django.views.generic import TemplateView
from .views import *
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password-reset/', PasswordForgotenView.as_view(), name='password-reset'),
    path('password-reset/done/', PasswordDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordConfirmResetView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordCompleteResetView.as_view(), name='password_reset_complete'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),
]