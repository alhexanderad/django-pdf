from importlib.resources import contents
from pyexpat import model
from statistics import mode
from turtle import ht
from django.shortcuts import render
from django.views.generic import ListView
from producto.models import Product

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# from django.views.generic.detail import DetailView
# from django_xhtml2pdf.views import PdfMixin
from weasyprint import HTML
class ListaProducto(ListView):
  model = Product
  context_object_name = 'productos'
  template_name = 'producto/lista.html'
  
def pdf_report(request):
  productos = Product.objects.all()
  print(productos)
  context = {'productos': productos}
  print("asdfasñldmf:",context)
  template_path = 'producto/reportepdf.html'
  # Create a Django response object, and specify content_type as pdf
  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = 'attachment; filename="productos.pdf"'
  # find the template and render it.
  template = get_template(template_path)
  html = template.render(context)

  # create a pdf
  pisa_status = pisa.CreatePDF(html, dest=response)
  # if error then show some funy view
  if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
  return response

def pdf_print(request):
  template = get_template('producto/printpdf.html')
  context = {'productos': Product.objects.all()}
  html = template.render(context).encode(encoding="UTF-8")
  pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()
  return HttpResponse(pdf,content_type='application/pdf')
  