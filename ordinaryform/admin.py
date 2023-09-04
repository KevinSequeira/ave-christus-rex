from django.contrib import admin
from ordinaryform.models import OrdinaryTimePrayer, OrdinaryTimeReading, AdventPrayer, AdventReading

# Register your models here.

class ordinaryTimePrayer(admin.ModelAdmin):
    list_display = ('liturgical_year', 'liturgical_season', 'week_number',
        'introit', 'collect', 'offertory', 'communion_antiphon', 'postcommunion', 'conclusion', 'background')

class ordinaryTimeReading(admin.ModelAdmin):
    list_display = ('liturgical_year', 'liturgical_season', 'week_number',
        'first_reading', 'psalm', 'second_reading', 'gospel_acclamation', 'gospel')

class adventPrayer(admin.ModelAdmin):
    list_display = ('liturgical_year', 'liturgical_season', 'week_number',
        'introit', 'collect', 'offertory', 'communion_antiphon', 'postcommunion', 'conclusion', 'background')

class adventReading(admin.ModelAdmin):
    list_display = ('liturgical_year', 'liturgical_season', 'week_number',
        'first_reading', 'psalm', 'second_reading', 'gospel_acclamation', 'gospel')

admin.site.register(OrdinaryTimePrayer, ordinaryTimePrayer)
admin.site.register(OrdinaryTimeReading, ordinaryTimeReading)
admin.site.register(AdventPrayer, adventPrayer)
admin.site.register(AdventReading, adventReading)