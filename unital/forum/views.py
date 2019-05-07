from django.shortcuts import render
from django.views.generic import CreateView
from django.http import JsonResponse
from main_app.models import User
from datetime import date, timedelta, datetime, timezone
from django.views.decorators.csrf import csrf_exempt
from .forms import *


# Create your views here.
@csrf_exempt
def post_question(request, **kwargs):
    if request.method == 'POST':
        question_form = QuestionModelForm(data=request.POST)
        data = {}
        if question_form.is_valid():
            if question_form.save():
                data['success'] = 'Question Posted!!'
            else:
                data['error'] = 'Something went wrong!!'
        else:
            data['error'] = 'Something went wrong!!'
        print(question_form.errors)
        return JsonResponse(data)

@csrf_exempt
def post_reply(request, **kwargs):
    if request.method == 'POST':
        reply_form = ReplyModelForm(data=request.POST)
        data = {}
        if reply_form.is_valid():
            if reply_form.save():
                data['success'] = 'Reply Posted!!'
            else:
                data['error'] = 'Something went wrong!!'
        else:
            data['error'] = 'Something went wrong!!'
        print(reply_form.errors)
        return JsonResponse(data)
