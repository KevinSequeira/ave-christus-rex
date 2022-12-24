from django.shortcuts import render
import json
import pandas as pan
from datetime import datetime, timedelta
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
    currentCycle = currentDateDimension.iloc[0]["Year Cycle"]
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
    feastShort = earliestFeastDimension.iloc[0]["Feast Short"]

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
        "feast_class": feastClass,
        "st_short_name": feastShort
    }

    if (currentSeasonShort == "advent"):
        context = adventloader(context)
    elif (currentSeasonShort == "christmas"):
        context = christmasloader(context)
    context = memorialloader(context)

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
    previousWeekday = (datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d') - timedelta(days = 1)).strftime('%A')
    currentQualifyingMonth = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
    currentQualifyingDay = currentDateDimension.iloc[0]["Qualifying Day"]
    currentCycle = "A, B, C"
    currentCycle = currentDateDimension.iloc[0]["Year Cycle"]
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
    saintShortName = earliestFeastDimension.iloc[0]["Feast Short"]

    # Load context variables
    context = {
        "current_date": currentDate,
        "current_weekday": currentWeekday,
        "previous_weekday": previousWeekday,
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
        "feast_class": feastClass,
        "st_short_name": saintShortName
    }

    if (currentSeasonShort == "advent"):
        context = adventloader(context)
    elif (currentSeasonShort == "christmas"):
        context = christmasloader(context)
    context = adventcalendar(context)
    context = christmascalendar(context)
    context = memorialloader(context)

    return render(request, "liturgicalcalendar.html", context)


def liturgyfortheday(request, current_date = "2022-11-27"):

    # Get the currentDate from the request URL
    currentDate = current_date
    if (currentDate in ['easter-vigil',
        'easter-midnight',
        'easter-dawn',
        'easter-daytime']):
        context = {
            "liturgy": currentDate
        }
        context = easterliturgies(context)
        return render(request, f"christmas/sunday.html", context)

    # Load the date dimension table
    dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension")

    # Slice the date dimension table for the current date
    currentDateIndex = dateDimension.loc[dateDimension["Date"] == currentDate].index
    currentDateDimension = dateDimension.loc[dateDimension["Date"] == currentDate]
    currentDate = currentDateDimension.iloc[0]["Date"]
    previousDate = str(datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d') - timedelta(days = 1))[0:10]
    currentWeekday = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
    previousWeekday = (datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d') - timedelta(days = 1)).strftime('%A')
    currentQualifyingMonth = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
    currentQualifyingDay = currentDateDimension.iloc[0]["Qualifying Day"]
    currentCycle = "A, B, C"
    currentCycle = currentDateDimension.iloc[0]["Year Cycle"]
    currentYear = currentDateDimension.iloc[0]["Year"]
    currentWeek = currentDateDimension.iloc[0]["Week"]
    currentSeason = currentDateDimension.iloc[0]["Season"]
    currentSeasonShort = currentDateDimension.iloc[0]["Season Short"]
    currentDateImage = currentDateDimension.iloc[0]["Liturgy Image Location"]

    # Load context variables
    context = {
        "current_date": currentDate,
        "current_weekday": currentWeekday,
        "previous_weekday": previousWeekday,
        "current_qualifying_month": currentQualifyingMonth,
        "current_qualifying_day": currentQualifyingDay,
        "current_year": currentYear,
        "current_week": currentWeek,
        "current_season": currentSeason,
        "current_season_short": currentSeasonShort,
        "current_cycle": currentCycle,
        "current_date_image": currentDateImage
    }

    if ((currentQualifyingMonth == "December")
        & (currentQualifyingDay == "25th")):
        context = christmasdayoptions(context)
        return render(request, f"christmas/christmasdayliturgies.html", context)

    # Add season-specific context variables
    if (currentSeasonShort == "advent"):
        context = advent(context)
    elif (currentSeasonShort == "lent"):
        context = lent(context)

    templateFileName = "sunday"
    if (currentWeekday == "Sunday"):
        templateFileName = "sunday"
    else:
        templateFileName = "weekday"

    return render(request, f"{currentSeasonShort}/{templateFileName}.html", context)


def adventloader(context = {}):

    context = context
    try:
        jsonFile = ""
        if ((context["current_qualifying_day"] > '16th')
            & (context["current_qualifying_month"] == 'December')
            & (context["current_weekday"] != 'Sunday')):
            jsonFile = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_qualifying_day'].lower()}.json")
        else:
            jsonFile = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_week'].lower()}/{context['current_weekday'].lower()}.json")
        jsonFile = json.load(jsonFile)
        context["liturgy_background_image"] = jsonFile["liturgy_background_image"]

    except:
        context["file_available"] = "no"
        context["liturgy_background_image"] = ""

    return context


def advent(context = {}):

    try:
        jsonFile = ""
        if ((context["current_qualifying_day"] > '16th')
            & (context["current_qualifying_month"] == 'December')
            & (context["current_weekday"] != 'Sunday')):
            jsonFile = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_qualifying_day'].lower()}.json")
        else:
            jsonFile = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_week'].lower()}/{context['current_weekday'].lower()}.json")
        jsonFile = json.load(jsonFile)

        commonPrayers = open(f"./static/documents/ordinaryform/commonprayers.json")
        commonPrayers = json.load(commonPrayers)

        context["liturgy_background_image"] = jsonFile["liturgy_background_image"]

        gloria_content = ""
        if (jsonFile["gloria"] == "yes"):
            gloria_content = commonPrayers["gloria"]

        credo_content = ""
        if (jsonFile["credo"] == "apostles_creed"):
            credo_content = commonPrayers["apostles_creed"]
        elif (jsonFile["credo"] == "nicene_creed"):
            credo_content = commonPrayers["nicene_creed"]

        context["file_available"] = "yes"

        context["opening_antiphon"] = jsonFile["opening_antiphon"]
        context["gloria"] = jsonFile["gloria"]
        context["gloria_content"] = gloria_content
        context["collect"] = jsonFile["collect"]
        context["first_reading"] = jsonFile["year_a"]["first_reading"]
        context["responsorial_psalm"] = jsonFile["year_a"]["responsorial_psalm"]

        second_reading_content = ""
        if ("second_reading" in jsonFile["year_a"]):
            context["second_reading"] = jsonFile["year_a"]["second_reading"]

        context["gospel_acclamation"] = jsonFile["year_a"]["gospel_acclamation"]
        context["gospel_reading"] = jsonFile["year_a"]["gospel_reading"]
        context["offertory"] = jsonFile["offertory"]
        context["credo"] = jsonFile["credo"]
        context["credo_content"] = credo_content
        context["communion_antiphon"] = jsonFile["communion_antiphon"]
        context["prayer_after_communion"] = jsonFile["prayer_after_communion"]
    except:
        context["file_available"] = "no"

        context["opening_antiphon"] = ""
        context["gloria"] = ""
        context["gloria_content"] = ""
        context["collect"] = ""
        context["first_reading"] = ""
        context["responsorial_psalm"] = ""
        context["second_reading"] = ""
        context["gospel_acclamation"] = ""
        context["gospel_reading"] = ""
        context["offertory"] = ""
        context["credo"] = ""
        context["credo_content"] = ""
        context["communion_antiphon"] = ""
        context["prayer_after_communion"] = ""

    return context


def adventcalendar(context = {}):

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
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")].append(row[["Date", "Qualifying Day", "Season", "Qualifying Weekday", "Week", "Feast Day", "Feast Class", "Feast Short", "Season Short"]].tolist())

    context["calendar_dictionary"] = calendarDictionary
    return context


def christmasloader(context = {}):

    try:
        jsonFile = ""
        if (context["current_qualifying_month"] == "December"):
            if (context["current_qualifying_day"] == "25th"):
                jsonFile = open(f"./static/documents/ordinaryform/christmas/december/christmas.json")
                jsonFile = json.load(jsonFile)
                context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
            elif (context["current_qualifying_day"] == "26th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-family.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/st-stephen-protomartyr.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
            elif (context["current_qualifying_day"] == "27th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-family.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/st-john-baptist.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
            elif (context["current_qualifying_day"] == "28th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-family.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-innocents.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
            elif (context["current_qualifying_day"] == "29th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-family.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/christmas-fifth-day.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
            elif (context["current_qualifying_day"] == "30th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-family.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/christmas-sixth-day.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
            elif (context["current_qualifying_day"] == "31st"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-family.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/christmas-seventh-day.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]

    except:
        context["file_available"] = "no"

        context["liturgy_background_image"] = ""

    return context


def christmasdayoptions(context = {}):

    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/christmas-options.json")
    jsonFile = json.load(jsonFile)

    context["christmas_vigil_image"] = jsonFile["christmas_vigil"]["feast_background_image"]
    context["christmas_vigil_position"] = jsonFile["christmas_vigil"]["feast_image_position"]
    context["christmas_midnight_image"] = jsonFile["christmas_midnight"]["feast_background_image"]
    context["christmas_midnight_position"] = jsonFile["christmas_midnight"]["feast_image_position"]
    context["christmas_dawn_image"] = jsonFile["christmas_dawn"]["feast_background_image"]
    context["christmas_dawn_position"] = jsonFile["christmas_dawn"]["feast_image_position"]
    context["christmas_daytime_image"] = jsonFile["christmas_daytime"]["feast_background_image"]
    context["christmas_daytime_position"] = jsonFile["christmas_daytime"]["feast_image_position"]

    return context

def christmas(context = {}):

    try:
        jsonFile = ""
        if (context["current_qualifying_month"] == "December"):
            if (context["current_qualifying_day"] == "25th"):
                jsonFile = open(f"./static/documents/ordinaryform/christmas/december/christmas-midnight.json")
            elif (context["current_qualifying_day"] == "26th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-family.json")
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/st-stephen-protomartyr.json")
            elif (context["current_qualifying_day"] == "27th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-family.json")
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/st-john-baptist.json")
            elif (context["current_qualifying_day"] == "28th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-family.json")
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-innocents.json")
            elif (context["current_qualifying_day"] == "29th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-family.json")
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/christmas-fifth-day.json")
            elif (context["current_qualifying_day"] == "30th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-family.json")
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/christmas-sixth-day.json")
            elif (context["current_qualifying_day"] == "31st"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-family.json")
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/christmas-seventh-day.json")
        jsonFile = json.load(jsonFile)

        commonPrayers = open(f"./static/documents/ordinaryform/commonprayers.json")
        commonPrayers = json.load(commonPrayers)

        context["liturgy_background_image"] = jsonFile["liturgy_background_image"]

        gloria_content = ""
        if (jsonFile["gloria"] == "yes"):
            gloria_content = commonPrayers["gloria"]

        credo_content = ""
        if (jsonFile["credo"] == "apostles_creed"):
            credo_content = commonPrayers["apostles_creed"]
        elif (jsonFile["credo"] == "nicene_creed"):
            credo_content = commonPrayers["nicene_creed"]

        context["file_available"] = "yes"

        context["opening_antiphon"] = jsonFile["opening_antiphon"]
        context["gloria"] = jsonFile["gloria"]
        context["gloria_content"] = gloria_content
        context["collect"] = jsonFile["collect"]
        context["first_reading"] = jsonFile["year_a"]["first_reading"]
        context["first_responsorial_psalm"] = jsonFile["year_a"]["first_responsorial_psalm"]

        second_reading_content = ""
        if ("second_reading" in jsonFile["year_a"]):
            context["second_reading"] = jsonFile["year_a"]["second_reading"]
            context["second_responsorial_psalm"] = jsonFile["year_a"]["second_responsorial_psalm"]

        third_reading_content = ""
        if ("third_reading" in jsonFile["year_a"]):
            context["third_reading"] = jsonFile["year_a"]["third_reading"]
            context["third_responsorial_psalm"] = jsonFile["year_a"]["third_responsorial_psalm"]

        fourth_reading_content = ""
        if ("fourth_reading" in jsonFile["year_a"]):
            context["fourth_reading"] = jsonFile["year_a"]["fourth_reading"]
            context["fourth_responsorial_psalm"] = jsonFile["year_a"]["fourth_responsorial_psalm"]

        context["gospel_acclamation"] = jsonFile["year_a"]["gospel_acclamation"]
        context["gospel_reading"] = jsonFile["year_a"]["gospel_reading"]
        context["offertory"] = jsonFile["offertory"]
        context["credo"] = jsonFile["credo"]
        context["credo_content"] = credo_content
        context["communion_antiphon"] = jsonFile["communion_antiphon"]
        context["prayer_after_communion"] = jsonFile["prayer_after_communion"]
    except:
        context["file_available"] = "no"

        context["opening_antiphon"] = ""
        context["gloria"] = ""
        context["gloria_content"] = ""
        context["collect"] = ""
        context["first_reading"] = ""
        context["first_responsorial_psalm"] = ""
        context["second_reading"] = ""
        context["second_responsorial_psalm"] = ""
        context["third_reading"] = ""
        context["third_responsorial_psalm"] = ""
        context["fourth_reading"] = ""
        context["gospel_acclamation"] = ""
        context["gospel_reading"] = ""
        context["offertory"] = ""
        context["credo"] = ""
        context["credo_content"] = ""
        context["communion_antiphon"] = ""
        context["prayer_after_communion"] = ""

    return context


def christmascalendar(context = {}):

    # Load the date dimension table
    dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension").fillna("")

    # Get all days for the current liturgical season
    currentSeasonCalendar = dateDimension.loc[dateDimension["Season Short"] == "christmas"]
    currentSeasonCalendar["Qualifying Month"] = currentSeasonCalendar["Month"].apply(lambda row: datetime.strptime(str(row), "%m").strftime("%B"))
    currentSeasonCalendar["Qualifying Weekday"] = currentSeasonCalendar["Date"].apply(lambda row: datetime.strptime(str(row), "%Y-%m-%d").strftime("%A"))

    # Get unique months for the current Season
    # monthsInTheSeason = currentSeasonCalendar["Date"].apply(lambda string: datetime.strptime(string, '%Y-%m-%d').strftime('%m')).unique()
    monthsInTheSeason = currentSeasonCalendar["Month"].unique().tolist()

    calendarDictionary = context["calendar_dictionary"]
    # Get data for each day for each month in the Season
    for month in monthsInTheSeason:
        if datetime.strptime(str(month), "%m").strftime("%B") not in calendarDictionary.keys():
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")] = []
        tempDataFrame = currentSeasonCalendar.loc[currentSeasonCalendar["Month"] == month]
        for index, row in tempDataFrame.iterrows():
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")].append(row[["Date", "Qualifying Day", "Season", "Qualifying Weekday", "Week", "Feast Day", "Feast Class", "Feast Short", "Season Short"]].tolist())

    context["calendar_dictionary"] = calendarDictionary
    return context


def christmasliturgies(request, current_date = "2022-12-24", liturgy = "christmas-vigil"):

    # Get the currentDate from the request URL
    currentDate = current_date
    liturgy = liturgy
    context = {}

    dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension")
    context["file_available"] = "yes"

    try:
        # Slice the date dimension table for the current date
        feastDateIndex = dateDimension.loc[dateDimension["Date"] == currentDate].index
        feastDateDimension = dateDimension.loc[dateDimension["Date"] == currentDate]
        feastDate = feastDateDimension.iloc[0]["Date"]
        feastYear = feastDateDimension.iloc[0]["Year"]
        feastWeek = feastDateDimension.iloc[0]["Week"]
        feastMonth = feastDateDimension.iloc[0]["Month"]
        feastDay = feastDateDimension.iloc[0]["Day"]
        if (feastMonth != 12):
            raise ValueError
        elif (feastDay not in (24, 25)):
            raise ValueError
        feastSeason = feastDateDimension.iloc[0]["Season"]
        feastWeekday = datetime.strptime(feastDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
        feastQualifyingMonth = datetime.strptime(feastDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
        feastQualifyingDay = feastDateDimension.iloc[0]["Qualifying Day"]
        feastName = feastDateDimension.iloc[0]["Feast Day"]
        feastShortName = liturgy
        feastClass = feastDateDimension.iloc[0]["Feast Class"]

        templateFileName = "Solemnity"

        # Load context variables
        context = {
            "feast_date": feastDate,
            "feast_weekday": feastWeekday,
            "feast_qualifying_month": feastQualifyingMonth,
            "feast_qualifying_day": feastQualifyingDay,
            "feast_year": feastYear,
            "feast_name": feastName,
            "feast_class": feastClass,
            "feast_week": feastWeek,
            "feast_season": feastSeason
        }

        try:
            jsonFile = open(f"./static/documents/ordinaryform/christmas/{feastQualifyingMonth.lower()}/{liturgy}.json")
            jsonFile = json.load(jsonFile)

            commonPrayers = open(f"./static/documents/ordinaryform/commonprayers.json")
            commonPrayers = json.load(commonPrayers)

            context["feast_background_image"] = jsonFile["feast_background_image"]
            context["feast_image_position"] = jsonFile["feast_image_position"]

            gloria_content = ""
            if (jsonFile["gloria"] == "yes"):
                gloria_content = commonPrayers["gloria"]

            credo_content = ""
            if (jsonFile["credo"] == "apostles_creed"):
                credo_content = commonPrayers["apostles_creed"]
            elif (jsonFile["credo"] == "nicene_creed"):
                credo_content = commonPrayers["nicene_creed"]

            context["file_available"] = "yes"

            context["opening_antiphon"] = jsonFile["opening_antiphon"]
            context["gloria"] = jsonFile["gloria"]
            context["gloria_content"] = gloria_content
            context["collect"] = jsonFile["collect"]
            context["first_reading"] = jsonFile["readings"]["first_reading"]
            context["responsorial_psalm"] = jsonFile["readings"]["responsorial_psalm"]

            second_reading_content = ""
            if ("second_reading" in jsonFile["readings"]):
                context["second_reading"] = jsonFile["readings"]["second_reading"]


            context["gospel_acclamation"] = jsonFile["readings"]["gospel_acclamation"]
            context["gospel_reading"] = jsonFile["readings"]["gospel_reading"]
            context["offertory"] = jsonFile["offertory"]
            context["credo"] = jsonFile["credo"]
            context["credo_content"] = credo_content
            context["communion_antiphon"] = jsonFile["communion_antiphon"]
            context["prayer_after_communion"] = jsonFile["prayer_after_communion"]

        except:
            context["file_available"] = "no"

            context["opening_antiphon"] = ""
            context["gloria"] = ""
            context["gloria_content"] = ""
            context["collect"] = ""
            context["first_reading"] = ""
            context["responsorial_psalm"] = ""
            context["second_reading"] = ""
            context["gospel_acclamation"] = ""
            context["gospel_reading"] = ""
            context["offertory"] = ""
            context["credo"] = ""
            context["credo_content"] = ""
            context["communion_antiphon"] = ""
            context["prayer_after_communion"] = ""

    except:
        context = {}
        context["file_available"] = "no"

    return render(request, f"christmas/christmas-day.html", context)


def memorialfortheday(request, current_date = "2022-11-27"):

    # Get the currentDate from the request URL
    currentDate = current_date
    saintClass = "Feast"
    context = {}
    context["file_available"] = "yes"

    try:
        # Load the date dimension table
        dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension")

        # Slice the date dimension table for the current date
        saintDateIndex = dateDimension.loc[dateDimension["Date"] == currentDate].index
        saintDateDimension = dateDimension.loc[dateDimension["Date"] == currentDate]
        saintDate = saintDateDimension.iloc[0]["Date"]
        saintYear = saintDateDimension.iloc[0]["Year"]
        saintWeekday = datetime.strptime(saintDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
        saintQualifyingMonth = datetime.strptime(saintDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
        saintQualifyingDay = saintDateDimension.iloc[0]["Qualifying Day"]
        saintName = saintDateDimension.iloc[0]["Feast Day"]
        saintShortName = saintDateDimension.iloc[0]["Feast Short"]
        saintClass = saintDateDimension.iloc[0]["Feast Class"]
        saintImage = saintDateDimension.iloc[0]["Feast Image Location"]

        templateFileName = "Memorial"
        if (saintClass == "Feast"):
            templateFileName = "feast"
        elif (saintClass == "Memorial"):
            templateFileName = "memorial"
        elif (saintClass == "Optional Memorial"):
            templateFileName = "memorial"
        elif (saintClass == "Solemnity"):
            templateFileName = "solemnity"

        # Load context variables
        context = {
            "saint_date": saintDate,
            "saint_weekday": saintWeekday,
            "saint_qualifying_month": saintQualifyingMonth,
            "saint_qualifying_day": saintQualifyingDay,
            "saint_year": saintYear,
            "saint_name": saintName,
            "saint_class": saintClass,
            "saint_image": saintImage
        }

        if ((saintQualifyingMonth == "December")
            & (saintQualifyingDay == "25th")):
            # Load context variables
            context = {
                "current_date": saintDate,
                "current_weekday": saintWeekday,
                "current_qualifying_month": saintQualifyingMonth,
                "current_qualifying_day": saintQualifyingDay,
                "current_year": saintYear,
                "current_name": saintName,
                "current_class": saintClass,
                "current_image": saintImage
            }
            context = christmasdayoptions(context)
            return render(request, f"christmas/christmasdayliturgies.html", context)

        try:
            jsonFile = open(f"./static/documents/ordinaryform/memorials/{saintQualifyingMonth.lower()}/{saintShortName}.json")
            jsonFile = json.load(jsonFile)

            commonPrayers = open(f"./static/documents/ordinaryform/commonprayers.json")
            commonPrayers = json.load(commonPrayers)

            context["saint_background_image"] = jsonFile["saint_background_image"]

            gloria_content = ""
            if (jsonFile["gloria"] == "yes"):
                gloria_content = commonPrayers["gloria"]

            credo_content = ""
            if (jsonFile["credo"] == "apostles_creed"):
                credo_content = commonPrayers["apostles_creed"]
            elif (jsonFile["credo"] == "nicene_creed"):
                credo_content = commonPrayers["nicene_creed"]

            context["file_available"] = "yes"

            context["opening_antiphon"] = jsonFile["opening_antiphon"]
            context["gloria"] = jsonFile["gloria"]
            context["gloria_content"] = gloria_content
            context["collect"] = jsonFile["collect"]
            context["first_reading"] = jsonFile["readings"]["first_reading"]
            context["responsorial_psalm"] = jsonFile["readings"]["responsorial_psalm"]

            second_reading_content = ""
            if ("second_reading" in jsonFile["readings"]):
                context["second_reading"] = jsonFile["readings"]["second_reading"]

            context["gospel_acclamation"] = jsonFile["readings"]["gospel_acclamation"]
            context["gospel_reading"] = jsonFile["readings"]["gospel_reading"]
            context["offertory"] = jsonFile["offertory"]
            context["credo"] = jsonFile["credo"]
            context["credo_content"] = credo_content
            context["communion_antiphon"] = jsonFile["communion_antiphon"]
            context["prayer_after_communion"] = jsonFile["prayer_after_communion"]

        except:
            context["file_available"] = "no"

            context["opening_antiphon"] = ""
            context["gloria"] = ""
            context["gloria_content"] = ""
            context["collect"] = ""
            context["first_reading"] = ""
            context["responsorial_psalm"] = ""
            context["second_reading"] = ""
            context["gospel_acclamation"] = ""
            context["gospel_reading"] = ""
            context["offertory"] = ""
            context["credo"] = ""
            context["credo_content"] = ""
            context["communion_antiphon"] = ""
            context["prayer_after_communion"] = ""

    except:
        context = {}
        context["file_available"] = "no"

    return render(request, f"memorials/{templateFileName}.html", context)


def memorialloader(context = {}):

    # Get the currentDate from the request URL
    context = context
    saintShortName = context["st_short_name"]
    saintClass = "Feast"
    saintQualifyingMonth = context["feast_qualifying_month"]
    context["file_available"] = "yes"

    try:
        jsonFile = open(f"./static/documents/ordinaryform/memorials/{saintQualifyingMonth.lower()}/{saintShortName}.json")
        jsonFile = json.load(jsonFile)

        context["saint_background_image"] = jsonFile["saint_background_image"]

    except:
        context["file_available"] = "no"

        context["saint_background_image"] = ""

    return context
