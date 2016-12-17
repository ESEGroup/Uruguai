"""
Inspection views
"""

import logging

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy
from simte.models import Inspection
from simte.forms import InspectionForm
from datetimewidget.widgets import DateTimeWidget

logger = logging.getLogger(__name__)


class InspectionListView(ListView):
    """
    View listing equipments
    """

    template_name = 'simte/inspection_list.html'
    model = Inspection


class InspectionEditView(UpdateView):
    """
    Edit equipments
    """

    template_name = 'simte/inspection.html'
    model = Inspection
    fields = ['start_date', 'end_date', 'in_type', 'equipment', 'description', 'assigned_to']
    success_url = reverse_lazy('inspection_list')


class InspectionCreateView(CreateView):
    """
    Create equipments
    """

    template_name = 'simte/inspection_add.html'
    model = Inspection
    fields = ['start_date', 'end_date', 'in_type', 'equipment', 'description', 'assigned_to']
    success_url = reverse_lazy('inspection_list')
