from ast import arg
import email
from django import forms


class SingUp(forms.Form):
    login = forms.CharField(max_length=32, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(max_length=48, required=True,)
    password2 = forms.CharField(max_length=48, required=True)


class LoginIn(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form_input'
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form_input'
        }))
