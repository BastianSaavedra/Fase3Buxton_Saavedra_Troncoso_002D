from django.test import TestCase, Client
from django.urls import reverse
from catalog.models import PlacasMadre, Procesadore

from django.core.files.uploadedfile import SimpleUploadedFile

class PlacaListViewTest(TestCase):
   @classmethod
   def setUpTestData(cls):
      number_of_placa = 2
      
      for placa_id in range(number_of_placa):
         PlacasMadre.objects.create(
            marca=f'msi {placa_id}',
            modelo=f'b450 {placa_id}',
            formato=f'ATX {placa_id}',
            plataforma=f'Intel {placa_id}',

         )
         
   def test_view_url_exists_at_desired_location(self):
      response = self.client.get('placamadre')
      self.assertEqual(response.status_code, 404)
      
      
class ProceListViewTest(TestCase):
   @classmethod
   
   def setUpTestData(cls):
      number_of_proce = 2
      
      for proce_id in range(number_of_proce):
         test_proce = Procesadore.objects.create(
            marca=f'Intel {proce_id}',
            modelo=f'I7-7700 {proce_id}'
         )
         
         test_proce.save()
         
   def test_view_url_exists_at_desired_location(self):
      response = self.client.get('procesador')
      self.assertEqual(response.status_code, 404)
      