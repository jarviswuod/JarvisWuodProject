from django.contrib import admin
from django.urls import path
from .views import home, addNewMail, weeklyMail


urlpatterns = [
    path('', home),
    path('new-mail/', addNewMail),
    path('job-updates/', weeklyMail),
]
