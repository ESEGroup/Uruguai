"""
Inspection model
"""

import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger(__name__)


class Inspection(models.Model):
    """
    Inspection model
    """

    TYPE_CHOICES = (
        ('P', _('Preventive')),
        ('F', _('Fix'))
    )

    start_date = models.DateTimeField(verbose_name=_('Start Date'))

    end_date = models.DateTimeField(blank=True,
                                    null=True,
                                    verbose_name=_('End Date'))

    in_type = models.CharField(max_length=2,
                               choices=TYPE_CHOICES,
                               default='P',
                               verbose_name=_('Type'))

    equipment = models.ForeignKey('Equipment')

    def save(self, *args, **kwargs):
        if self.end_date and self.start_date > self.end_date:
            raise ValueError("Start date greater than end date.")
        super(Inspection, self).save(*args, **kwargs)


    def __unicode__(self):
        return "{} ({})".format(self.equipment, self.in_type)
