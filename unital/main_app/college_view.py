from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Notice, College
from django.shortcuts import get_object_or_404

class CollegeHomepageView(TemplateView):
    template_name = 'college/college-homepage.html'
    def get_context_data(self, **kwargs):
        # # college = get_object_or_404(College, clg_u_name=kwargs['clg_u_name'])
        # college = 'mks'
        # print(kwargs)
        context = super(CollegeHomepageView, self).get_context_data(**kwargs)
        # # context['college_name'] = Notice.objects.order_by('-pub_date', '-id')[0:10]
        # # context['college_list'] = College.objects.all()
        context['college'] = College.objects.get(
            clg_u_name=kwargs['clg_u_name'])
        return context
