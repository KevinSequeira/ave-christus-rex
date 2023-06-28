## ================================================================================================================== ##

## ================================================================================================================== ##
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.response import TemplateResponse
import sqlite3

def home(request):
    # Get blog details
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = f"""SELECT [blog_title],
        [blog_subtitle],
        [blog_tag],
        [blog_background]
        FROM [blog_post]
        ORDER BY [created_at] DESC
        LIMIT 1;"""
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    cursor.close()

    context = {
        "blog_title": record[0][0],
        "blog_subtitle": record[0][1],
        "blog_tag": record[0][2],
        "blog_background": record[0][3]
    }

    return render(request, "index.html", context)
    # send_mail("Test Subject", "Test Message", settings.EMAIL_HOST_USER, ["iamkevinsequeira@gmail.com"], fail_silently=False)
    # context = {'autocompleteStrings': ["This",
    #                                   "is",
    #                                   "awesome",
    #                                   "Come",
    #                                   "and",
    #                                   "worship",
    #                                   "the",
    #                                   "LORD",
    #                                   "For God so loved the world that He gave His only begotten son, so that whoever believes in Him will not perish but have eternal life."]}
    # return render(request, "index.html", context)
