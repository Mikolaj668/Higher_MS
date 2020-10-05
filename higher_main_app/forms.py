from django import forms

from higher_main_app.models import *

# class AddMarkForm(forms.Form):
#     name = forms.CharField(label='Your name', max_length=128)

class AddMarkForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['value', 'task', 'candidate', 'recruiter']
