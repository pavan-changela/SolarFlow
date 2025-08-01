# SolarFlow/views.py
from django.shortcuts import render
from quotation.models import Quotation
from projects.models import Project
from payments.models import Payment
from service.models import Complaint

def dashboard(request):
    context = {
        'quotation_count': Quotation.objects.count(),
        'project_count': Project.objects.count(),
        'payment_count': Payment.objects.count(),
        'complaint_count': Complaint.objects.count(),
    }
    return render(request, 'dashboard.html', context)


