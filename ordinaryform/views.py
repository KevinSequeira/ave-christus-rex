from django.shortcuts import render, redirect
import json
import pandas as pan
from datetime import datetime, timedelta
import pytz
import calendar

# Create your views here.
def ordinaryform(request):

    # Get current date of processing
    currentDate = datetime.now(pytz.timezone("Asia/Calcutta")).strftime('%Y-%m-%d')

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
    currentDenomination = currentDateDimension.iloc[0]["Denomination"]
    currentSeason = currentDateDimension.iloc[0]["Season"]
    currentSeasonShort = currentDateDimension.iloc[0]["Season Short"]

    # Get earliest feast day
    earliestMemorialDimension = dateDimension.loc[(dateDimension["Date"] >= currentDate) & (dateDimension["Feast Day"]).notna()]
    memorialDate = earliestMemorialDimension.iloc[0]["Date"]
    memorialWeekday = datetime.strptime(earliestMemorialDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
    memorialQualifyingMonth = datetime.strptime(earliestMemorialDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
    memorialQualifyingDay = earliestMemorialDimension.iloc[0]["Qualifying Day"]
    memorialYear = earliestMemorialDimension.iloc[0]["Year"]
    memorialTitle = earliestMemorialDimension.iloc[0]["Feast Day"]
    memorialClass = earliestMemorialDimension.iloc[0]["Feast Class"]
    if (memorialClass == "Optional Memorial"):
        memorialClass = "Memorial"
    memorialShort = earliestMemorialDimension.iloc[0]["Feast Short"]

    # Load context variables
    context = {
        "current_date": currentDate,
        "current_weekday": currentWeekday,
        "current_qualifying_month": currentQualifyingMonth,
        "current_qualifying_day": currentQualifyingDay,
        "current_year": currentYear,
        "current_week": currentWeek,
        "current_denomination": currentDenomination,
        "current_season": currentSeason,
        "current_season_short": currentSeasonShort,
        "current_cycle": currentCycle,

        "memorial_date": memorialDate,
        "memorial_weekday": memorialWeekday,
        "memorial_qualifying_month": memorialQualifyingMonth,
        "memorial_qualifying_day": memorialQualifyingDay,
        "memorial_year": memorialYear,
        "memorial_title": memorialTitle,
        "memorial_class": memorialClass,
        "memorial_short_name": memorialShort
    }

    if (currentSeasonShort == "advent"):
        context = adventloader(context)
    elif (currentSeasonShort == "christmas"):
        context = christmasloader(context)
    elif (currentSeasonShort == "epiphany"):
        context = epiphaneyloader(context)
    elif (currentSeasonShort == "ordinarytime01"):
        context = ordinarytime01loader(context)
    elif (currentSeasonShort in ("ashwednesday", "lent")):
        context = lentloader(context)
    context = memorialloader(context)

    return render(request, "ordinaryform.html", context)


def calendar(request):

    # Get current date of processing
    currentDate = datetime.now(pytz.timezone("Asia/Calcutta")).strftime('%Y-%m-%d')

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
    currentDenomination = currentDateDimension.iloc[0]["Denomination"]
    currentSeason = currentDateDimension.iloc[0]["Season"]
    currentSeasonShort = currentDateDimension.iloc[0]["Season Short"]

    # Get earliest feast Day
    earliestMemorialDimension = dateDimension.loc[(dateDimension["Date"] >= currentDate) & (dateDimension["Feast Day"]).notna()]
    memorialDate = earliestMemorialDimension.iloc[0]["Date"]
    memorialWeekday = datetime.strptime(earliestMemorialDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
    memorialQualifyingMonth = datetime.strptime(earliestMemorialDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
    memorialQualifyingDay = earliestMemorialDimension.iloc[0]["Qualifying Day"]
    memorialYear = earliestMemorialDimension.iloc[0]["Year"]
    memorialTitle = earliestMemorialDimension.iloc[0]["Feast Day"]
    memorialClass = earliestMemorialDimension.iloc[0]["Feast Class"]
    if (memorialClass == "Optional Memorial"):
        memorialClass = "Memorial"
    memorialShortName = earliestMemorialDimension.iloc[0]["Feast Short"]

    # Load context variables
    context = {
        "current_date": currentDate,
        "current_weekday": currentWeekday,
        "previous_weekday": previousWeekday,
        "current_qualifying_month": currentQualifyingMonth,
        "current_qualifying_day": currentQualifyingDay,
        "current_year": currentYear,
        "current_week": currentWeek,
        "current_denomination": currentDenomination,
        "current_season": currentSeason,
        "current_season_short": currentSeasonShort,
        "current_cycle": currentCycle,

        "memorial_date": memorialDate,
        "memorial_weekday": memorialWeekday,
        "memorial_qualifying_month": memorialQualifyingMonth,
        "memorial_qualifying_day": memorialQualifyingDay,
        "memorial_year": memorialYear,
        "memorial_title": memorialTitle,
        "memorial_class": memorialClass,
        "memorial_short_name": memorialShortName
    }

    if (currentSeasonShort == "advent"):
        context = adventloader(context)
    elif (currentSeasonShort == "christmas"):
        context = christmasloader(context)
    elif (currentSeasonShort == "epiphany"):
        context = epiphaneyloader(context)
    elif (currentSeasonShort == "ordinarytime01"):
        context = ordinarytime01loader(context)
    elif (currentSeasonShort in ("ashwednesday", "lent")):
        context = lentloader(context)
    context = adventcalendar(context)
    context = christmascalendar(context)
    context = epiphanycalendar(context)
    context = ordinarytime01calendar(context)
    context = lentcalendar(context)
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
    currentDay = currentDateDimension.iloc[0]["Day"]
    currentWeekday = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
    previousWeekday = (datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d') - timedelta(days = 1)).strftime('%A')
    currentQualifyingMonth = datetime.strptime(currentDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
    currentQualifyingDay = currentDateDimension.iloc[0]["Qualifying Day"]
    currentCycle = "A, B, C"
    currentCycle = currentDateDimension.iloc[0]["Year Cycle"]
    currentCycleShort = currentDateDimension.iloc[0]["Year Cycle Short"]
    currentYear = currentDateDimension.iloc[0]["Year"]
    currentWeek = currentDateDimension.iloc[0]["Week"]
    currentSeason = currentDateDimension.iloc[0]["Season"]
    currentSeasonShort = currentDateDimension.iloc[0]["Season Short"]
    currentDateImage = currentDateDimension.iloc[0]["Liturgy Image Location"]

    # Load context variables
    context = {
        "current_date": currentDate,
        "current_day": currentDay,
        "current_weekday": currentWeekday,
        "previous_weekday": previousWeekday,
        "current_qualifying_month": currentQualifyingMonth,
        "current_qualifying_day": currentQualifyingDay,
        "current_year": currentYear,
        "current_week": currentWeek,
        "current_season": currentSeason,
        "current_season_short": currentSeasonShort,
        "current_cycle": currentCycle,
        "current_cycle_short": currentCycleShort,
        "current_date_image": currentDateImage
    }

    if (currentQualifyingMonth == "December"):
        if (currentQualifyingDay == "25th"):
            context = christmasdayoptions(context)
            return render(request, f"christmas/christmasdayliturgies.html", context)
        elif (currentQualifyingDay in ("26th", "27th", "28th")):
            return redirect("memorialfortheday", f"{current_date}")
        elif (currentQualifyingDay in ("29th", "30th", "31st")):
            if (currentWeekday == "Sunday"):
                return redirect("memorialfortheday", f"{current_date}")
    elif (currentQualifyingMonth == "January"):
        if (currentQualifyingDay == "1st"):
            return redirect("memorialfortheday", f"{current_date}")
        elif (currentQualifyingDay == "6th"):
            return redirect("memorialfortheday", f"{current_date}")
        elif ((currentQualifyingDay in ("7th", "8th", "9th", "10th", "11th", "12th", "13th"))
            & (currentWeekday == "Sunday")):
            return redirect("memorialfortheday", f"{current_date}")
    elif (currentWeek == "Holy Week"):
        if (currentWeekday == "Thursday"):
            return render(request, f"lent/maundythursdayliturgies.html", context)
        elif (currentWeekday == "Friday"):
            return render(request, f"christmas/goodfridayliturgy.html", context)
        elif (currentWeekDay == "Saturday"):
            pass

    # Add season-specific context variables
    if (currentSeasonShort == "advent"):
        context = advent(context)
    elif (currentSeasonShort == "christmas"):
        context = christmas(context)
    elif (currentSeasonShort == "epiphany"):
        context = epiphany(context)
    elif (currentSeasonShort == "ordinarytime01"):
        context = ordinarytime01(context)
    elif (currentSeasonShort == "ashwednesday"):
        context = lent(context)
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
        context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"

    except:
        context["file_available"] = "no"
        context["liturgy_background_image"] = ""

    return context


def advent(context = {}):

    try:
        jsonFile = ""
        if ((context["current_day"] > 16)
            & (context["current_qualifying_month"] == 'December')
            & (context["current_weekday"] != 'Sunday')):
            jsonFile = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_qualifying_day'].lower()}.json")
        else:
            jsonFile = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_week'].lower()}/{context['current_weekday'].lower()}.json")
        jsonFile = json.load(jsonFile)

        commonPrayers = open(f"./static/documents/ordinaryform/commonprayers.json")
        commonPrayers = json.load(commonPrayers)

        context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
        context["liturgy_background_position"] = jsonFile["liturgy_background_position"]

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
        tempDataFrame = currentSeasonCalendar.loc[currentSeasonCalendar["Month"] == month]
        if datetime.strptime(str(month), "%m").strftime("%B") not in calendarDictionary.keys():
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")] = []
        for index, row in tempDataFrame.iterrows():
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")].append(row[["Date", "Qualifying Day", "Season", "Qualifying Weekday", "Week", "Feast Day", "Feast Class", "Feast Short", "Season Short"]].tolist())

    context["calendar_dictionary"] = calendarDictionary
    return context


def christmasloader(context = {}):

    try:
        jsonFile = ""
        if (context["current_qualifying_month"] == "December"):
            if (context["current_qualifying_day"] == "25th"):
                jsonFile = open(f"./static/documents/ordinaryform/christmas/december/christmas-options.json")
                jsonFile = json.load(jsonFile)
                context["liturgy_background_image"] = jsonFile["christmas_vigil"]["feast_background_image"]
                context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"
                context["memorial_background_image"] = jsonFile["christmas_midnight"]["feast_background_image"]
            elif (context["current_qualifying_day"] == "26th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/jesus-mary-joseph.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/st-stephen-protomartyr.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"
            elif (context["current_qualifying_day"] == "27th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/jesus-mary-joseph.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/st-john-baptist.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"
            elif (context["current_qualifying_day"] == "28th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/jesus-mary-joseph.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-innocents.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"
            elif (context["current_qualifying_day"] == "29th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/jesus-mary-joseph.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/29th.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"
            elif (context["current_qualifying_day"] == "30th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/jesus-mary-joseph.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/30th.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"
            elif (context["current_qualifying_day"] == "31st"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/jesus-mary-joseph.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/31st.json")
                    jsonFile = json.load(jsonFile)
                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"

        elif (context["current_qualifying_month"] == "January"):
            if (context["current_qualifying_day"] == "1st"):
                jsonFile = open(f"./static/documents/ordinaryform/memorials/january/theotokos.json")

                jsonFile = json.load(jsonFile)

                context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"

            elif (context["current_qualifying_day"] < "6th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/january/second-sunday.json")

                    jsonFile = json.load(jsonFile)

                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"

                else:
                    jsonFile_readings = open(f"./static/documents/ordinaryform/christmas/january/{context['current_weekday'].lower()}.json")
                    jsonFile_prayers = open(f"./static/documents/ordinaryform/christmas/january/{context['current_qualifying_day'].lower()}.json")

                    jsonFile_readings = json.load(jsonFile_readings)
                    jsonFile_prayers = json.load(jsonFile_prayers)

                    jsonFile = { **jsonFile_readings, **jsonFile_prayers }

                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"

    except:
        context["file_available"] = "no"

        context["liturgy_background_image"] = "linear-gradient(rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.6) ), url('../../../static/images/saints/white_background_001.jpg')"

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
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/jesus-mary-joseph.json")
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/st-stephen-protomartyr.json")
            elif (context["current_qualifying_day"] == "27th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/jesus-mary-joseph.json")
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/st-john-baptist.json")
            elif (context["current_qualifying_day"] == "28th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/jesus-mary-joseph.json")
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/holy-innocents.json")
            elif (context["current_qualifying_day"] == "29th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/jesus-mary-joseph.json")
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/29th.json")
            elif (context["current_qualifying_day"] == "30th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/jesus-mary-joseph.json")
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/30th.json")
            elif (context["current_qualifying_day"] == "31st"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/december/jesus-mary-joseph.json")
                else:
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/december/31st.json")

            jsonFile = json.load(jsonFile)

        elif (context["current_qualifying_month"] == "January"):
            if (context["current_qualifying_day"] == "1st"):
                jsonFile = open(f"./static/documents/ordinaryform/memorials/january/theotokos.json")

                jsonFile = json.load(jsonFile)

            elif (context["current_qualifying_day"] < "6th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/christmas/january/second-sunday.json")

                    jsonFile = json.load(jsonFile)

                else:
                    jsonFile_readings = open(f"./static/documents/ordinaryform/christmas/january/{context['current_weekday'].lower()}.json")
                    jsonFile_prayers = open(f"./static/documents/ordinaryform/christmas/january/{context['current_qualifying_day'].lower()}.json")

                    jsonFile_readings = json.load(jsonFile_readings)
                    jsonFile_prayers = json.load(jsonFile_prayers)

                    jsonFile = { **jsonFile_readings, **jsonFile_prayers }

        commonPrayers = open(f"./static/documents/ordinaryform/commonprayers.json")
        commonPrayers = json.load(commonPrayers)

        context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
        context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"

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

        context["liturgy_background_image"] = "linear-gradient(rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.6) ), url('../../../static/images/saints/white_background_001.jpg')"

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
        tempDataFrame = currentSeasonCalendar.loc[currentSeasonCalendar["Month"] == month]
        if datetime.strptime(str(month), "%m").strftime("%B") not in calendarDictionary.keys():
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")] = []
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
            "feast_season": feastSeason,
            "feast_liturgy": "Vigil"
        }

        if (liturgy == "christmas-vigil"):
            context["feast_liturgy"] = "Vigil"
        elif (liturgy == "christmas-midnight"):
            context["feast_liturgy"] = "Midnight"
        elif (liturgy == "christmas-dawn"):
            context["feast_liturgy"] = "Dawn"
        elif (liturgy == "christmas-daytime"):
            context["feast_liturgy"] = "Daytime"

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


def epiphaneyloader(context):

    try:
        if (context["current_qualifying_month"] == "January"):
            if (context["current_qualifying_day"] == "6th"):
                jsonFile = open(f"./static/documents/ordinaryform/memorials/january/epiphany.json")

                jsonFile = json.load(jsonFile)

                context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"

            elif (context["current_qualifying_day"] > "6th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/january/baptism-jesus.json")

                    jsonFile = json.load(jsonFile)

                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"

                else:
                    jsonFile = open(f"./static/documents/ordinaryform/epiphany/{context['current_qualifying_day'].lower()}.json")

                    jsonFile = json.load(jsonFile)

                    context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
                    context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"

    except:
        context["file_available"] = "no"

        context["liturgy_background_image"] = "linear-gradient(rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.6) ), url('../../../static/images/saints/white_background_001.jpg')"

    return context


def epiphany(context = {}):

    try:
        jsonFile = ""
        if (context["current_qualifying_month"] == "January"):
            if (context["current_qualifying_day"] == "6th"):
                jsonFile = open(f"./static/documents/ordinaryform/memorials/january/epiphany.json")

            elif (context["current_qualifying_day"] > "6th"):
                if (context["current_weekday"] == "Sunday"):
                    jsonFile = open(f"./static/documents/ordinaryform/memorials/january/baptism-jesus.json")

                else:
                    jsonFile = open(f"./static/documents/ordinaryform/epiphany/{context['current_qualifying_day'].lower()}.json")

        jsonFile = json.load(jsonFile)

        commonPrayers = open(f"./static/documents/ordinaryform/commonprayers.json")
        commonPrayers = json.load(commonPrayers)

        context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
        context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"

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

        context["liturgy_background_image"] = "linear-gradient(rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.6) ), url('../../../static/images/saints/white_background_001.jpg')"

    return context


def epiphanycalendar(context = {}):

    # Load the date dimension table
    dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension").fillna("")

    # Get all days for the current liturgical season
    currentSeasonCalendar = dateDimension.loc[dateDimension["Season Short"] == "epiphany"]
    currentSeasonCalendar["Qualifying Month"] = currentSeasonCalendar["Month"].apply(lambda row: datetime.strptime(str(row), "%m").strftime("%B"))
    currentSeasonCalendar["Qualifying Weekday"] = currentSeasonCalendar["Date"].apply(lambda row: datetime.strptime(str(row), "%Y-%m-%d").strftime("%A"))

    # Get unique months for the current Season
    # monthsInTheSeason = currentSeasonCalendar["Date"].apply(lambda string: datetime.strptime(string, '%Y-%m-%d').strftime('%m')).unique()
    monthsInTheSeason = currentSeasonCalendar["Month"].unique().tolist()

    calendarDictionary = context["calendar_dictionary"]
    # Get data for each day for each month in the Season
    for month in monthsInTheSeason:
        tempDataFrame = currentSeasonCalendar.loc[currentSeasonCalendar["Month"] == month]
        if datetime.strptime(str(month), "%m").strftime("%B") not in calendarDictionary.keys():
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")] = []
        for index, row in tempDataFrame.iterrows():
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")].append(row[["Date", "Qualifying Day", "Season", "Qualifying Weekday", "Week", "Feast Day", "Feast Class", "Feast Short", "Season Short"]].tolist())

    context["calendar_dictionary"] = calendarDictionary
    return context


def ordinarytime01loader(context = {}):

    context = context
    try:
        jsonFilePrayers = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_week'].lower()}/prayers.json")
        jsonFilePrayers = json.load(jsonFilePrayers)
        jsonFileReadings = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_week'].lower()}/{context['current_weekday'].lower()}.json")
        jsonFileReadings = json.load(jsonFileReadings)

        jsonFile = { **jsonFilePrayers, **jsonFileReadings }

        context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
        context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"

    except:
        context["file_available"] = "no"
        context["liturgy_background_image"] = ""

    return context


def ordinarytime01(context = {}):

    try:
        jsonFilePrayers = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_week'].lower()}/prayers.json")
        jsonFilePrayers = json.load(jsonFilePrayers)
        jsonFileReadings = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_week'].lower()}/{context['current_weekday'].lower()}.json")
        jsonFileReadings = json.load(jsonFileReadings)

        jsonFile = { **jsonFilePrayers, **jsonFileReadings }

        commonPrayers = open(f"./static/documents/ordinaryform/commonprayers.json")
        commonPrayers = json.load(commonPrayers)

        context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
        context["liturgy_background_position"] = jsonFile["liturgy_background_position"]

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
        context["first_reading"] = jsonFile[context["current_cycle_short"]]["first_reading"]
        context["first_responsorial_psalm"] = jsonFile[context["current_cycle_short"]]["first_responsorial_psalm"]

        second_reading_content = ""
        if ("second_reading" in jsonFile[context["current_cycle_short"]]):
            context["second_reading"] = jsonFile[context["current_cycle_short"]]["second_reading"]

        context["gospel_acclamation"] = jsonFile[context["current_cycle_short"]]["gospel_acclamation"]
        context["gospel_reading"] = jsonFile[context["current_cycle_short"]]["gospel_reading"]
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


def ordinarytime01calendar(context = {}):

    # Load the date dimension table
    dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension").fillna("")

    # Get all days for the current liturgical season
    currentSeasonCalendar = dateDimension.loc[dateDimension["Season Short"] == "ordinarytime01"]
    currentSeasonCalendar["Qualifying Month"] = currentSeasonCalendar["Month"].apply(lambda row: datetime.strptime(str(row), "%m").strftime("%B"))
    currentSeasonCalendar["Qualifying Weekday"] = currentSeasonCalendar["Date"].apply(lambda row: datetime.strptime(str(row), "%Y-%m-%d").strftime("%A"))

    # Get unique months for the current Season
    # monthsInTheSeason = currentSeasonCalendar["Date"].apply(lambda string: datetime.strptime(string, '%Y-%m-%d').strftime('%m')).unique()
    monthsInTheSeason = currentSeasonCalendar["Month"].unique().tolist()

    calendarDictionary = context["calendar_dictionary"]
    # Get data for each day for each month in the Season
    for month in monthsInTheSeason:
        tempDataFrame = currentSeasonCalendar.loc[currentSeasonCalendar["Month"] == month]
        if datetime.strptime(str(month), "%m").strftime("%B") not in calendarDictionary.keys():
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")] = []
        for index, row in tempDataFrame.iterrows():
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")].append(row[["Date", "Qualifying Day", "Season", "Qualifying Weekday", "Week", "Feast Day", "Feast Class", "Feast Short", "Season Short"]].tolist())

    context["calendar_dictionary"] = calendarDictionary
    return context


def lentloader(context = {}):

    context = context
    try:
        jsonFile = ""
        if (context["current_week"] == "Ash Wednesday"):
            jsonFile = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_weekday'].lower()}.json")
        elif (context["current_week"] == "Holy Week"):
            if (context["current_weekday"] == "Thursday"):
                jsonFile = open(f"./static/documents/ordinaryform/{context['current_season_short']}/context['current_week']/{context['current_weekday'].lower()}.json")
            elif (context["current_weekday"]):
                pass
        else:
            jsonFile = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_week'].lower()}/{context['current_weekday'].lower()}.json")
        jsonFile = json.load(jsonFile)
        context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
        context["liturgy_background_position"] = jsonFile["liturgy_background_position"] or "top"

    except:
        context["file_available"] = "no"
        context["liturgy_background_image"] = ""

    return context


def lent(context = {}):

    try:
        jsonFile = ""
        if (context["current_week"] == "Ash Wednesday"):
            jsonFile = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_weekday'].lower()}.json")
        else:
            jsonFile = open(f"./static/documents/ordinaryform/{context['current_season_short']}/{context['current_week'].lower()}/{context['current_weekday'].lower()}.json")
        jsonFile = json.load(jsonFile)

        commonPrayers = open(f"./static/documents/ordinaryform/commonprayers.json")
        commonPrayers = json.load(commonPrayers)

        context["liturgy_background_image"] = jsonFile["liturgy_background_image"]
        context["liturgy_background_position"] = jsonFile["liturgy_background_position"]

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

        context["gradual"] = jsonFile["year_a"]["gradual"]
        context["gospel_reading"] = jsonFile["year_a"]["gospel_reading"]

        ashes_blessings_content = ""
        if ("blessing_the_ashes" in jsonFile):
            context["blessing_the_ashes"] = jsonFile["blessing_the_ashes"]
            context["ash_distribution_antiphons"] = jsonFile["ash_distribution_antiphons"]

        context["offertory"] = jsonFile["offertory"]
        context["credo"] = jsonFile["credo"]
        context["credo_content"] = credo_content
        context["communion_antiphon"] = jsonFile["communion_antiphon"]
        context["prayer_after_communion"] = jsonFile["prayer_after_communion"]
        context["prayer_over_the_people"] = jsonFile["prayer_over_the_people"]

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
        
        context["blessing_the_ashes"] = ""
        context["ash_distribution_antiphon_01"] = ""
        context["ash_distribution_antiphon_02"] = ""
        context["ash_distribution_antiphon_03"] = ""
        context["responsory_after_distribution"] = ""

        context["offertory"] = ""
        context["credo"] = ""
        context["credo_content"] = ""
        context["communion_antiphon"] = ""
        context["prayer_after_communion"] = ""
        context["prayer_over_the_people"] = ""

    return context


def lentcalendar(context = {}):

    # Load the date dimension table
    dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension").fillna("")

    # Get all days for the current liturgical season
    currentSeasonCalendar = dateDimension.loc[dateDimension["Season Short"].isin(["ashwednesday", "lent"])]
    currentSeasonCalendar["Qualifying Month"] = currentSeasonCalendar["Month"].apply(lambda row: datetime.strptime(str(row), "%m").strftime("%B"))
    currentSeasonCalendar["Qualifying Weekday"] = currentSeasonCalendar["Date"].apply(lambda row: datetime.strptime(str(row), "%Y-%m-%d").strftime("%A"))

    # Get unique months for the current Season
    # monthsInTheSeason = currentSeasonCalendar["Date"].apply(lambda string: datetime.strptime(string, '%Y-%m-%d').strftime('%m')).unique()
    monthsInTheSeason = currentSeasonCalendar["Month"].unique().tolist()

    calendarDictionary = context["calendar_dictionary"]
    # Get data for each day for each month in the Season
    for month in monthsInTheSeason:
        tempDataFrame = currentSeasonCalendar.loc[currentSeasonCalendar["Month"] == month]
        if datetime.strptime(str(month), "%m").strftime("%B") not in calendarDictionary.keys():
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")] = []
        for index, row in tempDataFrame.iterrows():
            calendarDictionary[datetime.strptime(str(month), "%m").strftime("%B")].append(row[["Date", "Qualifying Day", "Season", "Qualifying Weekday", "Week", "Feast Day", "Feast Class", "Feast Short", "Season Short"]].tolist())

    context["calendar_dictionary"] = calendarDictionary
    return context


def memorialloader(context = {}):

    # Get the currentDate from the request URL
    context = context
    memorialShortName = context["memorial_short_name"]
    memorialClass = "Feast"
    memorialQualifyingMonth = context["memorial_qualifying_month"]
    context["file_available"] = "yes"

    try:
        jsonFile = open(f"./static/documents/ordinaryform/memorials/{memorialQualifyingMonth.lower()}/{memorialShortName}.json")
        jsonFile = json.load(jsonFile)

        context["memorial_background_image"] = jsonFile["saint_background_image"]
        context["memorial_background_position"] = jsonFile["saint_background_position"] or "top"

    except:
        context["file_available"] = "no"

        context["memorial_background_image"] = ""

    return context


def memorialfortheday(request, current_date = "2022-11-27"):

    # Get the currentDate from the request URL
    currentDate = current_date
    memorialClass = "Feast"
    context = {}
    context["file_available"] = "yes"

    try:
        # Load the date dimension table
        dateDimension = pan.read_excel(f"./static/documents/datedimension.xlsx", sheet_name = "datedimension")

        # Slice the date dimension table for the current date
        memorialDateIndex = dateDimension.loc[dateDimension["Date"] == currentDate].index
        memorialDateDimension = dateDimension.loc[dateDimension["Date"] == currentDate]
        memorialDate = memorialDateDimension.iloc[0]["Date"]
        memorialYear = memorialDateDimension.iloc[0]["Year"]
        memorialWeekday = datetime.strptime(memorialDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%A')
        memorialQualifyingMonth = datetime.strptime(memorialDateDimension.iloc[0]["Date"], '%Y-%m-%d').strftime('%B')
        memorialQualifyingDay = memorialDateDimension.iloc[0]["Qualifying Day"]
        currentSeasonShort = memorialDateDimension.iloc[0]["Season Short"]
        memorialName = memorialDateDimension.iloc[0]["Feast Day"]
        memorialShortName = memorialDateDimension.iloc[0]["Feast Short"]
        memorialClass = memorialDateDimension.iloc[0]["Feast Class"]
        memorialImage = memorialDateDimension.iloc[0]["Feast Image Location"]

        templateFileName = "Memorial"
        if (memorialClass == "Feast"):
            templateFileName = "feast"
        elif (memorialClass == "Memorial"):
            templateFileName = "memorial"
        elif (memorialClass == "Optional Memorial"):
            templateFileName = "memorial"
        elif (memorialClass == "Solemnity"):
            templateFileName = "solemnity"

        # Load context variables
        context = {
            "memorial_date": memorialDate,
            "memorial_weekday": memorialWeekday,
            "memorial_qualifying_month": memorialQualifyingMonth,
            "memorial_qualifying_day": memorialQualifyingDay,
            "memorial_year": memorialYear,
            "current_season_short": currentSeasonShort,
            "memorial_name": memorialName,
            "memorial_class": memorialClass,
            "memorial_cycle": "",
            "memorial_image": memorialImage
        }

        if ((memorialQualifyingMonth == "December")
            & (memorialQualifyingDay in ("24th", "25th"))):
            # Load context variables
            context = {
                "current_date": memorialDate,
                "current_weekday": memorialWeekday,
                "current_qualifying_month": memorialQualifyingMonth,
                "current_qualifying_day": memorialQualifyingDay,
                "current_year": memorialYear,
                "current_class": memorialClass,
                "current_image": memorialImage
            }
            context = christmasdayoptions(context)
            # return render(request, f"christmas/christmasdayliturgies.html", context)
            if (memorialQualifyingDay == "24th"):
                current_date = str(datetime.strptime(memorialDateDimension.iloc[0]["Date"], '%Y-%m-%d') + timedelta(days = 1))[0:10]
                return redirect("christmasliturgies", current_date = current_date, liturgy = 'christmas-vigil')
            else:
                return redirect("liturgyfortheday", f"{current_date}")
        elif (memorialQualifyingMonth == "January"):
            if (memorialQualifyingDay == "6th"):
                context["memorial_cycle"] = "A, B, C"
            elif (memorialShortName in ("baptism")):
                context["memorial_cycle"] = memorialDateDimension.iloc[0]["Year Cycle"]

        try:
            jsonFile = open(f"./static/documents/ordinaryform/memorials/{memorialQualifyingMonth.lower()}/{memorialShortName}.json")
            jsonFile = json.load(jsonFile)

            commonPrayers = open(f"./static/documents/ordinaryform/commonprayers.json")
            commonPrayers = json.load(commonPrayers)

            context["memorial_background_image"] = jsonFile["saint_background_image"]
            context["memorial_background_position"] = jsonFile["saint_background_position"] or "top"

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
            context["first_responsorial_psalm"] = jsonFile["readings"]["first_responsorial_psalm"]

            second_reading_content = ""
            if ("second_reading" in jsonFile["readings"]):
                context["second_reading"] = jsonFile["readings"]["second_reading"]
                second_reading_content = "yes"

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

            return redirect('memorial', currentDate)

    except:
        context = {}
        context["file_available"] = "no"
        return redirect('liturgyfortheday', currentDate)

    return render(request, f"memorials/{templateFileName}.html", context)
