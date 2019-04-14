from django import forms
from django.forms import inlineformset_factory
from .models import *

class QuestionModelForm(forms.ModelForm):
    class Meta():
        model = Question
        fields = '__all__'

class ReplyModelForm(forms.ModelForm):
    class Meta():
        model = Reply
        fields = '__all__'