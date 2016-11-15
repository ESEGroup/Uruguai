"""
Inspection forms
"""

import logging

from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from simte.models import Inspection
from datetimewidget.widgets import DateTimeWidget

logger = logging.getLogger(__name__)

class InspectionForm(ModelForm):
    """
    Inspection form
    """

    class Meta:
        model = Inspection
        fields = ['start_date', 'end_date', 'in_type', 'equipment']
        widget = {
            'start_date': DateTimeWidget(attrs={'id':"start_date"}, usel10n = True, bootstrap_version=3),
            'end_date': DateTimeWidget(attrs={'id':"end_date"}, usel10n = True, bootstrap_version=3),
        }
