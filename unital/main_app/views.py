from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Notice, College
from django.urls import reverse_lazy

# Create your views here.
# college = ''

def redirect_view(request):
    if request.user.is_authenticated:
        if request.user.user_type=='admin':
            return redirect('admin_dashboard')
        elif request.user.user_type=='student':
            return redirect('student:homepage',request.user.college.clg_u_name, request.user.username)
        else:
            return redirect('unital_homepage')
    # else:
    #     print(kwargs)
    #     if kwargs and kwargs['college']:
    #         redirect(kwargs['college'])    
    return redirect('unital_homepage')

def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_type = request.POST.get('user_type')
    college = request.POST.get('college')
    
    user = authenticate(request, username=username, password=password)

    if (user is not None) and (user.user_type == user_type):
        login(request, user)
        return redirect('redirect')
    else:
        if request.POST:
            context = {'login-error': 'Invalid Credentials'}
        else:
            context = {}
        return render(request, template_name='unital/unital-homepage.html', context=context)

def user_logout(request):
    college = False
    if hasattr(request.user, 'college') and hasattr(request.user.college, 'clg_u_name'):
        college = request.user.college.clg_u_name
    logout(request)
    if college:
        return redirect('/%s/' % college)
    return redirect(reverse_lazy('redirect'))

class HomePageView(TemplateView):
    template_name = 'unital/unital-homepage.html'
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['notice_list'] = Notice.objects.order_by('-pub_date', '-id')[0:10]
        context['college_list'] = College.objects.all()
        return context

class AdminDashboardView(TemplateView):
    template_name = 'unital/admin_dashboard.html'
