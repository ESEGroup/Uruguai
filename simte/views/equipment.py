"""
Equipments views
"""

import logging

from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from simte.models import Equipment, Piece
from simte.forms import EquipmentForm

logger = logging.getLogger(__name__)


class EquipmentListView(ListView):
    """
    View listing equipments
    """

    template_name = 'equipment_list.html'
    model = Equipment


class EquipmentEditView(FormView):
    """
    Create/Edit listing equipments
    """

    template_name = 'equipment.html'
    form_class = EquipmentForm
    success_url = reverse_lazy('equipment_list')
