from django.contrib import admin
from django.urls import path
from .views import home, addNewMail, weeklyMail


urlpatterns = [
    path('', home),
    path('new-mail/', addNewMail, name="new-mail"),
    path('job-updates/', weeklyMail, name="job-updates"),
]
