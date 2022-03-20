from django.urls import path, include
from producto.views import producto

app_name='producto'


urlpatterns = [
  path('lista/', producto ,name="listaProsucto"),
]


