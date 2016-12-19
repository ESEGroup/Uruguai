"""
Inspection views
"""

import logging

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from simte.models import Inspection
from simte.forms import InspectionForm
from simte.shortcuts import get_user_equips
from datetimewidget.widgets import DateTimeWidget

logger = logging.getLogger(__name__)


class InspectionListView(LoginRequiredMixin, ListView):
    """
    View listing equipments
    """

    template_name = 'simte/inspection_list.html'
    model = Inspection

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        equips = get_user_equips(user)
        return Inspection.objects.filter(equipment__in=equips)


class InspectionEditView(LoginRequiredMixin, UpdateView):
    """
    Edit equipments
    """

    template_name = 'simte/inspection.html'
    model = Inspection
    fields = ['start_date', 'end_date', 'in_type', 'equipment', 'description', 'assigned_to']
    success_url = reverse_lazy('inspection_list')


class InspectionCreateView(LoginRequiredMixin, CreateView):
    """
    Create equipments
    """

    template_name = 'simte/inspection_add.html'
    model = Inspection
    fields = ['start_date', 'end_date', 'in_type', 'equipment', 'description', 'assigned_to']
    success_url = reverse_lazy('inspection_list')
