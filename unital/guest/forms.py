from django import forms
from django.forms import inlineformset_factory
from main_app.models import User

class GuestModelForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'dob', 'phone_no', 'gender', 'user_type')
