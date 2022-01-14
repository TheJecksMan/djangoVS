from django.urls import path
from . import views


urlpatterns = [
    path('register', views.sing_up, name='register'),
    path('login', views.sing_in, name='login'),
    path('reminder', views.reminder, name='reminders'),
]
