from django.shortcuts import render
from .modules.prayers import prayerdictionary
import sqlite3

# Create your views here.
def prayers(request):
    context = {}
    return render(request, "prayers.html", context)

def prayerCategory(request, prayer_category_tag = ""):
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    print(prayer_category_tag)
    sqlite_select_Query = f"SELECT * FROM [prayers_content] WHERE [prayer_category_tag] = '{prayer_category_tag}';"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    cursor.close()
    context = {
        "prayerCategory": record[0][1],
        "prayers": record
    }
    return render(request, "allPrayersInACategory.html", context)

def prayerDetails(request, prayer_category_tag = "", prayer_name_tag = ""):
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = f"SELECT * FROM [prayers_detail] WHERE [prayer_category_tag] = '{prayer_category_tag}' AND [prayer_name_tag] = '{prayer_name_tag}';"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchone()
    print(prayer_category_tag, "  lol  ", prayer_name_tag)
    cursor.close()
    context = {
        "prayerCategory": record[4],
        "prayerDetail": record
    }
    return render(request, "allPrayerDetails.html", context)

def essentialPrayers(request):
    context = {}
    return render(request, "essentialPrayers.html", context)
