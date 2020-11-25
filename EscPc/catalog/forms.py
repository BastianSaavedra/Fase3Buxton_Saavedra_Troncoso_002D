#!/usr/bin/python3
from django import forms
from django.forms import ModelForm
from .models import PlacasMadre, Procesadore, Gpu, Ram, Almacenamiento, FuentesPoder, Gabinete, Monitore, Contacto


'''
   AQUI SE ENCUENTRAN LOS FORMULARIOS QUE SE OCUPARAN, EN ESTE CASO ESTAMOS 
   EXTRAYENDO TODOS LOS CAMPOS DE CADA MODELO RESPECTIVAMENTE
'''


class PlacaForm(ModelForm):

   class Meta:
      model = PlacasMadre
      fields = ('marca', 'modelo', 'formato', 'plataforma', 'stock', 
               'imagen', 'imagen_detail', 'precio')

class ProceForm(ModelForm):

   class Meta:
      model = Procesadore
      fields = '__all__'

class GpuForm(ModelForm):

   class Meta:
      model = Gpu
      fields = ('marca', 'modelo', 'plataforma', 'memoria', 'frecuencia', 'stock', 'imagen', 'imagen_detail', 'precio')

class RamForm(ModelForm):

   class Meta:
      model = Ram
      fields = ('marca', 'capacidad', 'tipo', 'frecuencia', 'formato', 'stock', 'imagen', 'imagen_detail', 'precio',)

class AlmacenamientoForm(ModelForm):

   class Meta:
      model = Almacenamiento
      fields = '__all__'

class FuentesPoderForm(ModelForm):

   class Meta:
      model = FuentesPoder
      fields = '__all__'

class GabineteForm(ModelForm):

   class Meta:
      model = Gabinete
      fields = '__all__'

class MonitoreForm(ModelForm):

   class Meta:
      model = Monitore
      fields = '__all__'

class ContactoForm(ModelForm):
   
   class Meta:
      model = Contacto
      fields = '__all__'
      

