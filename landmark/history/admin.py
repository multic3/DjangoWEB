from django.contrib import admin
from .models import *
# Register your models here.


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'description', 'image', 'video', 'created_at', 'is_published')
    list_display_link = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Movie, HistoryAdmin)