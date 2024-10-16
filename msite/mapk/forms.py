from django import forms
from .models import Register, Login
from django.forms.widgets import PasswordInput, TextInput
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username','phone','email', 'password']
        # password = forms.CharField(widget=forms.PasswordInput())

class Login(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['email', 'password']

# class Login(forms.Form):
#     email = forms.EmailField(widget = forms.TextInput())
#     password = forms.CharField(widget=forms.PasswordInput())
