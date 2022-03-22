from django.urls import path, include
from producto.views import ListaProducto, pdf_report, pdf_print

app_name='producto'


urlpatterns = [
  path('lista/', ListaProducto.as_view() ,name="ListaProsucto"),
  path('pdf/', pdf_report , name="PDF-Producto"),
  path('pdf-print/', pdf_print , name="PDF-Print"),
]


