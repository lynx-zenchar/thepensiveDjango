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
    form = BlogPostAdminForm
    list_display = ('title', 'author', 'featured', 'public_journal', 'created_at')
    list_filter = ('featured', 'public_journal', 'created_at')
    search_fields = ('title', 'content', 'author__username')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)