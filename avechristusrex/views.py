## ================================================================================================================== ##

## ================================================================================================================== ##
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.response import TemplateResponse

def home(request):
    # send_mail("Test Subject", "Test Message", settings.EMAIL_HOST_USER, ["iamkevinsequeira@gmail.com"], fail_silently=False)
    context = {'autocompleteStrings': ["This",
                                      "is",
                                      "awesome",
                                      "Come",
                                      "and",
                                      "worship",
                                      "the",
                                      "LORD",
                                      "For God so loved the world that He gave His only begotten son, so that whoever believes in Him will not perish but have eternal life."]}
    return render(request, "index.html", context)
