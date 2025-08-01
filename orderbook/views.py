# orderbook/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'orderbook/home.html')  # Create this template if needed
