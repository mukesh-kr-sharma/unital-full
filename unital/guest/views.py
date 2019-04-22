from django.shortcuts import render
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
    return render(request, template_name='unital/guest/login.html', context=context)