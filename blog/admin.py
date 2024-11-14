# thepensiveDjango/thepensive_django/blog/admin.py

from django.contrib import admin
from .models import BlogPost, Comment
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'featured', 'public_journal', 'created_at', 'published_at']
    list_filter = ['featured', 'public_journal', 'author']
    search_fields = ['title', 'content']
    fields = ['title', 'content', 'author', 'featured', 'public_journal', 'image', 'published_at']


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)