from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin
from .views import *
from django.conf.urls import url

app_name = 'portfolio'

urlpatterns = [
    path('', TemplateView.as_view(template_name='portfolio/portfolio.html'), name="homepage"),
    
]
