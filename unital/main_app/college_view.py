from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Notice, College
from django.shortcuts import get_object_or_404

class CollegeHomepageView(TemplateView):
    template_name = 'college/college-homepage.html'
    def get_context_data(self, **kwargs):
        context = super(CollegeHomepageView, self).get_context_data(**kwargs)
        context['college'] = College.objects.get(clg_u_name=kwargs['clg_u_name'])
        # context['college.notice'] = College.notice.objects.order_by('-pub_date', '-id')[0:10]
        # context['college.notice'] = College.notice.objects.all()
        return context
