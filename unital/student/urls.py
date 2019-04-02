from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin
from .views import *
from django.conf.urls import url

# TEMPLATE TAGGING
app_name = 'student'

urlpatterns = [
    path('', TemplateView.as_view(template_name='college/student/student-homepage.html'), name="homepage"),
    # path('/portfolio', include('portfolio.urls'), name="portfolio" ),
    # path('/portfolio', PortfolioView.as_view(), name="portfolio" ),
    path('/portfolio', portfolio, name="portfolio" )
]
