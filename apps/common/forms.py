from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.userprofile.models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Enter a valiñd email address')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'phone_number',
            'birth_date',
            'profile_image'
        ]