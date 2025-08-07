from django.shortcuts import render, redirect  
from .forms import ComplaintForm
from .models import Complaint

def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, 'service/complaint_list.html', {'complaints': complaints})

def create_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaint_list')
    else:
        form = ComplaintForm()
    return render(request, 'service/create_complaint.html', {'form': form})


