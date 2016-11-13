"""
Inspection views
"""

import logging

from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse
from simte.models import Inspection
from simte.forms import InspectionForm

logger = logging.getLogger(__name__)


class InspectionListView(ListView):
    """
    View listing equipments
    """

    template_name = ''
    model = Inspection


class InspectionEditView(FormView):
    """
    Create/Edit listing equipments
    """

    template_name = ''
    form_class = InspectionForm
    #success_url = reverse('index') # TODO: fix this bug