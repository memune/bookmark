from django.contrib import admin

# Register your models here.

from .models import Bookmark, Category


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'author', 'created', 'updated']

admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Category)