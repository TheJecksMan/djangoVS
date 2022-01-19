from django.urls import path
from . import views


urlpatterns = [
    path('', views.news, name='news'),
    path('create', views.create_news, name='create'),
    path('post/<int:pk>', views.NewsDetailViews.as_view(), name='news-detail'),
]
