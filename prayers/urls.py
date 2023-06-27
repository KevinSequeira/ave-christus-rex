"""surveys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path("", views.prayers, name = "prayers"),
    re_path(r'^(?P<prayer_category_tag>.+?)/(?P<prayer_name_tag>.+?)/$', views.prayerDetails, name = "prayers"),
    re_path(r'^(?P<prayer_category_tag>.+?)/$', views.prayerCategory, name = "prayers"),
    path("essentialPrayers", views.essentialPrayers, name = "essentialPrayers"),
    # path("simpleprayers", views.simpleprayers, name = "simpleprayers"),
    # re_path(r'^prayer-details/(?P<page_alias>.+?)/$', views.prayerDetails , name = "prayerDetails"),
    path('tinymce/', include('tinymce.urls')),
]
