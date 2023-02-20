from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    location = models.TextField(max_length=255, default=True, verbose_name='Адрес')
    image = models.ImageField(upload_to='images/%Y/%m',verbose_name='Изображение')
    video = models.FileField(upload_to='videos//%Y/%m', verbose_name='Видео')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Достопримечательности'
        verbose_name_plural = 'Достопримечательности'
        ordering = ['title', 'created_at']


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    paid = models.BooleanField(default=True)


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
