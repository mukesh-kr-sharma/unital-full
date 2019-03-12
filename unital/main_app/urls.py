from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin
from .views import *
from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
# https://godjango.com/143-django-111-djangocontribauth-class-based-views-part-1/

urlpatterns = [
    path('', HomePageView.as_view(), name="unital_homepage"),
    path('adminDashboard', AdminDashboardView.as_view(), name="admin_dashboard"),
    path('login', LoginView.as_view(template_name='unital/admin_login.html', extra_context={
        # option 1: provide full path
        #'next': '/account/my_custom_url/',
        # option 2: just provide the name of the url
        'next': 'admin_dashboard',
    }), name='admin_login'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('admin_login')), name='admin_logout')
]
