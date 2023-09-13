from django import forms
from . models import Applicant

class Applicantform(forms.ModelForm):
    class Meta:
        model=Applicant
        fields=['full_name','email','phone','college_name']
