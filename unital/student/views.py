from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from main_app.models import User

# Create your views here.

app_name='student'

class PortfolioView(TemplateView):
    

    def get_full_path(self):
        return self.request.get_full_path()
    full_path = get_full_path
    # current_path = full_path[full_path.index('/', 1):]
    print("path: ")
    template_name = 'college/student/portfolio/portfolio.html'
    # def get_context_data(self, **kwargs):
    #     context = super(HomePageView, self).get_context_data(**kwargs)
    #     context['notice_list'] = Notice.objects.order_by('-pub_date', '-id')[0:10]
    #     context['college_list'] = College.objects.all()
    #     return context

def portfolio(request, **kwargs):
    full_path = request.get_full_path()
    college = full_path.split('/')[1]
    username = full_path.split('/')[2]
    student = User.objects.get(username=username, user_type='student')
    context = {}
    if student.college.clg_u_name == college:
        context = {"student": student}
    else:
        pass
    return render(request, template_name = 'college/student/portfolio/portfolio.html', context=context)