# thepensiveDjango/thepensive_django/blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('featured/', views.featured, name='featured'),  # Featured page
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),  # Blog detail
    path('public_journal/', views.public_journal, name='public_journal'),  # Public Journal
    path('create_blog_post/', views.create_blog_post, name='create_blog_post'),  # Create Blog Post
    # Add other URL patterns as needed
]