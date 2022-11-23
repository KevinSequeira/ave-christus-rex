from django.shortcuts import render
import json
import pandas as pan
from datetime import datetime

# Create your views here.
def ordinaryform(request):

    # Get current date of processing
    currentDate = datetime.today().strftime('%Y-%m-%d')

    # Load the date dimension table
    dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension")

    # Slice the date dimension table for the current date
    currentDateIndex = dateDimension.loc[dateDimension["Date"] == currentDate].index
    currentDateDimension = dateDimension.loc[dateDimension["Date"] == currentDate]
    currentDate = currentDateDimension.iloc[0]["Date"]
    currentWeekday = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
    currentQualifyingMonth = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
    currentQualifyingDay = currentDateDimension.iloc[0]["Qualifying Day"]
    currentYear = currentDateDimension.iloc[0]["Year"]
    currentWeek = currentDateDimension.iloc[0]["Week"]
    currentSeason = currentDateDimension.iloc[0]["Season"]

    # Load context variables
    context = {
        "current_date": currentDate,
        "current_weekday": currentWeekday,
        "current_qualifying_month": currentQualifyingMonth,
        "current_qualifying_day": currentQualifyingDay,
        "current_year": currentYear,
        "current_week": currentWeek,
        "current_season": currentSeason
    }
    print(context)

    return render(request, "ordinaryform.html", context)

def advent(request):
    context = {}
    return render(request, "firstSunday.html", context)

def advent(request, week_number = "01", week_day = "sunday"):

    jsonFile = open(f"./static/documents/ordinaryform/advent/adventprayers.json")
    jsonFile = json.load(jsonFile)

    commonPrayers = open(f"./static/documents/ordinaryform/commonPrayers.json")
    commonPrayers = json.load(commonPrayers)

    gloria_content = ""
    if (jsonFile["advent"][week_number][week_day]["gloria"] == "yes"):
        gloria_content = commonPrayers["gloria"]

    credo_content = ""
    if (jsonFile["advent"][week_number][week_day]["credo"] == "apostles_creed"):
        credo_content = commonPrayers["apostles_creed"]
    elif (jsonFile["advent"][week_number][week_day]["credo"] == "nicene_creed"):
        credo_content = commonPrayers["nicene_creed"]

    context = {
        "opening_antiphon": jsonFile["advent"][week_number][week_day]["opening_antiphon"],
        "gloria": jsonFile["advent"][week_number][week_day]["gloria"],
        "gloria_content": gloria_content,
        "collect": jsonFile["advent"][week_number][week_day]["collect"],
        "offetory": jsonFile["advent"][week_number][week_day]["offetory"],
        "credo": jsonFile["advent"][week_number][week_day]["credo"],
        "credo_content": credo_content,
    }
    return render(request, f"advent/{week_number}/{week_day}.html", context)
