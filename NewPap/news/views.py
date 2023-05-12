# from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
