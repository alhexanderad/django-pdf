from atexit import register
from django.contrib import admin
from producto.models import Product

admin.site.register(Product)

