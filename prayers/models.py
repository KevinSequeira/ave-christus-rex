from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class content(models.Model):
    prayer_name = models.CharField(max_length = 1248)
    prayer_category = models.CharField(max_length = 256)
    prayer_to = models.CharField(max_length = 256)
    prayer_type = models.CharField(max_length = 128)
    prayer_description = models.CharField(max_length = 4800)
    prayer_attributed_to = models.CharField(max_length = 256)
    prayer_content = HTMLField()
    prayer_category_tag = models.CharField(max_length = 256)
    prayer_name_tag = models.CharField(max_length = 256)

class detail(models.Model):
    prayer_name = models.CharField(max_length = 1248)
    prayer_description = models.CharField(max_length = 4800)
    prayer_content = HTMLField()
    prayer_article = HTMLField()
    prayer_category_tag = models.CharField(max_length = 256)
    prayer_name_tag = models.CharField(max_length = 256)
    prayer_image = models.CharField(max_length = 256)