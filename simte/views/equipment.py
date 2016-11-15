"""
Equipments views
"""

import logging

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy
from simte.models import Equipment, Piece
from simte.forms import EquipmentForm

logger = logging.getLogger(__name__)


class EquipmentListView(ListView):
    """
    View listing equipments
    """

    template_name = 'simte/equipment_list.html'
    model = Equipment


class EquipmentEditView(UpdateView):
    """
    Edit equipments
    """

    template_name = 'simte/equipment.html'
    model = Equipment
    fields = ['eq_type', 'serial_number']
    success_url = reverse_lazy('equipment_list')

class EquipmentCreateView(CreateView):
    """
    Create equipments
    """

    template_name = 'simte/equipment_add.html'
    model = Equipment
    fields = ['eq_type', 'serial_number']
    success_url = reverse_lazy('equipment_list')
