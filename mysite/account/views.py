from django.shortcuts import redirect, render
from .forms import *

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required  # redirect form login
def profile_account(request):
    return render(request, 'account/profile.html')


@login_required
def security_account(request):

    if request.method == 'POST':
        form = ChangePassword(request.POST)
        if form.is_valid():
            username = request.user.username
            new_password1 = request.POST['new_password1']  # password
            new_password2 = request.POST['new_password2']  # repeat password
            if new_password1 == new_password2:
                user = User.objects.get(username=username)
                user.set_password(new_password1)
                user.save()
    else:
        form = ChangePassword()

    return render(request, 'account/security.html', {'form': form})


def activate_account(request):
    form = ActivateEmail()
    return render(request, 'account/activate.html', {'form': form})


def reminder(request):
    return render(request, 'account/reminder.html')


def sing_up(request):  # registartion account
    error_text = ''
    if request.method == 'POST':
        form = SingUp(request.POST)
        if form.is_valid():

            email = request.POST['email']  # email
            username = request.POST['username']  # login
            password1 = request.POST['password1']  # password
            password2 = request.POST['password2']  # repeat password

            if password1 == password2:  # valid password
                # check valid email
                if not User.objects.filter(email=email).exists():
                    # check valid username
                    if not User.objects.filter(username=username).exists():
                        user = User.objects.create_user(
                            username, email, password1)

                        user.is_active = False
                        user.save()  # create user
                        return redirect('http://localhost:8000/activate/', permanent=True)
                    else:
                        error_text = '???????????????????????? ?? ?????????? ???????????? ?????? ????????????????????'
                else:
                    error_text = '???????????????????????? ?? ?????????? Email ?????? ????????????????????'
            else:
                error_text = '???????????? ???? ??????????????????'

            # set value about errors
            data = {'form': form, 'error_text': error_text}
            return render(request, 'account/register.html', context=data)
    else:
        form = SingUp()
    return render(request, 'account/register.html', {'form': form})


def sing_in(request):  # form authentication and loginin account
    error_text = ''
    if request.method == 'POST':
        form = LoginIn(request.POST)
        if form.is_valid():
            username = request.POST['username']  # login
            password = request.POST['password']  # password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if request.GET.get('next'):  # redirect if the user is not logged in
                    url = request.GET.get('next')
                    login(request, user)
                    return redirect(f'http://localhost:8000{url}', permanent=True)
                else:
                    login(request, user)
                    return redirect('http://localhost:8000/', permanent=True)

            else:
                error_text = '???????????????????????? ?????????? ?????? ????????????'
                data = {'form': form,
                        'error_text': error_text}
                return render(request, 'account/login.html', context=data)
    else:
        form = LoginIn()
    return render(request, 'account/login.html', {'form': form})
