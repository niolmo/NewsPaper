# from django.shortcuts import render
import datetime

from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['time_now'] = datetime.UTC
    context['value'] = None
    return context
