from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from history.models import Movie as M


def index(request):
    posts = M.objects.all()
    context = {'posts': posts,
               'title': 'Главная страница'
    }
    return render(request, 'history/index.html', context=context)


def about(request):
    context = {'title': 'О нас',
    }
    return render(request, 'history/about.html', context=context)


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи {post_id}')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1><p> Ошибка</p>")