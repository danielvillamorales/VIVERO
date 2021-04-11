from django.test import TestCase

# Create your tests here.

from webapp.models.viveros import Viveros

class ViverosModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Viveros.objects.create(codigo='vp78', nombre='vivero prueba')

    def test_codigo_label(self):
        viveros=Viveros.objects.get(id=1)
        field_label = viveros._meta.get_field('codigo').verbose_name
        self.assertEquals(field_label,'codigo')

    def test_nombre_label(self):
        viveros=Viveros.objects.get(id=1)
        field_label = viveros._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_codigo_max_length(self):
        viveros=Viveros.objects.get(id=1)
        max_length = viveros._meta.get_field('codigo').max_length
        self.assertEquals(max_length,4)
