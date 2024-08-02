from django.contrib import admin
from .models import Book
from .models import Author
from .models import Borrowing

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_id', 'first_name', 'last_name', 'email', 'phone']
    list_filter = ['first_name']
    search_fields = ['author_id', 'first_name']
    raw_id_fields = ['user']
    ordering = ['author_id']
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['isbn', 'title', 'publisher', 'date_of_publish', 'quantity']
    list_filter = ['publisher']
    search_fields = ['title', 'isbn']
    raw_id_fields = ['authors']
    date_hierarchy = 'date_of_publish'
    ordering = ['publisher', 'date_of_publish']
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Borrowing)
class BorrwingAdmin(admin.ModelAdmin):
    list_display = ['student', 'book', 'borrow_date', 'return_date', 'returned']
    list_filter = ['returned']
    search_fields = ['student', 'book']
    raw_id_fields = ['book','student']
    date_hierarchy = 'borrow_date'
    ordering = ['borrow_date', 'returned']
    show_facets = admin.ShowFacets.ALWAYS