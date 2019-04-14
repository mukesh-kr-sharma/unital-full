from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin
from .views import *
from . import college_view
from django.conf.urls import url

# app_name = 'main_app'

urlpatterns = [
    path('', HomePageView.as_view(), name="unital_homepage"),
    path('redirect', redirect_view, name="redirect"),
    path('admin-dashboard', AdminDashboardView.as_view(), name="admin_dashboard"),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('<slug:clg_u_name>/', college_view.CollegeHomepageView.as_view(), name='college-homepage'),
    path('<slug:clg_u_name>/<slug:username>/', include('student.urls'), name="student"),
    path('<slug:clg_u_name>/faculty/<slug:username>/', include('faculty.urls'), name="faculty"),
    path('forum/', include('forum.urls'), name="forum"),
]
