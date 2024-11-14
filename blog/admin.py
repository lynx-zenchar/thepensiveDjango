# thepensiveDjango/thepensive_django/blog/admin.py

from django.contrib import admin
from .models import BlogPost, Comment, About
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
    form = BlogPostAdminForm  # Ensure the custom form is used

class AboutAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email_primary', 'email_secondary')
    fields = ('image', 'bio', 'email_primary', 'email_secondary')
    readonly_fields = ()

    def has_add_permission(self, request):
        # Allow only one About instance
        if About.objects.exists():
            return False
        return True

# Register models with their respective admin classes
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)
admin.site.register(About, AboutAdmin)  # Associate AboutAdmin with About model