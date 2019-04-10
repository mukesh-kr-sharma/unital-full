from django import forms
from django.forms import inlineformset_factory
from .models import *

class PortfolioModelForm(forms.ModelForm):
    class Meta():
        model = Portfolio
        exclude = ['user',]
    
class AcademicQualificationModelForm(forms.ModelForm):
    class Meta():
        model = AcademicQualification
        exclude = ['portfolio',]

class SkillSetModelForm(forms.ModelForm):
    class Meta():
        model = SkillSet
        fields = '__all__'
        widgets = {'portfolio': forms.HiddenInput()}
        
class TechnicalSkillModelForm(forms.ModelForm):
    class Meta():
        model = TechnicalSkill
        fields = '__all__'
        widgets = {'portfolio': forms.HiddenInput()}