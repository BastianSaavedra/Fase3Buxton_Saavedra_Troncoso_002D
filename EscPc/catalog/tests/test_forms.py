from django.test import TestCase
from catalog.forms import PlacaForm, ProceForm
from catalog.models import PlacasMadre, Procesadore
from django.core.files.uploadedfile import SimpleUploadedFile

class PlacaFormTest(TestCase):
   
   def test_invalid_form(self):
      with open('catalog/static/fotos/bannerProductos.jpg', 'rb') as file:
         imagen = SimpleUploadedFile(file.name, file.read(), content_type='imagen/png')
      
      
      placa = PlacasMadre.objects.create(
            marca='',
            modelo='b450',
            formato='ATX',
            plataforma='Intel',
            imagen= imagen
         )
      data = {
         'marca': placa.marca,
         'modelo': placa.modelo,
         'formato': placa.formato,
         'plataforma': placa.plataforma,
         'imagen': placa.imagen,
      }
      form = PlacaForm(data=data)
      self.assertFalse(form.is_valid())
      
      
   def test_placa_form_no_data(self):
      form = PlacaForm(data={})
      self.assertFalse(form.is_valid())
      self.assertEqual(len(form.errors), 8)
      
      
class ProceFormTest(TestCase):

   def test_invalid_form(self):
      with open('catalog/static/fotos/bannerProductos.jpg', 'rb') as file:
         imagen = SimpleUploadedFile(file.name, file.read(), content_type='imagen/png')
      
      
      proce = Procesadore.objects.create(
            marca='',
            modelo='b450',
            frecuencia='3000',
            socket='AM4',
            imagen= imagen
         )
      data = {
         'marca': proce.marca,
         'modelo': proce.modelo,
         'frecuencia': proce.frecuencia,
         'socket': proce.socket,
         'imagen': proce.imagen,
      }
      form = ProceForm(data=data)
      self.assertFalse(form.is_valid())
      
   def test_proce_form_no_data(self):
      form = ProceForm(data={})
      self.assertFalse(form.is_valid())
      self.assertEqual(len(form.errors), 8)
      