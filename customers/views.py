from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomerForm





def home(request):
    return render(request, 'customers/home.html')

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_quotation')  # redirect back to quotation
    else:
        form = CustomerForm()
    return render(request, 'customers/new_customer.html', {'form': form})