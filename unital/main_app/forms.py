# # https://django-betterforms.readthedocs.io/en/latest/multiform.html#working-with-modelforms
from django import forms
from .models import User

class ProfileSettingModelForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('phone_no', 'address', 'profile_pic',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False
        # self.fields['password'].required = False