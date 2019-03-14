from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Notice, College

# Create your views here.

def redirect_view(request):
    if request.user.is_authenticated:
        if request.user.user_type=='admin':
            return redirect('admin_dashboard')
        else:
            return redirect('unital_homepage')
    return redirect('unital_homepage')


def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_type = request.POST.get('user_type')
    college = request.POST.get('college')
    
    user = authenticate(request, username=username, password=password, user_type=user_type)

    if user is not None:
        login(request, user)
        return redirect('redirect')
    else:
        if request.POST:
            context = {'login-error': 'Invalid Credentials'}
        else:
            context = {}
        return render(request, template_name='unital/unital-homepage.html', context=context)

def user_logout(request):
    # print(request.user.username)
    logout(request)
    return redirect('redirect')

class HomePageView(TemplateView):
    template_name = 'unital/unital-homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['notice_list'] = Notice.objects.order_by('-pub_date', '-id')[0:10]
        context['college_list'] = College.objects.all()
        return context

class AdminDashboardView(TemplateView):
    template_name = 'unital/admin_dashboard.html'
