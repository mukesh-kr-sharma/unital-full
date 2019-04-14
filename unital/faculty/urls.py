from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin
from .views import *
from django.conf.urls import url

app_name = 'faculty'

urlpatterns = [
    path('', TemplateView.as_view(template_name='college/faculty/faculty-homepage.html'), name="homepage"),
    path('student-list', StudentListView.as_view() , name="student-list"),
    path('student-list/<slug:student_username>', StudentDetailView.as_view(), name="student-detail"),
    path('syllabus', syllabus, name="syllabus"),
    path('forum', ForumView.as_view(), name="forum"),
]