from django import forms
from .models import Register

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'phone', 'email', 'password']
        password = forms.CharField(widget=forms.PasswordInput())


class Login(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
