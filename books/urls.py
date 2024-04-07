from django.urls import path
from . import views

urlpatterns = [
    path('book_upload/', views.book_upload, name='book-upload'),
    path('book_list/', views.book_list, name='book-list'),
    path('book_detail/<int:pk>/', views.book_detail, name='book-detail'),
    path('book_search/', views.book_search, name='book-search'),
]