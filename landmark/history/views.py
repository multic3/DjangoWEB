from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from history.models import Movie
from history.forms import *


class HistoryHome(ListView):
    model = Movie
    template_name = 'history/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Movie.objects.filter(is_published=True)


class HistoryAbout(ListView):
    model = Movie
    template_name = 'history/about.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О сайте'
        context['cat_selected'] = 0
        return context


class ShowPost(DetailView):
    model = Movie
    template_name = 'history/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1><p> Ошибка</p>")