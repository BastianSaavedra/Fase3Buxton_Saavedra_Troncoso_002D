#!/usr/bin/python3
from django.test import TestCase
from catalog.models import PlacasMadre
class PlacasMadreModelTest(TestCase):

   @classmethod
   def setUpTestData(cls):
      PlacasMadre.objects.create(marca="Asus", modelo="  prueba")

   def test_marca_label(self):
      placa = PlacasMadre.objects.get(id=1)
      field_label = placa._meta.get_field('marca').verbose_name
      self.assertEquals(field_label, 'marca')

   def test_marca_max_lenght(self):
      placa = PlacasMadre.objects.get(id=1)
      field_label = placa._meta.get_field('marca').max_length
      self.assertEquals(field_label, 100)

   def test_modelo_label(self):
      placa = PlacasMadre.objects.get(id=1)
      field_label = placa._meta.get_field('modelo').verbose_name
      self.assertEquals(field_label, 'modelo')

   def test_modelo_max_length(self):
      placa = PlacasMadre.objects.get(id=1)
      max_length = placa._meta.get_field('modelo').max_length
      self.assertEqual(max_length,100)
