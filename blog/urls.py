# thepensiveDjango/thepensive_django/blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('public_journal/', views.public_journal, name='public_journal'),
    path('create_blog_post/', views.create_blog_post, name='create_blog_post'),
    path('about/', views.about, name='about'),
    path('featured/', views.featured, name='featured'),  # Added Featured URL
]