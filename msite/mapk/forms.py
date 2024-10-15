from django import forms
# from .models import Register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'phone', 'email', 'password']
        # password = forms.CharField(widget=forms.PasswordInput())


class Login(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
