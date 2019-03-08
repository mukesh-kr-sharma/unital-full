from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', HomePageView.as_view()),
]
