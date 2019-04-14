from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from main_app.models import User, Syllabus
from main_app import models as main_app_models
from forum.models import *

class StudentListView(ListView):
    template_name = 'college/faculty/student-list.html'
    model = User
    context_object_name = 'student_list'
    paginate_by = 10

    def get_queryset(self):
        return User.objects.filter(college=self.request.user.college, department=self.request.user.department, user_type='student').order_by('username')

class StudentDetailView(DetailView):
    model = User
    context_object_name = 'student'
    template_name = 'college/faculty/student-detail.html'
    student_username = "student_username"
    # print('hii: ' + str(student_username))

    def get_object(self):
        print(self.request)
        return get_object_or_404(User, username=self.kwargs.get('student_username'))
        # return User.objects.all()[0]


def syllabus(request, **kwargs):
    syllabus = Syllabus.objects.filter(college=request.user.college, department=request.user.department)
    return render(request, template_name = 'college/faculty/syllabus/syllabus.html', context={'syllabus':syllabus})
    
class ForumView(ListView):
    model = Question
    context_object_name = 'question_list'
    template_name = 'college/faculty/forum/forum.html'
    extra_context = {
        'COLLEGE_CHOICES': main_app_models.College.objects.all(),
        'DEPARTMENT_CHOICES': main_app_models.Department.objects.all(),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_object(self):
        return Question.objects.filter(for_college = self.request.user.college, for_department = self.request.user.department)


    
