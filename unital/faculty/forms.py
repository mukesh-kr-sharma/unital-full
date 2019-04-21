from django import forms
from main_app.models import CollegeNotice

class CollegeNoticeModelForm(forms.ModelForm):
    class Meta():
        model = CollegeNotice
        fields = "__all__"
        widgets = { 'pub_date': forms.HiddenInput(),
                    'college': forms.HiddenInput(),
                    'department': forms.HiddenInput(),
                    'pub_by': forms.HiddenInput(),
                    'expiry_date': forms.TextInput(attrs={'type': 'date'})}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['link'].required = False
