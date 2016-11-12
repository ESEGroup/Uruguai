"""
Equipments forms
"""

import logging

from django.forms import ModelForm
from simte.models import Equipment

logger = logging.getLogger(__name__)

class EquipmentForm(ModelForm):
    """
    Equip form
    In future it will have pieces' formsets
    """

    class Meta:
        model = Equipment
        fields = ['status', 'eq_type', 'serial_number']
