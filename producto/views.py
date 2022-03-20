from importlib.resources import contents
from pyexpat import model
from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView
from producto.models import Product

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# from django.views.generic.detail import DetailView
# from django_xhtml2pdf.views import PdfMixin
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

# class ProductPdfView(PdfMixin):
#     model = Product
#     context_object_name = 'productos'
#     template_name = 'producto/reportepdf.html'