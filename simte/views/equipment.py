"""
Equipments views
"""

import logging

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from simte.models import Equipment, Piece
from simte.forms import EquipmentForm
from simte.shortcuts import get_user_equips

logger = logging.getLogger(__name__)


class EquipmentListView(LoginRequiredMixin, ListView):
    """
    View listing equipments
    """

    template_name = 'simte/equipment_list.html'
    model = Equipment

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        return get_user_equips(user)


class EquipmentEditView(LoginRequiredMixin, UpdateView):
    """
    Edit equipments
    """

    template_name = 'simte/equipment.html'
    model = Equipment
    fields = ['eq_type', 'serial_number', 'department', 'status']
    success_url = reverse_lazy('equipment_list')

    def get_context_data(self, **kwargs):
        context = super(EquipmentEditView, self).get_context_data(**kwargs)
        context['occupied_dates'] = self.object.occupied_dates
        return context

class EquipmentCreateView(LoginRequiredMixin, CreateView):
    """
    Create equipments
    """

    template_name = 'simte/equipment_add.html'
    model = Equipment
    fields = ['eq_type', 'serial_number', 'department', 'status']
    success_url = reverse_lazy('equipment_list')
