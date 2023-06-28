from django.shortcuts import render
import datetime

from django.views import View
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.paginator import Paginator



class simpleView(View):
    def get(self, request):
        post = Post.objects.order_by('-id')
        p = Paginator(post, 1)

        post = p.get_page(request.GRT.get('page', 1))

        data = {
            'post': post
        }
        return render(request, 'templates/item.html', data)


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 1


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'result'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10
def get_queryset(self):
    return Post.objects.filter()
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['d'] = self.request.Get.get('d')
    context['t'] = self.request.Get.get('t')
    context['a'] = self.request.Get.get('a')
    return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'item.html'
    context_object_name = 'post'


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['time_now'] = datetime.UTC
    context['value'] = None
    return context
