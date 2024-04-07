from django.urls import path
from . import views

urlpatterns = [
    path('book-order/', views.book_order, name='book-order'),
]