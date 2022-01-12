from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news'),
    path('create', views.create_news, name='name'),
    path('<int:pk>', views.NewsDetailViews.as_view(), name='news-detail'),
]