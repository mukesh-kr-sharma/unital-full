from django.views.generic import TemplateView
from django.urls import path
from django.contrib import admin
from .views import *
from . import college_view
from django.conf.urls import url


urlpatterns = [
    path('', HomePageView.as_view(), name="unital_homepage"),
    path('redirect', redirect_view, name="redirect"),
    path('admin-dashboard', AdminDashboardView.as_view(), name="admin_dashboard"),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    # path('<slug:clg_u_name>/', TemplateView.as_view(template_name='unital/unital-homepage.html'), name='index'),
    path('college/<slug:clg_u_name>/', college_view.CollegeHomepageView.as_view(), name='college-homepage')
]
