from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('book', 'author', 'review', 'rating')

admin.site.register(Review, ReviewAdmin)

# Register your models here.
