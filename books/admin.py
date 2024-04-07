from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'cover')

admin.site.register(Book, BookAdmin)
# Register your models here.
