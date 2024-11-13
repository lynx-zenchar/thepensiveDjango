# thepensiveDjango/thepensive_django/blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, CommentForm
from django.contrib import messages

def home(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    comments = blog.comments.all()
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'comments': comments})

def public_journal(request):
    posts = BlogPost.objects.filter(public_journal=True)
    return render(request, 'blog/public_journal.html', {'posts': posts})

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            messages.success(request, "Blog post created successfully!")
            return redirect('blog_detail', blog_id=blog_post.id)
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

def about(request):
    return render(request, 'blog/about.html')

def featured(request):
    featured_posts = BlogPost.objects.filter(featured=True).order_by('-created_at')
    return render(request, 'blog/featured.html', {'featured_posts': featured_posts})