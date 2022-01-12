from django.db import models
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.detail import DetailView
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DeleteView



def news_home (request):
    news = Articles.objects.order_by('-date')
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
