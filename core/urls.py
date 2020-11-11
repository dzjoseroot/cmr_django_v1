from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from apps.common.views import *
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
]
