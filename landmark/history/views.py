from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from history.models import Movie
from history.forms import *
from history.utils import *


class HistoryHome(DataMixin, ListView):
    paginate_by = 2
    model = Movie
    template_name = 'history/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        # context['cat_selected'] = 0
        c_def = self.get_user_context(title='Главная страница')
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


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'history/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'history/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1><p> Ошибка</p>")