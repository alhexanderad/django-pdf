from importlib.resources import contents
from pyexpat import model
from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView
from producto.models import Product

class ListaProducto(ListView):
  model = Product
  context_object_name = 'productos'
  template_name = 'producto/lista.html'
  
