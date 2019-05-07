from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from main_app import models as main_app_models
from django.views.generic.list import ListView
from main_app.forms import ProfileSettingModelForm
from forum.models import *
from forum.forms import *
from .forms import *

# Create your views here.
def guest_registration(request):
    context = {}
    if request.method == 'POST':
        print(request.POST)
        guest_form = GuestModelForm(request.POST)
        if guest_form.is_valid():
            guest_form.save()
        else:
            print(guest_form.errors)
    return render(request, template_name='unital/guest/register.html', context=context)

def guest_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        print(username, password, user_type)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            if user.user_type == user_type:
                login(request, user)
                return redirect('guest:homepage')
    return render(request, template_name='unital/guest/login.html', context=context)

def guest_homepage(request, **kwargs):
    if request.user.id is None:
        return redirect('guest:sign-in')
    return render(request, template_name='unital/guest/guest-homepage.html')

class ForumView(ListView):
    model = Question
    context_object_name = 'question_list'
    template_name = 'college/forum/forum-main.html'
    extra_context = {
        'COLLEGE_CHOICES': main_app_models.College.objects.all(),
        'DEPARTMENT_CHOICES': main_app_models.Department.objects.all(),
        'BASE_TEMPLATE' : 'unital/guest/base.html',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_object(self):
        return Question.objects.filter(for_college = self.request.user.college, for_department = self.request.user.department)

#################### SETTINGS #########################
def settings(request, **kwargs):
    context = {'BASE_TEMPLATE':'unital/guest/base.html'}
    if request.method == 'POST':
        context['saved'] = False
        profileForm = ProfileSettingModelForm(request.POST, request.FILES, instance=request.user)
        if profileForm.is_valid():
            if profileForm.save():
                password = request.POST.get('password')
                user = main_app_models.User.objects.get(id=request.user.id)
                if(password and len(password)<20):
                    user.set_password(password)
                    user.save()
                context['saved'] = True
    return render(request, 'college/settings/settings-main.html', context = context)

def notice(request):
    context = {}
    context['notice_list'] = main_app_models.CollegeNotice.objects.all()
    return render(request, 'unital/guest/notice/notice.html', context=context)

def notice_detail(request, **kwargs):
    notice = main_app_models.CollegeNotice.objects.get(pk=kwargs.get('pk'))
    context = {}
    context['notice'] = notice
    return render(request, template_name = "unital/guest/notice/detail.html", context=context)

def profile(request):
    return render(request, template_name= 'unital/guest/profile.html')