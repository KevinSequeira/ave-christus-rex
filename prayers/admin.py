from django.contrib import admin
from prayers.models import content, detail, category

# Register your models here.

class prayerAdmin(admin.ModelAdmin):
    list_display = ('prayer_name', 'prayer_category', 'prayer_to', 'prayer_type',
        'prayer_description', 'prayer_attributed_to', 'prayer_content',
        'prayer_category_tag', 'prayer_name_tag')

class prayerDetails(admin.ModelAdmin):
    list_display = ('prayer_name', 'prayer_description', 'prayer_content', 'prayer_article',
        'prayer_category_tag', 'prayer_name_tag', 'prayer_image')

class prayerCategory(admin.ModelAdmin):
    list_display = ('prayer_category', 'prayer_category_tag', 'prayer_category_tagline')

admin.site.register(content, prayerAdmin)
admin.site.register(detail, prayerDetails)
admin.site.register(category, prayerCategory)