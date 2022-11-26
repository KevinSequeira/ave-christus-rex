from django.shortcuts import render
import json
import pandas as pan
from datetime import datetime
import pytz
import calendar

# Create your views here.
def ordinaryform(request):

    # Get current date of processing
    currentDate = datetime.now(pytz.timezone("Australia/Adelaide")).strftime('%Y-%m-%d')

    # Load the date dimension table
    dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension")

    # Slice the date dimension table for the current date
    currentDateIndex = dateDimension.loc[dateDimension["Date"] == currentDate].index
    currentDateDimension = dateDimension.loc[dateDimension["Date"] == currentDate]
    currentDate = currentDateDimension.iloc[0]["Date"]
    currentWeekday = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
    currentQualifyingMonth = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
    currentQualifyingDay = currentDateDimension.iloc[0]["Qualifying Day"]
    currentCycle = "A, B, C"
    if (currentQualifyingDay == "Sunday"):
        currentCycle = currentDateDimension.iloc[0]["Sunday Cycle"]
    else:
        currentCycle = currentDateDimension.iloc[0]["Weekday Cycle"]
    currentYear = currentDateDimension.iloc[0]["Year"]
    currentWeek = currentDateDimension.iloc[0]["Week"]
    currentSeason = currentDateDimension.iloc[0]["Season"]

    # Get earliest feast Day
    earliestFeastDimension = dateDimension.loc[(dateDimension["Date"] >= currentDate) & (dateDimension["Feast Day"]).notna()]
    feastDate = earliestFeastDimension.iloc[0]["Date"]
    feastWeekday = datetime.strptime(earliestFeastDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
    feastQualifyingMonth = datetime.strptime(earliestFeastDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
    feastQualifyingDay = earliestFeastDimension.iloc[0]["Qualifying Day"]
    feastYear = earliestFeastDimension.iloc[0]["Year"]
    feastTitle = earliestFeastDimension.iloc[0]["Feast Day"]
    feastClass = earliestFeastDimension.iloc[0]["Feast Class"]

    # Load context variables
    context = {
        "current_date": currentDate,
        "current_weekday": currentWeekday,
        "current_qualifying_month": currentQualifyingMonth,
        "current_qualifying_day": currentQualifyingDay,
        "current_year": currentYear,
        "current_week": currentWeek,
        "current_season": currentSeason,
        "current_cycle": currentCycle,

        "feast_date": feastDate,
        "feast_weekday": feastWeekday,
        "feast_qualifying_month": feastQualifyingMonth,
        "feast_qualifying_day": feastQualifyingDay,
        "feast_year": feastYear,
        "feast_title": feastTitle,
        "feast_class": feastClass
    }

    return render(request, "ordinaryform.html", context)


def calendar(request):

    # Get current date of processing
    currentDate = datetime.now(pytz.timezone("Australia/Adelaide")).strftime('%Y-%m-%d')

    # Load the date dimension table
    dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension")

    # Slice the date dimension table for the current date
    currentDateIndex = dateDimension.loc[dateDimension["Date"] == currentDate].index
    currentDateDimension = dateDimension.loc[dateDimension["Date"] == currentDate]
    currentDate = currentDateDimension.iloc[0]["Date"]
    currentWeekday = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
    currentQualifyingMonth = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
    currentQualifyingDay = currentDateDimension.iloc[0]["Qualifying Day"]
    currentCycle = "A, B, C"
    if (currentWeekday == "Sunday"):
        currentCycle = currentDateDimension.iloc[0]["Sunday Cycle"]
    else:
        currentCycle = currentDateDimension.iloc[0]["Weekday Cycle"]
    currentYear = currentDateDimension.iloc[0]["Year"]
    currentWeek = currentDateDimension.iloc[0]["Week"]
    currentSeason = currentDateDimension.iloc[0]["Season"]
    currentSeasonShort = currentDateDimension.iloc[0]["Season Short"]

    # Get earliest feast Day
    earliestFeastDimension = dateDimension.loc[(dateDimension["Date"] >= currentDate) & (dateDimension["Feast Day"]).notna()]
    feastDate = earliestFeastDimension.iloc[0]["Date"]
    feastWeekday = datetime.strptime(earliestFeastDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
    feastQualifyingMonth = datetime.strptime(earliestFeastDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
    feastQualifyingDay = earliestFeastDimension.iloc[0]["Qualifying Day"]
    feastYear = earliestFeastDimension.iloc[0]["Year"]
    feastTitle = earliestFeastDimension.iloc[0]["Feast Day"]
    feastClass = earliestFeastDimension.iloc[0]["Feast Class"]

    # Load context variables
    context = {
        "current_date": currentDate,
        "current_weekday": currentWeekday,
        "current_qualifying_month": currentQualifyingMonth,
        "current_qualifying_day": currentQualifyingDay,
        "current_year": currentYear,
        "current_week": currentWeek,
        "current_season": currentSeason,
        "current_season_short": currentSeasonShort,
        "current_cycle": currentCycle,

        "feast_date": feastDate,
        "feast_weekday": feastWeekday,
        "feast_qualifying_month": feastQualifyingMonth,
        "feast_qualifying_day": feastQualifyingDay,
        "feast_year": feastYear,
        "feast_title": feastTitle,
        "feast_class": feastClass
    }

    context = adventCalendar(context)
    # Add season-specific context variables
    if (currentSeasonShort == "advent"):
        context = adventCalendar(context)
    elif (currentSeasonShort == "lent"):
        context = lentenCalendar(context)

    return render(request, "liturgicalcalendar.html", context)


def liturgyfortheday(request, current_date = "2022-11-27"):

    # Get the currentDate from the request URL
    currentDate = "2022-11-27"
    # Load the date dimension table
    dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension")

    # Slice the date dimension table for the current date
    currentDateIndex = dateDimension.loc[dateDimension["Date"] == currentDate].index
    currentDateDimension = dateDimension.loc[dateDimension["Date"] == currentDate]
    currentDate = currentDateDimension.iloc[0]["Date"]
    currentWeekday = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
    currentQualifyingMonth = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
    currentQualifyingDay = currentDateDimension.iloc[0]["Qualifying Day"]
    currentCycle = "A, B, C"
    print(currentWeekday)
    if (currentWeekday == "Sunday"):
        currentCycle = currentDateDimension.iloc[0]["Sunday Cycle"]
    else:
        currentCycle = currentDateDimension.iloc[0]["Weekday Cycle"]
    currentYear = currentDateDimension.iloc[0]["Year"]
    currentWeek = currentDateDimension.iloc[0]["Week"]
    currentSeason = currentDateDimension.iloc[0]["Season"]
    currentSeasonShort = currentDateDimension.iloc[0]["Season Short"]

    # Load context variables
    context = {
        "current_date": currentDate,
        "current_weekday": currentWeekday,
        "current_qualifying_month": currentQualifyingMonth,
        "current_qualifying_day": currentQualifyingDay,
        "current_year": currentYear,
        "current_week": currentWeek,
        "current_season": currentSeason,
        "current_season_short": currentSeasonShort,
        "current_cycle": currentCycle
    }

    # Add season-specific context variables
    if (currentSeasonShort == "advent"):
        context = advent(context)
    elif (currentSeasonShort == "lent"):
        context = lent(context)

    return render(request, f"{currentSeasonShort}/{currentWeekday.lower()}.html", context)


def advent(context = {}):

    jsonFile = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_week'].lower()}/{context['current_weekday'].lower()}.json")
    jsonFile = json.load(jsonFile)

    commonPrayers = open(f"./static/documents/ordinaryform/commonprayers.json")
    commonPrayers = json.load(commonPrayers)

    gloria_content = ""
    if (jsonFile["gloria"] == "yes"):
        gloria_content = commonPrayers["gloria"]

    credo_content = ""
    if (jsonFile["credo"] == "apostles_creed"):
        credo_content = commonPrayers["apostles_creed"]
    elif (jsonFile["credo"] == "nicene_creed"):
        credo_content = commonPrayers["nicene_creed"]

    context["opening_antiphon"] = jsonFile["opening_antiphon"]
    context["gloria"] = jsonFile["gloria"]
    context["gloria_content"] = gloria_content
    context["collect"] = jsonFile["collect"]
    context["first_reading"] = jsonFile["year_a"]["first_reading"]
    context["responsorial_psalm"] = jsonFile["year_a"]["responsorial_psalm"]
    context["second_reading"] = jsonFile["year_a"]["second_reading"]
    context["gospel_acclamation"] = jsonFile["year_a"]["gospel_acclamation"]
    context["gospel_reading"] = jsonFile["year_a"]["gospel_reading"]
    context["offertory"] = jsonFile["offertory"]
    context["credo"] = jsonFile["credo"]
    context["credo_content"] = credo_content
    context["communion_antiphon"] = jsonFile["communion_antiphon"]
    context["prayer_after_communion"] = jsonFile["prayer_after_communion"]

    return context


def adventCalendar(context = {}):

    # print(context)
    # Load the date dimension table
    dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension").fillna("")

    # Get all days for the current liturgical season
    currentSeasonCalendar = dateDimension.loc[dateDimension["Season Short"] == "advent"]
    currentSeasonCalendar["Qualifying Month"] = currentSeasonCalendar["Month"].apply(lambda row: datetime.strptime(str(row), "%m").strftime("%B"))
    currentSeasonCalendar["Qualifying Weekday"] = currentSeasonCalendar["Date"].apply(lambda row: datetime.strptime(str(row), "%Y-%m-%d").strftime("%A"))

    # Get unique months for the current Season
    # monthsInTheSeason = currentSeasonCalendar["Date"].apply(lambda string: datetime.strptime(string, '%Y-%m-%d').strftime('%m')).unique()
    monthsInTheSeason = currentSeasonCalendar["Month"].unique().tolist()

    calendarDictionary = {}
    # Get data for each day for each month in the Season
    for month in monthsInTheSeason:
        calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")] = []
        tempDataFrame = currentSeasonCalendar.loc[currentSeasonCalendar["Month"] == month]
        for index, row in tempDataFrame.iterrows():
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")].append(row[["Date", "Qualifying Day", "Season", "Qualifying Weekday", "Week", "Feast Day", "Feast Class"]].tolist())

    context["calendar_dictionary"] = calendarDictionary.items()
    return context
