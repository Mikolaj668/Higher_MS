from django import forms
from django.core.exceptions import ValidationError
from higher_main_app.models import *


class AddMarkForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['value', 'task', 'candidate', 'recruiter']

