from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.forms.models import modelformset_factory
from django.urls import reverse_lazy
from main_app.models import User, Syllabus
from .forms import *
from .models import *

# Create your views here.

app_name='student'
# https://micropyramid.com/blog/understanding-djangos-model-formsets-in-detail-and-their-advanced-usage/
def update_portfolio(request, **kwargs):
    if request.method == 'POST':
        portfolio_form = PortfolioModelForm(data=request.POST, instance=get_object_or_404(Portfolio, id=request.user.portfolio.id))
        academic_qualification_form = AcademicQualificationModelForm(data=request.POST, instance=get_object_or_404(AcademicQualification, id=request.user.portfolio.academic_qualification.id))

        SkillSetFormSet = modelformset_factory(SkillSet, form=SkillSetModelForm, can_delete=True)
        skillset_formset = SkillSetFormSet(data=request.POST, prefix="skill_set")

        TechnicalSkillFormSet = modelformset_factory(TechnicalSkill, form=TechnicalSkillModelForm, can_delete=True)
        technicalskill_formset = TechnicalSkillFormSet(data=request.POST, prefix="technical_skill")

        if portfolio_form.is_valid() and academic_qualification_form.is_valid():

            portfolio = portfolio_form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()

            academic_qualification = academic_qualification_form.save(commit=False)
            academic_qualification.portfolio = request.user.portfolio
            academic_qualification.save()
        
        if skillset_formset.is_valid():
            skillset_formset.save()
        
        if technicalskill_formset.is_valid():
            technicalskill_formset.save()

        return redirect(reverse_lazy('redirect'))
    else:
        context = {}
        template_name = 'college/student/portfolio/edit-portfolio.html'
        portfolio_form = PortfolioModelForm(instance=Portfolio.objects.get_or_create(user=request.user.id)[0])
        academic_qualification_form = AcademicQualificationModelForm(instance=AcademicQualification.objects.get_or_create(portfolio=request.user.portfolio.id)[0])


        SkillSetFormSet = modelformset_factory(SkillSet, form=SkillSetModelForm, extra=0, can_delete=True)
        skillset_formset = SkillSetFormSet(queryset=SkillSet.objects.filter(portfolio=request.user.portfolio.id), 
                            prefix="skill_set",
                            initial=[{'portfolio': request.user.portfolio.id,}])
        
        TechnicalSkillFormSet = modelformset_factory(TechnicalSkill, form=TechnicalSkillModelForm, extra=2, can_delete=True)
        technicalskill_formset = TechnicalSkillFormSet(queryset=TechnicalSkill.objects.filter(portfolio=request.user.portfolio.id), 
                             prefix="technical_skill",
                             initial=[{'portfolio': request.user.portfolio.id,}])

        context['portfolio_form'] = portfolio_form
        context['academic_qualification_form'] = academic_qualification_form
        context['skillset_formset'] = skillset_formset
        context['technicalskill_formset'] = technicalskill_formset
        return render(request, template_name = template_name, context=context)

def portfolio(request, **kwargs):
    full_path = request.get_full_path()
    college = full_path.split('/')[1]
    username = full_path.split('/')[2]
    student = User.objects.get(username=username, user_type='student')
    context = {}
    if student.college.clg_u_name == college:
        technical_skill = student.portfolio.technical_skill.all().order_by('-skill_level')
        skill_title = []
        for skill in technical_skill:
            skill_title.append(skill.skill_title)
        
        context = {"student": student}
        context['projects'] = student.portfolio.project.filter(portfolio=request.user.portfolio,)
        context['academic_projects'] = student.portfolio.project.filter(project_type='Academic Project', portfolio=request.user.portfolio)
        context['technical_skill_title'] = set(skill_title)
        context['technical_skill'] = technical_skill
    else:
        pass
    return render(request, template_name = 'college/student/portfolio/portfolio.html', context=context)

def syllabus(request, **kwargs):
    syllabus = Syllabus.objects.get(college=request.user.college, department=request.user.department, session=request.user.session)
    return render(request, template_name = 'college/student/syllabus/syllabus.html', context={'syllabus':syllabus})
