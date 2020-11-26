from django.test import TestCase, Client
from django.urls import reverse
from catalog.models import PlacasMadre, Procesadore

from django.core.files.uploadedfile import SimpleUploadedFile

class PlacaTestView(TestCase):
   @classmethod
   def setUpTestData(cls):
      number_of_placa = 2
      with open('catalog/static/fotos/bannerProductos.jpg', 'rb') as file:
         imagen = SimpleUploadedFile(file.name, file.read(), content_type='imagen/png')
      
      for placa_id in range(number_of_placa):
         PlacasMadre.objects.create(
            marca=f'msi {placa_id}',
            modelo=f'b450 {placa_id}',
            formato=f'ATX {placa_id}',
            plataforma=f'Intel {placa_id}',
            imagen= imagen

         )
   
   def test_view_url_accessible_by_name(self):
      response = self.client.get(reverse('placamadre'))
      self.assertEqual(response.status_code, 200)
      
   def test_view_uses_correct_template(self):
      response = self.client.get(reverse('placamadre'))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'placasmadres.html', 'base_generic.html')
   

   
   
      
class ProceListViewTest(TestCase):
   @classmethod
   
   def setUpTestData(cls):
      number_of_proce = 2
      with open('catalog/static/fotos/bannerProductos.jpg', 'rb') as file:
         document = SimpleUploadedFile(file.name, file.read(), content_type='imagen/png')
      
      for proce_id in range(number_of_proce):
         test_proce = Procesadore.objects.create(
            marca=f'Intel {proce_id}',
            modelo=f'I7-7700 {proce_id}',
            frecuencia=f'3000mhz {proce_id}',
            socket=f'LGA 1151-v2 {proce_id}',
            imagen= document
         )
         
         test_proce.save()
         
   def  test_view_url_accessible_by_name(self):
      response = self.client.get(reverse('procesador'))
      self.assertEqual(response.status_code, 200)
      
   def test_view_uses_correct_template(self):
      response = self.client.get(reverse('procesador'))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'procesadores.html', 'base_generic.html')
         
   
   
      