from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    usuario = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User


class PersonajeForm(forms.Form):
    name = forms.CharField()
    id_usuario = forms.CharField()