from django.shortcuts import render
import sqlite3

# Create your views here.
def blog(request):
    # Get blog list
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = f"""SELECT [blog_title],
        [blog_subtitle],
        CAST(STRFTIME('%d-%m-%Y', [created_at]) AS TEXT) AS [created_at],
        CAST(STRFTIME('%d-%m-%Y', [updated_at]) AS TEXT) AS [updated_at],
        [blog_tag],
        STRFTIME('%d', [created_at]) || ' ' || CASE STRFTIME('%m', [created_at])
            WHEN '01' THEN 'January'
            WHEN '02' THEN 'February'
            WHEN '03' THEN 'March'
            WHEN '04' THEN 'April'
            WHEN '05' THEN 'May'
            WHEN '06' THEN 'June'
            WHEN '07' THEN 'July'
            WHEN '08' THEN 'August'
            WHEN '09' THEN 'September'
            WHEN '10' THEN 'October'
            WHEN '11' THEN 'November'
            WHEN '12' THEN 'December'
            END || ', ' || STRFTIME('%Y', [created_at]) AS [created_date_text],
        STRFTIME('%d', [updated_at]) || ' ' || CASE STRFTIME('%m', [updated_at])
            WHEN '01' THEN 'January'
            WHEN '02' THEN 'February'
            WHEN '03' THEN 'March'
            WHEN '04' THEN 'April'
            WHEN '05' THEN 'May'
            WHEN '06' THEN 'June'
            WHEN '07' THEN 'July'
            WHEN '08' THEN 'August'
            WHEN '09' THEN 'September'
            WHEN '10' THEN 'October'
            WHEN '11' THEN 'November'
            WHEN '12' THEN 'December'
            END || ', ' || STRFTIME('%Y', [updated_at]) AS [updated_at_text]
        FROM [blog_post]
        ORDER BY [created_at] DESC;"""
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print(record)
    cursor.close()

    context = {
        "blog_list": record
    }

    return render(request, "blogList.html", context)

def blogArticle(request, blog_tag = "season-of-advent"):
    # Get blog details
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = f"SELECT * FROM [blog_post] WHERE [blog_tag] = '{blog_tag}';"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    cursor.close()

    context = {
        "blog_title": record[0][1],
        "blog_tagline": record[0][2],
        "blog_content": record[0][5],
        "blog_tag": record[0][6],
        "blog_background": record[0][7]
    }

    return render(request, "blogpost.html", context)
