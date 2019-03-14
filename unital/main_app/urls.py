from django.views.generic import TemplateView
from django.urls import path
from django.contrib import admin
from .views import *
from django.conf.urls import url
from django.urls import reverse_lazy

urlpatterns = [
    path('', HomePageView.as_view(), name="unital_homepage"),
    path('redirect', redirect_view, name="redirect"),
    path('admin-dashboard', AdminDashboardView.as_view(), name="admin_dashboard"),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout')
]
