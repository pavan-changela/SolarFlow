# projects/forms.py
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['quotation', 'completion_deadline', 'is_completed']
        widgets = {
            'quotation': forms.Select(attrs={'class': 'form-select'}),
            'completion_deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
