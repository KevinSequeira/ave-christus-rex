from django.shortcuts import render
from .modules.prayers import prayerdictionary

# Create your views here.
def prayers(request):
    context = {}
    return render(request, "prayers.html", context)

def simpleprayers(request):
    context = {}
    return render(request, "simpleprayers.html", context)

def essentialPrayers(request):
    context = {}
    return render(request, "essentialPrayers.html", context)

def prayerDetails(request, page_alias = "this"):
    context = {
        page_alias: "in-nomine-patris",
        "prayer_dictionary": prayerdictionary()
    }
    prayerPages = {
        "in-nomine-patris": "signumCrucis.html",
        "pater-noster": "paterNoster.html"
    }
    return render(request, prayerPages[page_alias], context)
