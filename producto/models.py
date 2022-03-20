from email.policy import default
from django.db import models
import uuid
import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.forms import model_to_dict

class Product(models.Model):

  nombres             = models.CharField('Nombres',max_length=50)
  correo_electronico  = models.EmailField('Correo Electronico',unique=True)
  imagen          = models.ImageField('Image',upload_to='img/',blank=True, height_field=None, width_field=None, max_length=None)
  ffecha_registro = models.DateTimeField(auto_now_add=True)
  fecha_actualizar    = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Producto'
    verbose_name_plural = 'Productos'
    ordering = ['-id']

  def __str__(self):
    return "{}".format(self.nombres[:25])
  
