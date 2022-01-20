from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register', views.sing_up, name='register'),
    path('login', views.sing_in, name='login'),
    path('reminder', views.reminder, name='reminders'),
    path('activate/', views.activate_account, name='activate'),
    path('setting/profile', views.profile_account, name='profile'),
    path('logout', auth_views.logout_then_login, name='logout'),
]
