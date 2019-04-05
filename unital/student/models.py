from django.db import models
from main_app.models import User
from django.utils.translation import gettext as _
import datetime
# Create your models here.

class PortfolioChoices():
    PROJECT_TYPE = (
        ('Academic Project','Academic Project'),
        ('Non Academic Project', 'Non Academic Project'),
    )
    LANGUAGES_KNOWN = (
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Bhojpuri', 'Bhojpuri'),
    )
    TECHNICAL_SKILL_TITLE = (
        ('Programming Languages', 'Programming Languages'),
        ('Database', 'Database'),
        ('Operating Systems', 'Operating System'),
        ('Web Development (Frontend)', 'Web Development (Frontend)'),
        ('Web Development (Backend)', 'Web Development (Backend)'),
        ('Other', 'Other')
    )
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    MONTH_CHOICES = []
    for r in range(1, 12):
        MONTH_CHOICES.append((r,r))

class Portfolio(models.Model):
    # user = models.ForeignKey("main_app.User", verbose_name=_("Student"), 
    #                         on_delete=models.CASCADE, 
    #                         related_name='portfolio', 
    #                         limit_choices_to={'user_type': 'student'})
    user = models.OneToOneField("main_app.User", verbose_name=_("Student"), on_delete=models.CASCADE, related_name='portfolio', limit_choices_to={'user_type': 'student'}, null=True)
    
    career_objective = models.TextField(_("Career Objective"), 
                        default='To secure a responsible career opportunity to full utilize my knowledge, training and skills, while making a significant contribution to the success of the company/organization. ')
    fb_link = models.URLField(_("Facebook Link"), max_length=200, blank=True)
    twitter_link = models.URLField(_("Twitter Link"), max_length=200, blank=True)
    insta_link = models.URLField(_("Instragram Link"), max_length=200, blank=True)
    github_link = models.URLField(_("Github Link"), max_length=200, blank=True)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)

    class Meta:
        verbose_name_plural = "1. Portfolios"
    

class AcademicQualification(models.Model):
    def current_year():
        return datetime.date.today().year
    portfolio = models.OneToOneField("Portfolio", verbose_name=_("Portfolio"), related_name='academic_qualification',      on_delete=models.CASCADE)
    metric_school = models.CharField(_("10th School"), max_length=150)
    metric_board = models.CharField(_("10th Board"), max_length=50)
    metric_percentage = models.DecimalField(_("10th Percentage"), max_digits=5, decimal_places=2)
    metric_pass_year = models.IntegerField(_('10th Passing Year'), choices=PortfolioChoices.YEAR_CHOICES, default=current_year)
    inter_school = models.CharField(_("12th School/College"), max_length=150)
    inter_board = models.CharField(_("12th Board"), max_length=50)
    inter_percentage = models.DecimalField(_("12th Percentage"), max_digits=5, decimal_places=2)
    inter_pass_year = models.IntegerField(_('12th Passing Year'), choices=PortfolioChoices.YEAR_CHOICES, default=current_year)
    graduation_percentage = models.DecimalField(_("Graduation Percentage"), max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.portfolio.user.first_name) + ' ' + str(self.portfolio.user.last_name)
    
    class Meta:
        verbose_name_plural = "2. Academic Qualifications"
    


class SkillSet(models.Model):
    portfolio = models.ForeignKey("Portfolio", verbose_name=_("Portfolio"), related_name='skill_set',       on_delete=models.CASCADE)
    skill = models.CharField(_("Skill"), max_length=250)
    def __str__(self):
        return '(' + str(self.portfolio.user.username) + '). ' + str(self.skill)
    
    class Meta:
        verbose_name_plural = "3. Skill Set"

class TechnicalSkill(models.Model):
    portfolio = models.ForeignKey("Portfolio", verbose_name=_("Portfolio"), related_name='technical_skill',         on_delete=models.CASCADE)
    skill_title = models.CharField(_("Title"), max_length=100, choices=PortfolioChoices.TECHNICAL_SKILL_TITLE)
    skill = models.CharField(_("Skill"), max_length=50)
    skill_level = models.IntegerField(_("Skill Level"))
    def __str__(self):
        return '(' + str(self.portfolio.user.username) + '). ' + self.skill_title + ' :' + str(self.skill)
    class Meta:
        verbose_name_plural = "4. Technical Skills"

class ProfileSummary(models.Model):
    portfolio = models.ForeignKey("Portfolio", verbose_name=_("Portfolio"), related_name='profile_summary', on_delete=models.CASCADE)
    summary = models.TextField(_("Summary"))
    class Meta:
        verbose_name_plural = "5. Profile Summary"

class Internship(models.Model):
    portfolio = models.ForeignKey("Portfolio", verbose_name=_("Portfolio"), related_name='internship', on_delete=models.CASCADE)
    company = models.CharField(_("Company"), max_length=150)
    duration = models.IntegerField(_("Internship Duration (months)"), choices=PortfolioChoices.MONTH_CHOICES)
    internship_on = models.CharField(_("Internship On"), max_length=50)

    def __str__(self):
        return str(self.portfolio.user.first_name) + ' ' + str(self.portfolio.user.last_name) + ' (' + str(self.company) + ')'
    
    class Meta:
        verbose_name_plural = "7. Internships"
    

class Project(models.Model):
    portfolio = models.ForeignKey("Portfolio", verbose_name=_("Portfolio"), related_name='project', on_delete=models.CASCADE)
    project_type = models.CharField(_("Project Type"), max_length=50, choices=PortfolioChoices.PROJECT_TYPE)
    title = models.CharField(_("Project Title"), max_length=250)
    description = models.TextField(_("Description"))
    github_link = models.URLField(_("Project Github Link"), max_length=200, blank=True)

    def __str__(self):
        return str(self.portfolio.user.first_name) + ' ' + str(self.portfolio.user.last_name) + ' (' + str(self.title) + ')'

    class Meta:
        verbose_name_plural = "8. Projects"

class TechnologyUsed(models.Model):
    project = models.ForeignKey("Project", verbose_name=_("Project"), on_delete=models.CASCADE, related_name='technology_used')
    technology = models.ForeignKey("TechnicalSkill", verbose_name=_("Technology Used"), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project.portfolio.user.first_name) + ' ' + str(self.project.portfolio.user.last_name) + ' (' + str(self.project.title) + ': ' + str(self.technology.skill) + ')'
    
    class Meta:
        verbose_name_plural = '9. Technology Used (in project)'

class Hobbies(models.Model):
    portfolio = models.ForeignKey("Portfolio", verbose_name=_("Portfolio"), on_delete=models.CASCADE)
    hobby = models.CharField(_("Hobby"), max_length=50)
    class Meta:
        verbose_name_plural = "6. Hobbies"


