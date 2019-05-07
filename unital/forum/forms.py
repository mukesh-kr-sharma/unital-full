from django import forms
from django.forms import inlineformset_factory
from .models import *

class QuestionModelForm(forms.ModelForm):
    class Meta():
        model = Question
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['for_college'].required = False
        self.fields['for_department'].required = False

class ReplyModelForm(forms.ModelForm):
    class Meta():
        model = Reply
        fields = '__all__'