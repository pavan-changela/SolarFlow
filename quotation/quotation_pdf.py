from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import re

def render_pdf_view(template_src, context_dict, customer_name):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()

    # Clean filename
    filename = re.sub(r'\\s+', '_', customer_name.strip().lower())

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={filename}_quotation.pdf'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF')
    return response
