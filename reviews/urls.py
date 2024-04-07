from django.urls import path
from . import views

urlpatterns = [
    path('review_upload/', views.review_upload, name='review-upload'),
]