from django.urls import path
from .views import *


urlpatterns = [
    path('', HistoryHome.as_view(), name='home'),
    path('about/', HistoryAbout.as_view(), name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
]