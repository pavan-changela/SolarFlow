# service/forms.py
from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['customer', 'complaint_type', 'description','is_resolved']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-select'}),
            'complaint_type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_resolved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
