# quotation/forms.py
from django import forms
from .models import Quotation

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = [
            'customer', 'quotation_no', 'module_quantity', 'module_wp',
            'inverter_size', 'complete_epc_rate', 'meter_charge',
            'fabrication_rate', 'module_rate', 'inverter_rate'
        ]
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-select'}),
            'quotation_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'module_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'module_wp': forms.NumberInput(attrs={'class': 'form-control'}),
            'inverter_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'complete_epc_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'meter_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'fabrication_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'module_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'inverter_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }
