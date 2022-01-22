import email
from django import forms


class SingUp(forms.Form):
    """
    Форма регистрации пользовователя
    Расположенная в пути /account/register.html
    """
    username = forms.CharField(
        max_length=32, widget=forms.TextInput(attrs={'class': 'form_input'}))

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form_input'}))

    password1 = forms.CharField(
        max_length=48, widget=forms.PasswordInput(attrs={'class': 'form_input'}))

    password2 = forms.CharField(
        max_length=48, widget=forms.PasswordInput(attrs={'class': 'form_input'}))


class LoginIn(forms.Form):
    """
    Форма авторизации пользователя на сайте
    Расположенная в пути /account/login.html
    """
    username = forms.CharField(
        max_length=32, widget=forms.TextInput(attrs={'class': 'form_input'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form_input'}))


class ActivateEmail(forms.Form):
    """
    Форма подтверждения почты после регистрации
    Расположенная в пути /account/activate.html
    """
    code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_input'}))


class GeneralAccountProfile(forms.Form):
    """
    Форма полей профиля
    Расположенная в пути /account/profile.html
    """
    real_name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={}))

    sex = forms.CharField(
        max_length=10, widget=forms.TextInput(attrs={}))

    about_me = forms.CharField(
        max_length=1000, widget=forms.TextInput(attrs={}))


"""
Формы полей профиля
Расположенные в пути /account/profile.html
и /account/security.html
"""


class ChangeEmail(forms.Form):

    new_email = forms.EmailField(widget=forms.EmailInput(attrs={}))

    password1 = forms.CharField(
        max_length=48, widget=forms.PasswordInput(attrs={}))

    password2 = forms.CharField(
        max_length=48, widget=forms.PasswordInput(attrs={}))


class ChangePassword(forms.Form):
    new_password1 = forms.CharField(
        max_length=48, widget=forms.PasswordInput(attrs={'class': 'base_input base-input__input'}))

    new_password2 = forms.CharField(
        max_length=48, widget=forms.PasswordInput(attrs={'class': 'base_input base-input__input'}))
