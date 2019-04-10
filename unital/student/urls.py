from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin
from .views import *
from django.conf.urls import url

app_name = 'student'

urlpatterns = [
    path('', TemplateView.as_view(template_name='college/student/student-homepage.html'), name="homepage"),
    path('portfolio', portfolio, name="portfolio" ),
    path('portfolio/update', update_portfolio, name="update-portfolio" ),
    path('syllabus', syllabus, name="syllabus"),
]
# https://computernerddiaries.wordpress.com/2014/10/29/django-error-generic-detail-view-must-be-called-with-either-an-object-pk-or-a-slug/