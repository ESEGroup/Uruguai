from django.test import TestCase
from simte.models.equipment import Equipment, Piece
from simte.models.inspection import Inspection

class EquipmentTestCase(TestCase):
    def setUp(self):
        cadeiraEletrica = Equipment.objects.create(eq_type = "Cadeira Eletrica",serial_number = "66677766677") # Creating an object
        Inspection.objects.create(start_date='1/1/2017',end_date = '5/1/2017',in_type = 'P',equipment = cadeiraEletrica) # Creating an inspection, since it is needed to test is_available

    def test_is_available(self):
        self.assertTrue(cadeiraEletrica.is_available('1/1/2017'),false)


class InspectionTestCase(TestCase):
    def setUp(self)
        inspection = Inspection.objects.create()

    def test_inspection(self):
        self.assertTrue()
