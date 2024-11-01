from django.contrib import admin

from .models import Author, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'quantity',)
    list_display = (
        'title',
        'author',
        'quantity',
    )
    list_filter = ('author',)
    search_fields = ('title', 'author__name')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
