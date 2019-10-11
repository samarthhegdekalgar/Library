from django.contrib import admin
from .models import Book, Author


# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'price', 'author_name', )
    list_filter = ('available', )
    search_fields = ['book_name', ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
