# thepensiveDjango/thepensive_django/blog/forms.py

from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    published_at = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'featured', 'public_journal', 'image', 'published_at']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }