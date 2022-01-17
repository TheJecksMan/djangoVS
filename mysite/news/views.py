from django.db import models
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Articles
from .forms import ArticlesForm
from django.core.paginator import Paginator


def news(request):
    news = Articles.objects.order_by('date').reverse
    # news_paginator = Paginator(news, 5)
    # context = {
    #     'count': news_paginator.count,
    #     'news': news
    # }
    return render(request, 'news/news.html', {'news': news})


class NewsDetailViews(DetailView):
    model = Articles
    template_name = 'news/details_views.html'
    context_object_name = 'article'


def create_news(request):
    error_text = 'Форма была некорректной'
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error_text

    form = ArticlesForm()
    data = {
        'form': form,
        'error_text': error_text
    }
    return render(request, 'news/create.html', data)
