from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import User, Syllabus
from main_app import models as main_app_models
from main_app.forms import ProfileSettingModelForm
from .forms import *
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
    template_name = 'college/forum/forum-main.html'
    extra_context = {
        'COLLEGE_CHOICES': main_app_models.College.objects.all(),
        'DEPARTMENT_CHOICES': main_app_models.Department.objects.all(),
        'BASE_TEMPLATE' : 'college/faculty/base.html',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_object(self):
        return Question.objects.filter(for_college = self.request.user.college, for_department = self.request.user.department)


#################### SETTINGS #########################
def settings(request, **kwargs):
    context = {'BASE_TEMPLATE':'college/faculty/base.html'}
    if request.method == 'POST':
        context['saved'] = False
        profileForm = ProfileSettingModelForm(request.POST, request.FILES, instance=request.user)
        if profileForm.is_valid():
            if profileForm.save():
                password = request.POST.get('password')
                user = main_app_models.User.objects.get(id=request.user.id)
                if(password and len(password)<20):
                    user.set_password(password)
                    user.save()
                context['saved'] = True
    return render(request, 'college/settings/settings-main.html', context = context)

######################## NOTICE ###########################
def notice_list(request, **kwargs):
    context = {}
    if request.method == 'POST':
        notice_form = CollegeNoticeModelForm(request.POST)
        if notice_form.is_valid():
            if notice_form.save():
                context['saved'] = True
        else:
            print(notice_form)
    notice = main_app_models.CollegeNotice.objects.all()
    context['notice_list'] = notice
    return render(request, template_name = "college/faculty/notice/list.html", context=context)

def notice_detail(request, **kwargs):
    print(kwargs)
    notice = main_app_models.CollegeNotice.objects.get(pk=kwargs.get('pk'))
    context = {}
    context['notice'] = notice
    return render(request, template_name = "college/faculty/notice/detail.html", context=context)

def notice_delete(request, **kwargs):
    notice = get_object_or_404(main_app_models.CollegeNotice, pk=kwargs.get('pk'))    
    if request.method=='POST':
        notice.delete()
        return redirect('faculty:notice-list', clg_u_name=request.user.college.clg_u_name, username=request.user.username)
    return render(request, template_name = "college/faculty/notice/delete.html",context={'notice': notice})

def notice_update(request, **kwargs):
    context = {}
    notice = get_object_or_404(main_app_models.CollegeNotice, pk=kwargs.get('pk'))
    if request.method == 'POST':
        notice_form = CollegeNoticeModelForm(request.POST, instance=notice)
        if notice_form.is_valid():
            if notice_form.save():
                context['saved'] = True
        else:
            print(notice_form)
    context['notice'] = notice
    context['notice_form'] = notice_form = CollegeNoticeModelForm(instance=notice)
    return render(request, template_name = "college/faculty/notice/update.html", context=context)
