from distutils import archive_util
from importlib.resources import contents
from pyexpat import model
from statistics import mode
from tkinter import image_names
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

#Configuracion de ReportLab
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from PIL import Image
import os
import platform
class ListaProducto(ListView):
  model = Product
  context_object_name = 'productos'
  template_name = 'producto/lista.html'
  
def pdf_report(request):
  #Se realizo la configuracion de xhtml2pdf
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
  #Se realizaar con la configuracion de WEASYPRINT
  template = get_template('producto/printpdf.html')
  context = {'productos': Product.objects.all()}
  html = template.render(context).encode(encoding="UTF-8")
  pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()
  return HttpResponse(pdf,content_type='application/pdf')

class ReportePersonasPDF(View):  
  '''La documentacion se realizo es de: https://pythonpiura.wordpress.com/2016/05/13/reporte-pdf-en-django-con-reportlab/'''
  def cabecera(self,pdf):
    #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes

    archivo_imagen = os.path.join(os.path.dirname(os.path.dirname(__file__)),'logo.png')
    #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
    pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)                
        
  def get(self, request, *args, **kwargs):
    #Indicamos el tipo de contenido a devolver, en este caso un pdf
    response = HttpResponse(content_type='application/pdf')
    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
    buffer = BytesIO()
    #Canvas nos permite hacer el reporte con coordenadas X y Y
    pdf = canvas.Canvas(buffer)
    #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
    self.cabecera(pdf)
    #Con show page hacemos un corte de página para pasar a la siguiente
    pdf.showPage()
    pdf.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
  
def pdf_certificado(request):
  #Se verifica el sistema operativo al que nos encontremos.
  sistema = platform.system()
  print("Estamos en {}".format(sistema))
  
  template = get_template('producto/certificado.html')
  context = {
    'producto': Product.objects.get(pk=3),
    'alumno':Product.objects.get(pk=4),
    'circular':Product.objects.get(pk=5),
    'centro':Product.objects.get(pk=6),
    }
  html = template.render(context).encode(encoding="UTF-8")
  pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()
  return HttpResponse(pdf,content_type='application/pdf')
  