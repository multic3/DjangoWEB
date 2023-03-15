from django.contrib.auth import login
from django.urls import path
from .views import *


urlpatterns = [
    path('', HistoryHome.as_view(), name='home'),
    path('about/', HistoryAbout.as_view(), name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
]