from django.views.generic import TemplateView
from django.urls import path, include
from .views import *

app_name = 'guest'

urlpatterns = [
    path('register', guest_registration, name="sign-up"),
    path('login', guest_login, name="sign-in"),
    path('forum', ForumView.as_view(), name="forum"),
    path('profile', profile, name="profile"),
    path('settings', settings, name='settings'),
    path('notice', notice, name='notice'),
    path('notice/<int:pk>', notice_detail, name="notice-detail"),
    path('', guest_homepage, name="homepage"),
]
