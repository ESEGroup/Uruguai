"""
Inspection forms
"""

import logging

from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from simte.models import Inspection

logger = logging.getLogger(__name__)

class InspectionForm(ModelForm):
    """
    Inspection form
    """

    class Meta:
        model = Inspection
        fields = ['start_date', 'end_date', 'in_type', 'equipment']
