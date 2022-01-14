from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginIn


def register(request):
    return render(request, 'account/register.html')


def reminder(request):
    return render(request, 'account/reminder.html')


def sing_in(request):
    error_text = ''
    if request.method == 'POST':
        form = LoginIn(request.POST)
        if form.is_valid():
            username = request.POST['username']  # login
            password = request.POST['password']  # password

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Аутентификация выполнена!')

            else:
                error_text = 'Некорректный логин или пароль'
                data = {'form': form,
                        'error_text': error_text}
                return render(request, 'account/login.html', context=data)
    else:
        form = LoginIn()
    return render(request, 'account/login.html', {'form': form})
