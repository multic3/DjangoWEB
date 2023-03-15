from django.contrib.auth import login
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *


urlpatterns = [
    path('', cache_page(60)(HistoryHome.as_view()), name='home'),
    path('about/', cache_page(60)(HistoryAbout.as_view()), name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
]