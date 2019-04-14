from django.shortcuts import render
from django.views.generic import CreateView
from django.http import JsonResponse
from main_app.models import User
from datetime import date, timedelta, datetime, timezone
from django.views.decorators.csrf import csrf_exempt
from .forms import *

class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

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
