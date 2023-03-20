from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'description', 'image', 'video', 'created_at', 'is_published')
    list_display_link = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")



admin.site.register(Movie, HistoryAdmin)


admin.site.site_title = 'Администрирование сайта'
admin.site.site_header = 'Администрирование сайта'