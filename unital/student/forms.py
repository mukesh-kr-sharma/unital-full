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

class ProfileSettingModelForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('phone_no', 'address', 'profile_pic',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False
        # self.fields['password'].required = False