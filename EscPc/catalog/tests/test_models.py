from django.test import TestCase
from . models import PlacasMadre

class PlacasMadreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        PlacasMadre.objects.create(marca="Msi", modelo="B450 TomaHowk")

    def test_marca_label(self):
       placa = PlacasMadre.objects.get(id=3)
       field_label = placa._meta.get_field('marca').verbose_name
       self.assertEquals(field_label, 'marca')

    def test_marca_max_lenght(self):
        placa = PlacasMadre.objects.get(id=3)
        field_label = placa._meta.get_field('marca').max_length
        self.assertEquals(field_label, 'marca')

    def test_modelo_label(self):
        placa = PlacasMadre.objects.get(id=3)
        field_label = placa._meta.get_field('modelo').verbose_name
        self.assertEquals(field_label, 'modelo')

    def test_modelo_max_length(self):
        placa = PlacasMadre.objects.get(id=3)
        max_length = placa._meta.get_field('modelo').max_length
        self.assertEqual(max_length,100)
