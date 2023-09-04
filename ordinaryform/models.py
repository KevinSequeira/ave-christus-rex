from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class OrdinaryTimePrayer(models.Model):
    liturgical_year = models.CharField(max_length = 128)
    liturgical_season = models.CharField(max_length = 256)
    week_number = models.CharField(max_length = 128)
    introit = HTMLField()
    collect = HTMLField()
    offertory = HTMLField()
    communion_antiphon = HTMLField()
    postcommunion = HTMLField()
    conclusion = HTMLField()
    background = models.CharField(max_length = 512)
    week_colour = models.CharField(max_length = 128)

class OrdinaryTimeReading(models.Model):
    liturgical_year = models.CharField(max_length = 128)
    liturgical_season = models.CharField(max_length = 256)
    week_number = models.CharField(max_length = 128)
    week_day = models.CharField(max_length = 128)
    first_reading = HTMLField()
    psalm = HTMLField()
    second_reading =  HTMLField()
    gospel_acclamation = HTMLField()
    gospel = HTMLField()

class AdventPrayer(models.Model):
    liturgical_year = models.CharField(max_length = 128)
    liturgical_season = models.CharField(max_length = 256)
    week_number = models.CharField(max_length = 128)
    introit = HTMLField()
    collect = HTMLField()
    offertory = HTMLField()
    communion_antiphon = HTMLField()
    postcommunion = HTMLField()
    conclusion = HTMLField()
    background = models.CharField(max_length = 512)
    week_colour = models.CharField(max_length = 128)

class AdventReading(models.Model):
    liturgical_year = models.CharField(max_length = 128)
    liturgical_season = models.CharField(max_length = 256)
    week_number = models.CharField(max_length = 128)
    week_day = models.CharField(max_length = 128)
    first_reading = HTMLField()
    psalm = HTMLField()
    second_reading =  HTMLField()
    gospel_acclamation = HTMLField()
    gospel = HTMLField()