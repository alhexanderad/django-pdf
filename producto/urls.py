from django.urls import path, include
from producto.views import ListaProducto, ReportePersonasPDF,pdf_report, pdf_print, pdf_certificado

app_name='producto'


urlpatterns = [
  path('lista/', ListaProducto.as_view() ,name="ListaProsucto"),
  path('pdf-report/', ReportePersonasPDF.as_view() , name="PDF-Report"),
  path('pdf-certificado/', pdf_certificado , name="PDF-Certificado"),
  path('pdf/', pdf_report , name="PDF-Producto"),
  path('pdf-print/', pdf_print , name="PDF-Print"),
  
]


