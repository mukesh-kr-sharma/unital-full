from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.forms.models import modelformset_factory
from django.urls import reverse_lazy
from main_app.models import User
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
        
        TechnicalSkillFormSet = modelformset_factory(TechnicalSkill, form=TechnicalSkillModelForm, extra=0, can_delete=True)
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
        technical_skill = student.portfolio.technical_skill.all()
        skill_title = []
        for skill in technical_skill:
            skill_title.append(skill.skill_title)
        
        context = {"student": student}
        context['academic_projects'] = student.portfolio.project.filter(project_type='Academic Project')
        context['technical_skill_title'] = set(skill_title)
    else:
        pass
    return render(request, template_name = 'college/student/portfolio/portfolio.html', context=context)



# {
#     'object': <Portfolio: Portfolio object (1)>, 
#     'portfolio': <Portfolio: Portfolio object (1)>, 
#     'form': <PortfolioModelForm bound=True, valid=Unknown, fields=(user;career_objective;fb_link;twitter_link;insta_link;github_link)>, 
#     'view': <student.views.PortfolioUpdate object at 0x000001FC762370B8>, 
#     'academic_qualification': <AcademicQualificationModelForm bound=False, valid=Unknown, fields=(portfolio;metric_school;metric_board;metric_percentage;metric_pass_year;inter_school;inter_board;inter_percentage;inter_pass_year;graduation_percentage)>, 
#     'skill_set': <django.forms.formsets.SkillSetFormFormSet object at 0x000001FC76B38978>, 
#     'technical_skill': <django.forms.formsets.TechnicalSkillFormFormSet object at 0x000001FC76B38320>
# }


# <QueryDict: {'csrfmiddlewaretoken': ['Nk8sXJBhSHKe8xNqFSF63qSQi9bij3E9NHiqfvHEWNMfmwVf7E7TOhs1LtGyI6Mb'], 
# 'career_objective': ['To secure a responsible career opportunity to full utilize my knowledge, training and skills, while making a significant contribution to the success of the Mukesh'], 
# 'fb_link': [''], 
# 'twitter_link': [''], 
# 'insta_link': [''], 
# 'github_link': [''], 
# 'metric_school': ['BRL DAV Public Schoo'], 
# 'metric_board': ['CBSE'], 
# 'metric_percentage': ['83.00'], 
# 'metric_pass_year': ['2014'], 
# 'initial-metric_pass_year': ['2014'], 
# 'inter_school': ['BRL DAV Public School'], 
# 'inter_board': ['CBSE'], 
# 'inter_percentage': ['82.00'], 
# 'inter_pass_year': ['2016'], 
# 'initial-inter_pass_year': ['2016'], 
# 'graduation_percentage': ['90.00'], 
# 'skill_set-TOTAL_FORMS': ['2'], 
# 'skill_set-INITIAL_FORMS': ['1'], 
# 'skill_set-MIN_NUM_FORMS': ['0'], 
# 'skill_set-MAX_NUM_FORMS': ['1000'], 
# 'skill_set-0-id': ['2'], 
# 'skill_set-0-skill': ['Reasoning Ability'], 
# 'skill_set-1-skill': ['hiii'], 
# 'skill_set-__prefix__-skill': ['']}>

# <tr><th><label for="id_skill_set-0-skill">Skill:</label></th><td><input type="text" name="skill_set-0-skill" value="Reasoning Ability" maxlength="250" id="id_skill_set-0-skill"></td></tr>

# <tr><th><label for="id_skill_set-0-DELETE">Delete:</label></th><td><input type="checkbox" name="skill_set-0-DELETE" id="id_skill_set-0-DELETE"><input type="hidden" name="skill_set-0-id" value="2" id="id_skill_set-0-id"></td></tr>

# <tr><th><label for="id_skill_set-1-skill">Skill:</label></th><td><input type="text" name="skill_set-1-skill" value="hiii" maxlength="250" id="id_skill_set-1-skill"></td></tr>

# <tr><th><label for="id_skill_set-1-DELETE">Delete:</label></th><td><input type="checkbox" name="skill_set-1-DELETE" id="id_skill_set-1-DELETE"><input type="hidden" name="skill_set-1-id" id="id_skill_set-1-id"></td></tr>