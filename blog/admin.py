from django.contrib import admin
from blog.models import post

# Register your models here.

class blogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_subtitle', 'created_at', 'updated_at',
        'blog_description', 'blog_tag')

admin.site.register(post, blogAdmin)