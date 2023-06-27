from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class post(models.Model):
    blog_title = models.CharField(max_length = 256)
    blog_subtitle = models.CharField(max_length = 4800)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog_description = HTMLField()
    blog_tag = models.CharField(max_length = 128)