from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News, Category, Tag


class HomeView(ListView):
    model = News
    template_name = 'blog/index.html'
    context_object_name = 'news'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Blog news'
        return context


class NewsByCategoryView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'news'
    paginate_by = 4

    def get_queryset(self):
        return News.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class NewsView(DetailView):
    model = News
    template_name = 'blog/news.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NewsByTagView(ListView):
    pass
