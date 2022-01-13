from django.shortcuts import render


def register(request):
    return render(request, 'account/register.html')


def login(request):
    return render(request, 'account/login.html')


def reminder(request):
    return render(request, 'account/reminder.html')
