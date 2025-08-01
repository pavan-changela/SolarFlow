from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuotationForm
from .models import Quotation
from .quotation_pdf import render_pdf_view

def create_quotation(request):
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            quotation = form.save()
            return redirect('quotation_success')
    else:
        form = QuotationForm()
    return render(request, 'quotation/create_quotation.html', {'form': form})


def quotation_success(request):
    try:
        latest = Quotation.objects.latest('id')
    except Quotation.DoesNotExist:
        latest = None
    return render(request, 'quotation/success.html', {'quotation': latest})


def quotation_pdf(request, quotation_id):
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    context = {'quotation': quotation}
    return render_pdf_view('quotation/quotation_pdf.html', context, quotation.customer.name)

def quotation_redirect(request):
    return redirect('create_quotation')
