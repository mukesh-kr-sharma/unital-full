from django.urls import path, include
from .views import *

app_name = 'forum'

urlpatterns = [
    path('post-question', post_question, name='post-question'),
    path('post-reply', post_reply, name='post-reply'),
]