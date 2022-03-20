from django.urls import path, include
from producto.views import ListaProducto

app_name='producto'


urlpatterns = [
  path('lista/', ListaProducto.as_view() ,name="ListaProsucto"),
]


