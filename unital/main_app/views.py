from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Notice, CollegeList

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'unital/unital-homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['notice_list'] = Notice.objects.order_by('-pub_date', '-id')[0:10]
        context['college_list'] = CollegeList.objects.all()
        return context
