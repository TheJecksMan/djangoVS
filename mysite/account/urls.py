from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.sing_in, name='login'),
    #path('login', views.login, name='login'),
    path('reminder', views.reminder, name='reminders'),
]
