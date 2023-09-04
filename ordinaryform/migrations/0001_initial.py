# Generated by Django 3.1.6 on 2023-09-04 13:37

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdventPrayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liturgical_year', models.CharField(max_length=128)),
                ('liturgical_season', models.CharField(max_length=256)),
                ('week_number', models.CharField(max_length=128)),
                ('introit', tinymce.models.HTMLField()),
                ('collect', tinymce.models.HTMLField()),
                ('offertory', tinymce.models.HTMLField()),
                ('communion_antiphon', tinymce.models.HTMLField()),
                ('postcommunion', tinymce.models.HTMLField()),
                ('conclusion', tinymce.models.HTMLField()),
                ('background', models.CharField(max_length=512)),
                ('week_colour', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='AdventReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liturgical_year', models.CharField(max_length=128)),
                ('liturgical_season', models.CharField(max_length=256)),
                ('week_number', models.CharField(max_length=128)),
                ('week_day', models.CharField(max_length=128)),
                ('first_reading', tinymce.models.HTMLField()),
                ('psalm', tinymce.models.HTMLField()),
                ('second_reading', tinymce.models.HTMLField()),
                ('gospel_acclamation', tinymce.models.HTMLField()),
                ('gospel', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='OrdinaryTimePrayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liturgical_year', models.CharField(max_length=128)),
                ('liturgical_season', models.CharField(max_length=256)),
                ('week_number', models.CharField(max_length=128)),
                ('introit', tinymce.models.HTMLField()),
                ('collect', tinymce.models.HTMLField()),
                ('offertory', tinymce.models.HTMLField()),
                ('communion_antiphon', tinymce.models.HTMLField()),
                ('postcommunion', tinymce.models.HTMLField()),
                ('conclusion', tinymce.models.HTMLField()),
                ('background', models.CharField(max_length=512)),
                ('week_colour', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='OrdinaryTimeReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liturgical_year', models.CharField(max_length=128)),
                ('liturgical_season', models.CharField(max_length=256)),
                ('week_number', models.CharField(max_length=128)),
                ('week_day', models.CharField(max_length=128)),
                ('first_reading', tinymce.models.HTMLField()),
                ('psalm', tinymce.models.HTMLField()),
                ('second_reading', tinymce.models.HTMLField()),
                ('gospel_acclamation', tinymce.models.HTMLField()),
                ('gospel', tinymce.models.HTMLField()),
            ],
        ),
    ]
