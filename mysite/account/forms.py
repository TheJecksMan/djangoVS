from ast import arg
import email
from django import forms


class SingUp(forms.Form):

    username = forms.CharField(
        max_length=32, widget=forms.TextInput(attrs={'class': 'form_input'}))

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form_input'}))

    password1 = forms.CharField(
        max_length=48, widget=forms.PasswordInput(attrs={'class': 'form_input'}))

    password2 = forms.CharField(
        max_length=48, widget=forms.PasswordInput(attrs={'class': 'form_input'}))


class LoginIn(forms.Form):
    username = forms.CharField(
        max_length=32, widget=forms.TextInput(attrs={'class': 'form_input'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form_input'}))
