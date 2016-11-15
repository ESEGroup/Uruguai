"""
Inspection views
"""

import logging

from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from simte.models import Inspection
from simte.forms import InspectionForm

logger = logging.getLogger(__name__)


class InspectionListView(ListView):
    """
    View listing equipments
    """

    template_name = 'simte/inspection_list.html'
    model = Inspection


class InspectionEditView(FormView):
    """
    Create/Edit listing equipments
    """

    template_name = 'simte/inspection.html'
    form_class = InspectionForm
    success_url = reverse_lazy('inspection_list')
