from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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
    return render(request, template_name='unital/guest/guest-homepage.html')