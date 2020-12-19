from datetime import datetime

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Author, Genre, Book
# Register your models here.


class AuthorAdmin(ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'first_name', 'last_name']
    list_per_page = 20
    search_fields = ['last_name']
    list_display_links = ['id', 'first_name', 'last_name']


class BookAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (
            'External Information',
            {
                'fields': ['author', 'genre', 'publication_date'],
                'description': (
                    'These fields are going to be filled with data parsed '
                    'from external databases.'
                )
            }
        ),
        (
            'User Information',
            {
                'fields': ['rating', 'description'],
                'description': 'These fields are intended to be filled in by our users.'
            }
        )
    ]

    @staticmethod
    def publication_year(obj):
        return obj.publication_date.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    @staticmethod
    def new_publication_date(modeladmin, request, queryset):
        queryset.update(publication_date=datetime.now())

    ordering = ['id']
    list_display = ['id', 'title', 'author', 'genre', 'publication_year']
    list_display_links = ['id', 'title']
    list_per_page = 20
    list_filter = ['author', 'genre']
    search_fields = ['title']
    actions = ['cleanup_description', 'new_publication_date']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)