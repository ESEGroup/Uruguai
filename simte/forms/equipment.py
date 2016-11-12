"""
Equipments forms
"""

import logging

from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from simte.models import Equipment, Piece

logger = logging.getLogger(__name__)

class EquipmentForm(ModelForm):
    """
    Equip form
    """

    class Meta:
        model = Equipment
        fields = ['status', 'eq_type', 'serial_number']

class PieceForm(ModelForm):
    """
    Piece form to be inlined
    """

    class Meta:
        model = Piece
        fields = ['pc_type', 'serial_number']

PieceFormSet = inlineformset_factory(Equipment, Piece, form=PieceForm, extra=1)
