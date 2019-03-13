from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Notice, College

# Create your views here.

def afterLoginRedirect(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admin_dashboard')
        else:
            return redirect('students:quiz_list')
    return render(request, 'classroom/home.html')

class HomePageView(TemplateView):
    template_name = 'unital/unital-homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['notice_list'] = Notice.objects.order_by('-pub_date', '-id')[0:10]
        context['college_list'] = College.objects.all()
        return context

class AdminDashboardView(TemplateView):
    template_name = 'unital/admin_dashboard.html'
