from django.shortcuts import render

# Create your views here.
def blog(request):
    context = {}
    return render(request, "blogpost.html", context)

def blog(request, article_number = "advent"):

    # Get blog details
    blogTitle = "The Season of Advent"
    blogTagline = "Draw on the graces of the Season as we prepare ourselves for the commemoration of the birth of our Lord Jesus Christ"
    blogBackgroundImage = "../../static/images/Extra Large/Advent in Church.jpg"

    context = {
        "blog_title": blogTitle,
        "blog_tagline": blogTagline,
        "blog_background_image": blogBackgroundImage
    }

    return render(request, "blogpost.html", context)
