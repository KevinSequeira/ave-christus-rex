from django.shortcuts import render
import sqlite3

# Create your views here.
def blog(request):
    context = {}
    return render(request, "blogpost.html", context)

def blog(request, article_number = "B0001"):

    # Get blog details
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = f"SELECT * FROM [blogArticles] WHERE [ID] = '{article_number}';"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print(record)
    cursor.close()

    blogTitle = "The Season of Advent"
    blogTagline = "Draw on the graces of the Season as we prepare ourselves for the commemoration of the birth of our Lord Jesus Christ"
    blogBackgroundImage = "../../static/images/Extra Large/Advent in Church.jpg"

    context = {
        "blog_title": record[0][1],
        "blog_tagline": record[0][2],
        "blog_background_image": blogBackgroundImage
    }

    return render(request, "blogpost.html", context)
