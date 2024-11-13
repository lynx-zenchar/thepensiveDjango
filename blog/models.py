# thepensiveDjango/thepensive_django/blog/models.py

from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField  # Add this import

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    public_journal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # Add this field

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.blog_post.title}'