from django.views.generic import TemplateView
from django.urls import path, include
from .views import *

app_name = 'guest'

urlpatterns = [
    path('register', guest_registration, name="sign-up"),
    path('', TemplateView.as_view(template_name='unital/guest/guest-homepage.html')),
    path('login', guest_login, name="sign-in"),
]
